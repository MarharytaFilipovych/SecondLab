import numpy as np

def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector

def decrypt_message(encrypted_vector, key_matrix):
    key_matrix_inverse = np.linalg.inv(key_matrix)
    decrypted_vector = np.dot(key_matrix_inverse, encrypted_vector)
    decrypted_message = ''.join(chr(int(np.real(np.round(number)))) for number in decrypted_vector)
    return decrypted_message


message = input("Enter a message: ")
key_matrix = np.random.randint(0, 256, (len(message), len(message)))
encrypted_vector = encrypt_message(message, key_matrix)
print(f"Matrix: {key_matrix} ")
print(f'Encrypted message: {encrypted_vector}')
decrypted_message = decrypt_message(encrypted_vector, key_matrix)
print(f"Decrypted message: {decrypted_message}")