# 🦄 OGD AI Search

**Semantic, lexical, and multilingual search for your OGD metadata catalog.**

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
- [Overview](#overview)
- [What is semantic search?](#what-is-semantic-search)
- [Project Team](#project-team)
- [Feedback and Contributing](#feedback-and-contributing)
- [Disclaimer](#disclaimer)

</details>

![](_imgs/app_ui.png)

## Usage

```bash
# Clone the repository
git clone https://github.com/statistikZH/ogd_ai-search.git
cd ogd_ai-search

# Install dependencies
pip3 install uv
uv venv
source .venv/bin/activate
uv sync

# Create search index
# Run 01_mdv_search.ipynb to create the Weaviate search index

# Start the app
cd _streamlit
streamlit run ai-search.py
```

## Overview

Search the [Canton of Zurich's open government data catalog](https://www.zh.ch/en/politics-state/statistics-data/data-catalog.html#/) using hybrid search that combines **lexical keyword matching** with **semantic similarity**. The application supports **multiple languages**, including German and all European languages.

The search uses [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) for embeddings via sentence-transformers—a multilingual model optimized for German with a 512-token context length. Search results are powered by [Weaviate](https://weaviate.io/), an open-source vector database.

## What is semantic search?

Semantic search finds text based on meaning rather than exact keywords. For example, searching for _disease_ can return documents containing _illness_, _virus_, _infection_, _treatment_, or _healthcare_ without the exact word _disease_ appearing.

Using statistical methods and Machine Learning, language models learn word and sentence similarities from large text corpora. While semantic search has many advantages, it is approximate rather than exact and **may include false positives or miss relevant entries**.

**Hybrid search combines lexical and semantic approaches**, delivering both exact keyword matches and semantically similar results.

## Project Team

**Laure Stadler**, **Chantal Amrhein**, **Patrick Arnecke** – [Statistisches Amt Zürich: Team Data](https://www.zh.ch/de/direktion-der-justiz-und-des-innern/statistisches-amt/data.html)

Many thanks to **Corinna Grobe** and our former colleague **Adrian Rupp**.

## Feedback and Contributing

We'd love to hear from you. Share your feedback or ideas by [emailing us](mailto:datashop@statistik.zh.ch), opening an issue, or submitting a pull request.

We use [Ruff](https://docs.astral.sh/ruff/) for linting and code formatting with default settings.

## Disclaimer

This software (the Software) incorporates models (Models) from Hugging Face and others and has been developed according to and with the intent to be used under Swiss law. Please be aware that the EU Artificial Intelligence Act (EU AI Act) may, under certain circumstances, be applicable to your use of the Software. You are solely responsible for ensuring that your use of the Software as well as of the underlying Models complies with all applicable local, national and international laws and regulations. By using this Software, you acknowledge and agree (a) that it is your responsibility to assess which laws and regulations, in particular regarding the use of AI technologies, are applicable to your intended use and to comply therewith, and (b) that you will hold us harmless from any action, claims, liability or loss in respect of your use of the Software.
