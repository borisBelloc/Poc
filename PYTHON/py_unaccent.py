import unicodedata

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# How to use :
print(strip_accents('my string : é è à â ê i o ô'))
