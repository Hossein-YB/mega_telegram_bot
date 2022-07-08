from string import ascii_letters, digits
from random import choice


async def generic_file_cod():
    letters = ascii_letters + digits
    code = ""
    for _ in range(10):
        code += choice(letters)
    return code

