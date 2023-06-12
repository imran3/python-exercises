hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hex_to_dec(hexNum):
    if not isinstance(hexNum, str): return None
    
    charLocation = 0
    res = 0
    for char in reversed(hexNum.upper()):
        if char not in hexNumbers: return None
        
        res += hexNumbers[char] * (16 ** charLocation)
        charLocation +=1
    return res