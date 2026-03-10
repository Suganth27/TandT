import hmac
import hashlib

SECRET_KEY = b"super_secret_key"

def generate_response(counter, challenge):
    message = f"{counter}:{challenge}".encode()
    return hmac.new(SECRET_KEY, message, hashlib.sha256).hexdigest()

def verify_response(counter, challenge, response):
    expected = generate_response(counter, challenge)
    return hmac.compare_digest(expected, response)