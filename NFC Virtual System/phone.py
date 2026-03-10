from crypto import generate_response

counter = 0

def phone_response(challenge):
    global counter
    counter += 1

    response = generate_response(counter, challenge)

    print("Phone counter:", counter)
    print("Phone response:", response)

    return counter, response