# <img src="./integrity.png" style="width:64px;padding-right:20px;margin-bottom:-8px;">Integrity
 LLM prompt injection detection

## How it works

1. Potentially malicious user submits input.
2. Input is passed through a prompt designed to accept user input + a unique key generated at runtime.
3. If the output is an invalid JSON or the key doesn't match, then there is a chance of prompt injection.

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
