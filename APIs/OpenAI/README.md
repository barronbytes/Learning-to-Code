# Sentimental Analysis with OpenAI

...

## Live Demo

...

## Features

* **Backend:** ...
* **Data Science:** ...

## Prerequisites

Before running this project locally, ensure you have the following installed:

* IDE (VS Code, PyCharm, etc.)
* Install Python 3.10+ version > for type hinting compatability > visit [python download page](https://www.python.org/downloads/)
* Install OpenAI: `pip install openai` > see [API Key Setup](#api-key-setup)
* Install Matplotlib: `pip install matplotlib`
* Install NumPy: `pip install numpy`
* Bourne Shell compatible OS like Linux or macOS > to run test runner script that executes all unit tests in project > Windows users should [download WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)

## Quick Start

Follow the steps below to correctly setup the project on your local device.

### API Key Setup

The purpose of these steps is to prevent publicly exposing your API on the internet.

1. Visit OpenAI page to [create API key](https://platform.openai.com/docs/libraries)
2. Terminal (safely save API Key): `echo 'export API_OPENAI="your_api_key_here"' >> ~/.bashrc && source ~/.bashrc`
3. Python file (imports): `import os`
4. Python file (access API Key): `api_key = os.getenv("API_OPENAI")`

## Usage

...

## Development Roadmap

Overall, this project resembled an ETL pipeline. The following resources were relevant for project completion:
* JSON: [Past file handling mini-project](https://github.com/barronbytes/Learning-to-Code/tree/main/File-Handling) on working with JSON data.
* Data Validation: [Past heart rate monitoring data processing mini-project](https://github.com/barronbytes/Learning-to-Code/tree/main/Data-Science/Summary-Statistics) completed to handle **data extraction**. Specifically, the `get_file_data.py` file within the source code folder.
* OpenAI API: [Official OpenAI API documentation on prompt generation](https://platform.openai.com/docs/guides/prompt-generation) helped me generate prompts for **data transformation**.

## Results

...

## Analysis

...

## Credits and Contributing

...