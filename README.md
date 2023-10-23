# <img src="https://raw.githubusercontent.com/Cutwell/canary/main/canary.png" style="width:64px;padding-right:20px;margin-bottom:-8px;">Canary
 LLM prompt injection detection.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyTests](https://github.com/Cutwell/canary/actions/workflows/pytest-with-poetry.yaml/badge.svg)
![Pre-commit](https://github.com/Cutwell/canary/actions/workflows/pre-commit.yaml/badge.svg)

## How it works

1. User submits a potentially malicious message.
2. The message is passed through a LLM prompted to format the message plus a unique key into a JSON. In the event the message is a malicious prompt, this output should be compromised. If the output is an invalid JSON, is missing a key, or a key-value doesn't match the expected values, then the integrity may be compromised.
3. If the integrity check passes, the user message is forwarded to the guarded LLM (e.g.: the application chatbot, etc.).
4. The API returns the result of the integrity test (boolean) and either the chatbot response (if integrity passes) or an error message (if integrity fails).

```mermaid
graph TD
    A[1. User Inputs Chat Message] --> B[2. Integrity Filter]
    B -->|Integrity check passes.| C[3. Generate Chatbot Response]
    B -->|Integrity check fails.\n\nResponse is error message.| D
    C -->|Response is chatbot message.| D[4. Return Integrity and Response]
```

What this solution can do:
* Detect inputs that override an LLMs initial / system prompt.

What this solution cannot do:
* Neutralise malicious prompts.

## Install dependencies

If using poetry:

```bash
poetry install
```

If using vanilla pip:

```bash
pip install .
```

## Usage

Set your OpenAI API key in `.envrc`.

To run the project locally, run

```bash
make start
```

This will launch a webserver on port 8001.

Or via docker compose (does not use hot reload by default):

```bash
docker compose up
```

Query the `/chat` endpoint, e.g.: using curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hi how are you?"}' http://127.0.0.1:8000/chat
```

To run unit tests:

```bash
make test
```

## Contributing

For information on how to set up your dev environment and contribute, see [here](.github/CONTRIBUTING.md).

## License

MIT
