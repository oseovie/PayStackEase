"""
Helpers for handling Paystack meta objects.
"""

def get_meta(response: dict) -> dict:
    """
    Extract the meta object from a Paystack API response.

    :param response: Full API response dictionary
    :return: Meta object if present, else empty dict
    """
    if not isinstance(response, dict):
        return {}
      
    meta = response.get("meta")

    if isinstance(meta, dict):
        return meta


    return response.get("meta", {})
