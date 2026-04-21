import hmac
import hashlib

class Webhooks:
    def __init__(self, client):
        self.client = client

    def verify_signature(self, payload: str, signature: str, secret: str) -> bool:
        expected = hmac.new(
            secret.encode('utf-8'),
            payload.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(expected, signature)
