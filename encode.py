def encode(password):
    encoded = ''
    for char in password:
        encoded += (str(int(char) + 3))  # adds 3 to each number in the password
    return encoded

