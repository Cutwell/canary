from ..src.chains import chatbot_chain


def read_test_case(file_path: str) -> str:
    with open(file_path, "r") as file:
        adversarial_prompt = file.read()
    return adversarial_prompt


def assert_chatbot(message: str):
    response = chatbot_chain.invoke({"message": message})

    assert response == "meow", f"Incorrect chatbot response: {response}"
