import numpy as np

def compute_eigen_values_vectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

matrix = np.array([[2, 3], [5, 7]])

eigenvalues, eigenvectors =compute_eigen_values_vectors(matrix)
print("Власні значення:")
print(eigenvalues)

print("Власні вектори:")
print(eigenvectors)

def check(eigenvalues, eigenvectors, matrix):
    for i in range(len(eigenvalues)):
        v = eigenvectors[: , i]
        λ = eigenvalues[i]
        λv = λ * v
        Av = np.dot(matrix, v)
        if not np.allclose(Av, λv, atol=1e-08):
            print("Check failed!")
            return False
        print("Everything is correct!")
        return True

check(eigenvalues, eigenvectors, np.array([[2, 3], [5, 7]]))