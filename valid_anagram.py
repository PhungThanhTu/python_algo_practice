
def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    # format the original string by removing nondigit and lowercasing letters
    formatted = ""
    for char in s:
        if char.isalnum():
            formatted += char.lower()
    print(formatted)
    if formatted == "":
        return True
    # start checking the char
    for index in range(int(len(formatted)/2)):
        if formatted[index] == formatted[len(formatted)-index-1]:
            pass
        else:
            return False
    return True