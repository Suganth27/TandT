import random
from crypto import verify_response
from phone import phone_response

def generate_challenge():
    return random.randint(100000,999999)

def reader_authentication():

    challenge = generate_challenge()
    print("Reader challenge:", challenge)

    counter, response = phone_response(challenge)

    if verify_response(counter, challenge, response):
        print("Authentication SUCCESS")
    else:
        print("Authentication FAILED")

reader_authentication()