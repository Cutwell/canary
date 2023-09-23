import glob

import pytest
from fastapi.testclient import TestClient

from ..src.main import app
from ..src.schema import ChatResponse
from .helpers import read_test_case

client = TestClient(app)


@pytest.mark.parametrize("file_path", glob.glob("canary/tests/adversarial_prompts/*.txt"))
def test_integrity_chain(file_path):
    adversarial_prompt = read_test_case(file_path)

    response = client.post(
        url="/chat",
        headers={"Content-Type": "application/json"},
        json={"message": adversarial_prompt},
    )

    assert (
        response.status_code == 200
    ), f"Unexpected response code: {response.status_code} is not 200."

    response_data = ChatResponse(**response.json())

    assert isinstance(
        response_data.message, str
    ), f"Unexpected message type: {response_data.message} is not str."
    assert isinstance(
        response_data.response, str
    ), f"Unexpected message type: {response_data.response} is not str."
    assert isinstance(
        response_data.integrity, bool
    ), f"Unexpected message type: {response_data.integrity} is not bool."
