import json
import logging
import secrets
import string
from pprint import pformat

from .chains import integrity_llm_chain


def get_secret(N: int = 7) -> str:
    security_key = "".join(
        secrets.choice(string.ascii_uppercase + string.digits) for _ in range(N)
    )

    return security_key


def check_integrity(message: str) -> bool:
    # 0: create a one-time security key
    security_key = get_secret()

    # 1: run input through integrity filter
    json_string = integrity_llm_chain.predict(
        message=message, security_key=security_key
    )

    # 2: try to decode output as json
    try:
        assert json.loads(json_string)

        json_object = json.loads(json_string)

        assert "key" in json_object, "Security key not in JSON."
        assert "message" in json_object, "Message not in JSON."
        assert (
            json_object["key"] == security_key
        ), "Security key does not match expected value."
        assert (
            json_object["message"] == message
        ), "Message does not match expected value."

        return True, None

    # catch JSON decode error separately to show error and custom message
    except json.JSONDecodeError as e:
        response = f"Error decoding JSON string: {e}."
        logging.error(
            pformat({
                'message': message,
                'JSON string': json_string,
                'error': response
            })
        )
        return False, response

    except Exception as error:
        response = str(error)
        logging.error(
            pformat({
                'message': message,
                'JSON': json_object,
                'error': response
            })
        )
        return False, response
