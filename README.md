# <img src="./integrity.png" style="width:64px;padding-right:20px;margin-bottom:-8px;">Integrity
 LLM prompt injection detection

## How it works

1. User submits a potentially malicious message.
2. The message is passed through a LLM prompted to format the message plus a unique key into a JSON. In the event the message is a malicious prompt, this output should be compromised.
3. If the output is an invalid JSON, is missing a key, or a key-value doesn't match the expected values, then the integrity may be compromised.

## Install

1. Clone this repository locally.
2. Create `.envrc` and set `OPENAI_API_KEY` according to `.envrc.example.sh`.
3. Install with poetry.

```bash
make install    # Install dependencies
make test       # Run unit tests to check installation
```

## Usage

* Run `make dev` to run a default `uvicorn` server.
* Run `poetry run python -m uvicorn integrity.src.main:app --reload --port=8000` to customise your deployment settings.

## FastAPI Docs

Visit the `/docs` endpoint of your FastAPI server.

## License

MIT
