from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    map = dict(Counter(magazine))
    for char in ransomNote:
        try:
            map[char] -= 1
            if map[char] < 0:
                return False
        except  KeyError:
            return False

    return True

def canConstruct2(ransomNote: str, magazine: str) -> bool:
    for char in set(ransomNote):
        if ransomNote.count(char) > magazine.count(char):
            return False

    return True
