# import re
def checkio(words: str) -> bool:
    c = 0
    for i in range(len(words.split(' '))):
        try: 
            int(words.split(' ')[i])
            if c <= 2 : c = 0
        except ValueError:
            c += 1
    return True if c >= 3 else False
    # return 'x'*3 in ''.join(['x' if not x.isdigit() else 'y' for x in words.split()])
    # return bool(re.search('([A-Za-z]+ ){2}[A-Za-z]+', words))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("hi four eight seven seven seven 484"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


'''
other answer
    ・'x'*3 in ''.join(['x' if not x.isdigit() else 'y' for x in words.split()])
    ・bool(re.search('([A-Za-z]+ ){2}[A-Za-z]+', words))
'''