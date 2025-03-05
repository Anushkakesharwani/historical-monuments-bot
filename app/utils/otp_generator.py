# app/utils/otp_generator.py

import random

def generate_otp():
    # Generate a random 6-digit OTP as a string
    return str(random.randint(100000, 999999))
