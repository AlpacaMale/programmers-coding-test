def solution(s, n):
    result = ""
    for char in s:
        c_ascii = ord(char)
        if char.isalpha() and char.isupper():
            result += chr(c_ascii + n) if c_ascii + n < 91 else chr(c_ascii + n - 26)
        elif char.isalpha() and char.islower():
            result += chr(c_ascii + n) if c_ascii + n < 123 else chr(c_ascii + n - 26)
        else:
            result += char
    return result
