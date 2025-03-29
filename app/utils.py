import random
import string

def generate_short_code(length=6):
    """Gera um código curto aleatório para a URL"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length)) 