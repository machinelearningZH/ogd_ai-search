import streamlit as st
import time
from datetime import datetime
from dotenv import load_dotenv
import os
import re
import spacy
import weaviate
import weaviate.classes as wvc
from openai import OpenAI

import logging

logging.basicConfig(
    filename=f"app.log",
    filemode="a",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.WARNING,
)


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# ---------------------------------------------------------------
# Constants and functions


@st.cache_resource
def instantiate_spacy_model():
    """Instantiate spaCy model."""
    return spacy.load("de_core_news_lg")


LETTERS_AND_DIGITS = re.compile(r"[^a-zäüöA-ZÜÄÖ0-9.]")
MULTIPLE_SPACES = re.compile(r"\s+")


def prepare_for_lexical_search(text, lower=False, remove_umlauts=False):
    """Lemmatize text, and optionally lower case and remove umlauts for lexical search.

    Args:
        text (str): Text to process.

    Keyword Arguments:
        lower (bool): Lower case text (default: {True}).
        remove_umlauts (bool): Remove umlauts from text (default: {True}).

    Returns:
        str: Lemmatized text, optionally lower cased, and without umlauts.
    """
    doc = nlp(text)
    text = " ".join([token.lemma_ if token.is_alpha else token.text for token in doc])
    text = re.sub(LETTERS_AND_DIGITS, " ", text)
    text = re.sub(MULTIPLE_SPACES, " ", text)
    if lower:
        text = text.lower()
    if remove_umlauts:
        text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    return text


@st.cache_resource
def get_project_info():
    """Get project info."""
    with open("utils_projectinfo.md") as f:
        return f.read()


def create_project_info(project_info):
    """Create expander for project info. This is the text that will expand at the top section."""
    with st.expander("Detaillierte Informationen zum Projekt"):
        st.markdown(project_info, unsafe_allow_html=True)


@st.cache_resource
def instantiate_weaviate_client():
    """Instantiate Weaviate client."""
    return weaviate.connect_to_embedded()


@st.cache_resource
def count_datasets():
    """Count objects in Weaviate."""
    collection = client.collections.get("MDV")
    response = collection.aggregate.over_all(total_count=True)
    return response.total_count


@st.cache_resource
def instantiate_openai_client():
    return OpenAI()


def embed_with_openai(texts, model="text-embedding-3-small"):
    """Embed text using OpenAIs text embedding model.

    Args:
        texts (list): List of texts to embed.
        model (str): OpenAI model to use (default: {"text-embedding-3-small"}).

    Returns:
        list: List of embeddings.
    """
    response = client_openai.embeddings.create(input=texts, model=model)
    return [x.embedding for x in response.data]


def log_interaction(start_time, raw_search_terms):
    """Log interaction with timestamp, duration, and search terms.

    Args:
        start_time (float): Start time.
        raw_search_terms (str): Raw search terms.
    """
    end_time = time.time()
    logging.warning(
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\t{end_time - start_time:.3f}\t{raw_search_terms}"
    )


def list_results(final_results):
    """List search results."""

    if show_preview_text:
        for result in final_results:
            result = result.properties
            if result["is_study"]:
                st.markdown(
                    f"📚 [{result['title']}]({result['link']})",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"[{result['title']}]({result['link']})",
                    unsafe_allow_html=True,
                )
            description = result["description"].replace("\n", " ")
            description = description.replace(":", " : ")
            st.caption(f"{description}", unsafe_allow_html=True)
    else:
        for result in final_results:
            result = result.properties
            if result["is_study"]:
                st.markdown(
                    f"📚 [{result['title']}]({result['link']})",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"[{result['title']}]({result['link']})",
                    unsafe_allow_html=True,
                )


QUERY_PROPERTIES = [
    "title^2",
    "description",
    "title_lemma^2",
    "description_lemma",
    "theme",
    "theme_lemma",
    "keyword",
    "distribution",
    "distribution_lemma",
]


def search_by_terms():
    """Search by search terms."""

    start_time = time.time()

    raw_search_terms = []
    search_terms = []

    if search_box != "":
        raw_search_terms = search_box

    if raw_search_terms == []:
        return None

    search_terms = raw_search_terms

    # Text has to be lemmatized in the exact same way as the data, that we indexed.
    query = prepare_for_lexical_search(search_terms)
    query_embedding = embed_with_openai(query)[0]

    # We set the Autocut limit to 4.
    # Autocut looks for discontinuities, or jumps, in result metrics such as vector distance or search score.
    # The limit specifies how many jumps there should be in your query.
    # https://weaviate.io/developers/weaviate/api/graphql/additional-operators#autocut
    auto_limit = 4

    if not auto_cut:
        auto_limit = None

    response = collection.query.hybrid(
        query=query,
        query_properties=QUERY_PROPERTIES,
        vector=query_embedding,
        limit=top_k,
        auto_limit=auto_limit,
        alpha=hybrid_balance,
        fusion_type=wvc.query.HybridFusion.RELATIVE_SCORE,
        filters=(
            wvc.query.Filter.by_property("is_study").equal(False)
            | wvc.query.Filter.by_property("is_study").equal(include_studies)
        ),
    )

    list_results(response.objects)
    log_interaction(start_time, raw_search_terms)


# ---------------------------------------------------------------

nlp = instantiate_spacy_model()
client_openai = instantiate_openai_client()

client = instantiate_weaviate_client()
collection = client.collections.get("MDV")

dataset_count = count_datasets()
project_info = get_project_info()


# Create sidebar.
with st.sidebar:
    st.subheader(
        "🔍 :grey[Den Datenkatalog Kanton Zürich] :rainbow[intelligent] :grey[durchsuchen:] :green[lexikalisch], :violet[semantisch] :grey[und] :red[multilingual]."
    )
    st.markdown(
        f"{dataset_count} Datensätze im [Datenkatalog](https://www.zh.ch/de/politik-staat/statistik-daten/datenkatalog.html#/) gefunden.",
        unsafe_allow_html=True,
    )

    search_box = st.text_input(
        "Suchbegriffe oder Suchsatz...",
        value="Croissance démographique de la ville de Zurich",
        max_chars=1000,
        # # Feel free to change the height of the search box.
        # height=100,
        help="Gib hier deine Suchbegriffe oder Suchsätze ein. Du kannst auch mehrere Begriffe oder lange Sätze eingeben. Die Suche ist multilingual und versteht viele Sprachen.",
    )

    top_k = st.slider(
        "Anzahl Suchergebnisse",
        value=50,
        min_value=10,
        max_value=100,
        step=10,
    )

    hybrid_balance = st.slider(
        "Balance lexikalisch / semantisch",
        value=0.7,
        min_value=0.0,
        max_value=1.0,
        step=0.10,
        help="Verhältnis zwischen semantischer und lexikalischer Suche. Je höher der Wert, desto mehr semantische Ergebnisse werden angezeigt. Ein guter Standardwert ist 0.75",
    )
    auto_cut = st.checkbox(
        "Begrenze Ergebnisse automatisch",
        value=True,
        help="Die Sucherergebnisse werden automatisch auf die besten Ergebnisse begrenzt.",
    )

    # Our datacatalog contains studies and reports as well. We can include or exclude them in the search.
    include_studies = st.checkbox(
        "Studien einschliessen",
        value=False,
        help="Suche auch in Studien und Berichten.",
    )
    show_preview_text = st.checkbox("Beschreibung anzeigen", value=False)

    create_project_info(project_info)


search_by_terms()
