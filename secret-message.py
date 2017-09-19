def find_message(text):
    """Find a secret message"""
    strings = ''
    for i in range(0, len(text)):
        if text[i].isupper() == True:
            strings += text[i]

    return strings if strings != '' else ''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
