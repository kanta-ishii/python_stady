def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    words = text.split()
    return words[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")