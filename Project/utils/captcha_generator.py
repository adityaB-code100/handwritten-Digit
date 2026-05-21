import random

def generate_captcha_digit():
    """Generates a random digit (0-9) for the user to draw."""
    return random.randint(0, 9)



import string

def generate_captcha_letter():
    """Generates a random uppercase letter (A-Z) for the user to draw."""
    return random.choice(string.ascii_uppercase)