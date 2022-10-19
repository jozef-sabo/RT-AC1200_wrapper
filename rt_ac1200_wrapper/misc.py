import re
import base64


def is_ip_valid(ip: str) -> bool:
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    if re.search(regex, ip):
        return True
    return False


def create_authorization_string(username: str, password: str) -> str:
    # username is stripped (trim function), password is not (from Main_Login.asp login() function)
    username = username.strip()
    # Base64 encoded for authorization header (from Main_Login.asp login() function)
    return base64.b64encode(bytes(f"{username}:{password}", encoding="utf-8")).decode("UTF-8")
