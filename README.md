# 🦄 OGD AI Search

**Search semantically, lexically, and multilingually in your OGD metadata catalog.**

![GitHub License](https://img.shields.io/github/license/machinelearningzh/ogd_ai-search)
[![PyPI - Python](https://img.shields.io/badge/python-v3.10+-blue.svg)](https://github.com/machinelearningZH/ogd_ai-search)
[![GitHub Stars](https://img.shields.io/github/stars/machinelearningZH/ogd_ai-search.svg)](https://github.com/machinelearningZH/ogd_ai-search/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/machinelearningZH/ogd_ai-search.svg)](https://github.com/machinelearningZH/ogd_ai-search/issues)
[![GitHub Issues](https://img.shields.io/github/issues-pr/machinelearningZH/ogd_ai-search.svg)](https://img.shields.io/github/issues-pr/machinelearningZH/ogd_ai-search)
[![Current Version](https://img.shields.io/badge/version-0.2-green.svg)](https://github.com/machinelearningZH/ogd_ai-search)
<a href="https://github.com/astral-sh/ruff"><img alt="linting - Ruff" class="off-glb" loading="lazy" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>

<details>
<summary>Contents</summary>

- [Usage](#usage)
- [What does the code do?](#what-does-the-code-do)
- [What is semantic search?](#what-is-semantic-search)
- [Project team](#project-team)
- [Feedback and contributing](#feedback-and-contributing)
- [Disclaimer](#disclaimer)

</details>

![](_imgs/app_ui.png)

## Usage

```bash
# Clone the repository
git clone https://github.com/statistikZH/ogd_ai-search.git
cd ogd_ai-search

# Install uv and dependencies
pip3 install uv
uv venv
source .venv/bin/activate
uv sync
```

- Create an `.env` file and input your OpenAI API keys:

```
    OPENAI_API_KEY=sk-...
```

- Run the notebook and create the search index with the Open Source database [Weaviate](https://weaviate.io/).
- Change into the app directory: `cd _streamlit_app/`
- Start the app: `streamlit run aisearch.py`

## What does the code do?

This application allows you to search the [Canton of Zurich's open government data catalog](https://www.zh.ch/en/politics-state/statistics-data/data-catalog.html#/). It combines exact **lexical keyword searches** with **semantic searches based on meaning and similarity**. The search supports **multiple languages**, including all European languages and many others.

For this prototype app we use OpenAIs embeddings for convenience. We also tested these **open source models with [SentenceTransformers](https://sbert.net/) with very good results**:

- [PM-AI/bi-encoder_msmarco_bert-base_german](https://huggingface.co/PM-AI/bi-encoder_msmarco_bert-base_german) - 350 tokens context length
- [Jina AI jina-embeddings-v2-base-de](https://huggingface.co/jinaai/jina-embeddings-v2-base-de) - 8192 tokens context length

> [!Note]
> The app sends all your search queries to an [embedding interface (API) at OpenAI](https://platform.openai.com/docs/guides/embeddings). Please avoid entering sensitive information that you do not want or are not permitted to share with third-party providers like OpenAI.

## What is semantic search?

Unlike a lexical search, which looks for exact keywords, a semantic search considers text that is semantically similar but does not have to match the search term exactly. For example, a semantic search for the word _disease_ can find documents containing the words _illness_, _virus_, _infection_, _treatment_, or _healthcare_ without the word _disease_ appearing in the documents.

Semantic search uses statistical methods and Machine Learning (ML). By analyzing large amounts of text, ML language models for semantic search have learned word and sentence similarities, enabling them to search for documents based on these similarities. While semantic search has many advantages, it is not exact but approximate. Therefore, **semantic search results itself may not be complete and can include false hits or miss relevant entries**.

**Combining lexical and semantic to hybrid search gives you the best of both worlds.** You get exact lexical but also semantically similar matches in your search results.

## Project Team

**Laure Stadler**, **Chantal Amrhein**, **Patrick Arnecke** – [Statistisches Amt Zürich: Team Data](https://www.zh.ch/de/direktion-der-justiz-und-des-innern/statistisches-amt/data.html)

Many thanks also go to **Corinna Grobe** and our former colleague **Adrian Rupp**.

## Feedback and contributing

We would love to hear from you. Please share your feedback and let us know how you use the code. You can [write an email](mailto:datashop@statistik.zh.ch) or share your ideas by opening an issue or pull request.

Please note that we use [Ruff](https://docs.astral.sh/ruff/) for linting and code formatting with default settings.

## Disclaimer

This software (the Software) incorporates models (Models) from Hugging Face and others and has been developed according to and with the intent to be used under Swiss law. Please be aware that the EU Artificial Intelligence Act (EU AI Act) may, under certain circumstances, be applicable to your use of the Software. You are solely responsible for ensuring that your use of the Software as well as of the underlying Models complies with all applicable local, national and international laws and regulations. By using this Software, you acknowledge and agree (a) that it is your responsibility to assess which laws and regulations, in particular regarding the use of AI technologies, are applicable to your intended use and to comply therewith, and (b) that you will hold us harmless from any action, claims, liability or loss in respect of your use of the Software.
