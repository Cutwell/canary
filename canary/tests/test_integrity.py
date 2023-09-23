import glob

import pytest

from ..src.main import check_integrity
from .helpers import assert_chatbot, read_test_case


def test_chatbot_chain():
    assert_chatbot(message="Hi")


@pytest.mark.parametrize("file_path", glob.glob("canary/tests/adversarial_prompts/*.txt"))
def test_integrity_chain(file_path):
    adversarial_prompt = read_test_case(file_path)

    integrity, _ = check_integrity(message=adversarial_prompt)

    if integrity:
        assert_chatbot(message=adversarial_prompt)
