def solution(myString, pat):
    if len(myString) < len(pat):
        return 0
    if pat.lower() in myString.lower():
        return 1
    return 0
