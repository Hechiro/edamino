import requests
import json

from time import time as timestamp
from .util import device, headers


class Client:
    def __init__(self, certificate_path=None, proxies=None):
        self.api = "https://service.narvii.com/api/v1"
        self.device_id = device.device_id
        self.certificate_path = certificate_path
        self.proxies = proxies

    def login(self, email: str, password: str):
        data = json.dumps({
            "email": email,
            "v": 2,
            "secret": f"0 {password}",
            "deviceID": self.device_id,
            "clientType": 100,
            "action": "normal",
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(url=f"{self.api}/g/s/auth/login", verify=self.certificate_path, data=data,
                                 headers=headers.Headers(data=data).headers, proxies=self.proxies)

        if response.status_code != 200:
            raise Exception("Error")
        else:
            return response.status_code

