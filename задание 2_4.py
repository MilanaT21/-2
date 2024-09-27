import re

def is_valid_hex_color(color):
    pattern = r'^#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})$'
    return bool(re.match(pattern, color))

color = input()
print(is_valid_hex_color(color))
