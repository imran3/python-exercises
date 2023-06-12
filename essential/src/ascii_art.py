# encode a string like 'AAAAABBBBAAA' as a list of tuples: [('A', 5), ('B', 4), ('A', 3)] 
# meaning that the string has "5 A's, followed by 4 B's, followed by 3 A's"
def encode_art(inputToEncode):
    if not isinstance(inputToEncode, str) or not inputToEncode: return None

    res = []
    currentChar = inputToEncode[0]
    ctr = 0
    for c in inputToEncode + ' ':
        if c != currentChar:
            res.append((currentChar, ctr))
            ctr = 0
            currentChar = c
        ctr += 1

    return res

# given an encodedString, return decoded version
def decode_art(encodedList):
    res = ''
    for char, ctr in encodedList:
        res += char * ctr
    
    return res



art = '''
              ,,_
              (=-'
         /\/\  ))
       ~/    \/ |
       | )___(  |
       |/     \||
ejm98  |'      |'
'''

print(decode_art(encode_art(art)))
