def myfunction():
    num = input("Enter string:")
    a = ""
    b = num
    while len(b) > 0:
        if len(b) > 0:
            c = b[-1]
            b = b[:-1]
            a += c
        else:
            break
    if a == num:
        return True
    else:
        return False

"""Function that reverses the order of the words in a sentence, but not the words themselves"""
def reverse_sentence(sentence: str) -> str:
    # lst = split list by whitespace
    reversed_list = lst[::-1]
    res = ""
    for item in reversed_list:
        res += item
        res += " "
    return res
    
def reverse_sentence2(sentence: str) -> str:
    reversed_list = list(filter(reverse, sentence))
    res = ""
    for item in reversed_list:
        res += item
        res += " "
    return res

print(myfunction())

