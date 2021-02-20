def sum_numbers(text: str) -> int:
    # your code here
    s, c = text.split(' '), 0
    for i in range(len(s)):
        if s[i].isdigit(): c = c + int(s[i])
    return c


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")


'''
other answer
    ・sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())
    ・sum(int(word) for word in text.split() if word.isdigit())
'''