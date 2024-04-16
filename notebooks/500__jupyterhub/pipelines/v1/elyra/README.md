<!--
{% comment %}
Copyright 2018-2022 Elyra Authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
{% endcomment %}
-->

NOTE: This is an reference of (https://github.com/elyra-ai/examples)

# Elyra examples

This repository provides a set of examples that explore some of the unique
features provided by Elyra. All examples require Elyra version 3.x.


* Disconnected: This directory contains code which doesnt have the download of data, the data is present with it.
  * Please include PIP_INDEX_URL, PIP_TRUSTED_HOST, SSL_CERT_FILE to the pipeline properties.
    * PIP_INDEX_URL: Base URL of the Python Package Index.
    * PIP_TRUSTED_HOST: Mark this host or host:port pair as trusted.
    * SSL_CERT_FILE: <file> where Storage certs are included.
  * ![Alt text](./pipeline_default.png "Pipeline")

## Pipelines

Use the Elyra Visual Pipeline Editor to [assemble pipelines from Python notebooks or scripts](https://elyra.readthedocs.io/en/stable/user_guide/pipelines.html) without the need for any coding.

### Pipeline tutorials

Tutorials to get started with generic pipelines in Elyra:
- [Run pipelines on Data Science Pipelines](pipelines/run-pipelines-on-data-science-pipelines)
