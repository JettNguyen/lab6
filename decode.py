def decode(encoded):
    decoded = ''
    for char in encoded:
        decoded += (str(int(char) - 3))  # subtracts 3 to each number in the password
    return decoded
