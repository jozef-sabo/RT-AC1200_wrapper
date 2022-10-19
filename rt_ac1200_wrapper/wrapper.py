import requests
from . import misc


class AC1200_router(object):
    def __init__(self, ip: str, port: int = 80):
        ip = ip.strip().strip("/")
        if ip == "localhost":
            ip = "127.0.0.1"
        if not misc.check_ip(ip):
            raise ValueError("Inserted IP is not valid")
        self.ip = ip

        assert 65_535 >= port > 0, "Port is not between 1-65535"
        self.port = port




