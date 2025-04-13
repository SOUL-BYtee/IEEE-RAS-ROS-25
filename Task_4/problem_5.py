import re

def is_valid(card):
    if not re.fullmatch(r'[456]\d{3}(-?\d{4}){3}', card):
        return False
    card_digits = card.replace('-', '')
    if re.search(r'(\d)\1{3,}', card_digits):
        return False
    return True

n = int(input())
for _ in range(n):
    card = input().strip()
    print('Valid' if is_valid(card) else 'Invalid')
