import requests
from . import misc


class AC1200_router(object):
    def __init__(self, ip: str, username: str, password: str, port: int = 80):
        ip = ip.strip().strip("/")
        if ip == "localhost":
            ip = "127.0.0.1"
        if not misc.is_ip_valid(ip):
            raise ValueError("Inserted IP is not valid")
        self.ip = ip

        assert 65_535 >= port > 0, "Port is not between 1-65535"
        self.port = port

        assert username, "Username was not set"
        assert password, "Password was not set"
        self.authorization = misc.create_authorization_string(username, password)





