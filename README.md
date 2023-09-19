# integrity
LLM prompt injection detection

1. Potentially malicious user submits input.
2. Input is passed through a prompt designed to accept user input + a unique key generated at runtime.
3. If the output is an invalid JSON or the key doesn't match, then there is a chance of prompt injection.
