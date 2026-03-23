def generate_challenge():
    return b"random_challenge"



# PROTOCOL = {
#     "step1": "Receiver generates challenge",
#     "step2": "Transmitter computes HMAC(secret, counter + challenge)",
#     "step3": "Transmitter sends response",
#     "step4": "Receiver verifies response",
#     "step5": "Access granted/denied"
# }