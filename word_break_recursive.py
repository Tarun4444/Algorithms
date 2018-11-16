def dictionaryContains(word):
    dictionary=[
                "mobile","samsung","sam",
                "sung","man","mango","icecream",
                "and","go","i","like","ice","cream"
            ]
    size=len(dictionary)
    for i in range(size):
        if dictionary[i] == word:
            return True
    return False

def wordBreak(s):
    n=len(s)
    if n==0:
        return True
    for i in range(1,n+1):
        if dictionaryContains(s[:i]) and wordBreak(s[i:]):
            return True
    return False

print("yes") if wordBreak("hola") else print("No")
