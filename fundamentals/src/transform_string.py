# given an input string, do following replacement: a->4, e->3, i->1, s->5

replaceMap = {
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "s": "5"
}

def hacker_speak(input: str):
    for k in replaceMap:
        input = input.replace(k, replaceMap[k])
    return input