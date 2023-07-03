def solution(myString, pat):
    myString = myString.replace('A', 'b').replace('B', 'a').upper()
    if pat in myString:
        return 1
    else:
        return 0