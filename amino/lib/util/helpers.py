import hmac
import json
import os

from base64 import b64encode, urlsafe_b64decode
from hashlib import sha1

def generate_device_id() -> str:
    identifier = os.urandom(20)
    key = bytes.fromhex("E7309ECC0953C6FA60005B2765F99DBBC965C8E9")
    mac = hmac.new(key, bytes.fromhex("19") + identifier, sha1)
    return f"19{identifier.hex()}{mac.hexdigest()}".upper()

def generate_signature(data) -> str:
    try: d = data.encode("utf-8")
    except Exception: d = data

    mac = hmac.new(bytes.fromhex("DFA5ED192DDA6E88A12FE12130DC6206B1251E44"), d, sha1)
    return b64encode(bytes.fromhex("19") + mac.digest()).decode("utf-8")

def generate_device_info():
    return {
        "device_id": generate_device_id(),
        "user_agent": "Apple iPhone13,4 iOS v15.6.1 Main/3.12.9"
    }

# okok says: please use return annotations :(( https://www.python.org/dev/peps/pep-3107/#return-values

def decode_sid(sid: str) -> dict:
    return json.loads(urlsafe_b64decode(sid + "=" * (4 - len(sid) % 4))[1:-20])

def sid_to_uid(SID: str) -> str: return decode_sid(SID)["2"]

def sid_to_ip_address(SID: str) -> str: return decode_sid(SID)["4"]

def sid_created_time(SID: str) -> str: return decode_sid(SID)["5"]

def sid_to_client_type(SID: str) -> str: return decode_sid(SID)["6"]
