"""Clean Code in Python - Chapter 1: Introduction, Tools, and Formatting

> Extra code for isolated examples
"""


def data_from_response(response: dict) -> dict:
    """If the response is OK, return its payload.
    - response: A dict like::
    {
        "status": 200, # <int>
        "timestamp": "....", # ISO format string of the current date time
        "payload": { ... } # dict with the returned data
    }
    - Returns a dictionary like::
    {"data": { .. } }

    - Raises:
    - ValueError if the HTTP status is != 200
    """
    if response["status"] != 200:
        raise ValueError
    return {"data": response["payload"]}
