def palindrome(intext):
    input = str(intext).replace(" ", "")
    return input.lower() == input[::-1].lower()
