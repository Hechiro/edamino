from amino.util import device

sid = None
device = device.DeviceGenerator()


class Headers:
    def __init__(self, data=None, content_type=None):
        headers = {
            "NDCDEVICEID": device.device_id,
            "NDC-MSG-SIG": device.device_id_sig,
            "Accept-Language": "en-US",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": device.user_agent,
            "Host": "service.narvii.com",
            "Accept-Encoding": "gzip",
            "Connection": "Keep-Alive"
        }

        if data:
            headers["Content-Length"] = str(len(data))
        if sid:
            headers["NDCAUTH"] = f"sid={sid}"
        if content_type:
            headers["Content-Type"] = content_type
        self.headers = headers
