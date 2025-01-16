import string

def encrypt_text(text, n, m):
    encrypted_text = []
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                new_char = chr(((ord(char) - ord('a') + n * m) % 26) + ord('a'))
            else:
                new_char = chr(((ord(char) - ord('n') - (n + m)) % 26) + ord('n'))
        elif char.isupper():
            if 'A' <= char <= 'M':
                new_char = chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
            else:
                new_char = chr(((ord(char) - ord('N') + m**2) % 26) + ord('N'))
        else:
            new_char = char
        encrypted_text.append(new_char)
    return ''.join(encrypted_text)

def decrypt_text(text, n, m):
    decrypted_text = []
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                new_char = chr(((ord(char) - ord('a') - n * m) % 26) + ord('a'))
            else:
                new_char = chr(((ord(char) - ord('n') + (n + m)) % 26) + ord('n'))
        elif char.isupper():
            if 'A' <= char <= 'M':
                new_char = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
            else:
                new_char = chr(((ord(char) - ord('N') - m**2) % 26) + ord('N'))
        else:
            new_char = char
        decrypted_text.append(new_char)
    return ''.join(decrypted_text)

def check_correctness(original_text, decrypted_text):
    return original_text == decrypted_text

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    while True:
        try:
            n = int(input("Enter the value of n: "))
            m = int(input("Enter the value of m: "))
            break
        except ValueError:
            print("Invalid input. Please enter integer values for n and m.")

    raw_text = read_file('raw_text.txt')
    encrypted_text = encrypt_text(raw_text, n, m)
    write_file('encrypted_text.txt', encrypted_text)

    decrypted_text = decrypt_text(encrypted_text, n, m)
    write_file('decrypted_text.txt', decrypted_text)

    if check_correctness(raw_text, decrypted_text):
        print("Decryption is correct.")
    else:
        print("Decryption is incorrect.")
        print(f"Original Text: {raw_text}")
        print(f"Encrypted Text: {encrypted_text}")
        print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
