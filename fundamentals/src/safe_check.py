
from enum import Enum

class SafeCheckResult(Enum):
    CLEAN = "Safe watching!"
    BANNED = "No!"

ban_list = ["Dog", "pet", "Music", "Funny meme", "Listen to this"]
ban_list_lowercase = list(map(str.lower, ban_list))

# given an input string, check if it contains banned words and phrases
def safe_check(input_text: str):
    input_text = input_text.lower()
    for word in ban_list_lowercase:
        if word in input_text:
            return SafeCheckResult.BANNED.value
    return SafeCheckResult.CLEAN.value

def safe_check_v2(input_text: str):
    res =  any(word in input_text.lower() for word in ban_list_lowercase)
    print("REDS", res)
    return SafeCheckResult.BANNED.value if res else SafeCheckResult.CLEAN.value
