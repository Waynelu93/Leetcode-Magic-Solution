# https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str1), 1, -1):
            substr = str1[:i]
            if consist(str1, substr) and consist(str2, substr):
                return substr
        return ""

def consist(target: str, substr: str) -> bool:
    index = 0
    substrLen = len(substr)
    while True:
        if target[index: index + substrLen] == "":
            break
        if target[index: index + substrLen] != substr:
            return False
        index += substrLen
    return True
