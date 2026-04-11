import hmac
import hashlib

def generate_hmac(key, message):
    if isinstance(message, str):
        message = message.encode()

    return hmac.new(key, message, hashlib.sha256).hexdigest()




# import hmac
# import hashlib

# def generate_hmac(key, message):
#     return hmac.new(key, message, hashlib.sha256).hexdigest()

# def verify_hmac(key, message, received):
#     return generate_hmac(key, message) == received