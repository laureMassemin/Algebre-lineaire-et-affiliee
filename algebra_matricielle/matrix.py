from ..algebra_lineaire.vector import Vector
class Matrix :

    # Build a matrix from dimensions or a list of lists.
    def __init__(self, n, p= None):
        if isinstance(n, int) and isinstance(p, int):
            self.n = n
            self.p = p
            self.matrice = [[0 for _ in range(p)] for _ in range(n)]
            return
        
        if isinstance(n, list) and p is None:
            if len(n) == 0:
                raise ValueError("All rows must have the same number of columns")
            for i in range(len(n)):
                if not isinstance(n[i], list) or len(n[i]) != len(n[0]):
                    raise ValueError("All rows must have the same number of columns")
                for y in range(len(n[0])):
                    if not isinstance(n[i][y], (int,float)):
                        raise ValueError("All matrix element must be integer or float")
            self.n = len(n)
            self.p = len(n[0])
            self.matrice = n
            return

        raise TypeError("Arguments must be integers or a list of lists")
    
    # Return the number of rows.
    def rows(self):
        return self.n

    # Return the number of columns.
    def cols(self):
        return self.p
    
    # Get element at row i, column j.
    def get_element(self, i, j):
        return self.matrice[i][j]

    # Set element at row i, column j.
    def set_element(self, i, j, value):
        self.matrice[i][j] = value
    
    # Return a readable string representation.
    def __str__(self):
        result = "\n"
        for i in range(self.rows()):
            result += "  " + str(self.matrice[i])
            if i < self.rows() - 1:
                result += "\n"
        result += "\n"
        return result
    
    # Add two matrices with the same dimensions.
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Addition is only supported between two Matrix objects")
        
        if self.rows() != other.rows() or self.cols() != other.cols():
            raise ValueError("Matrices must have the same dimensions")
        
        result = Matrix(self.rows(), self.cols())
        for i in range(self.rows()):
            for j in range(self.cols()):
                result.set_element(i, j, self.get_element(i, j) + other.get_element(i, j))
        return result
    

    # Subtract two matrices with the same dimensions.
    def __sub__(self,other):
        if not isinstance(other, Matrix):
            raise TypeError("Soustraction is only supported between two Matrix objects")
        
        if self.rows() != other.rows() or self.cols() != other.cols():
            raise ValueError("Matrices must have the same dimensions")
        
        result = Matrix(self.rows(), self.cols())
        for i in range(self.rows()):
            for j in range(self.cols()):
                result.set_element(i, j, self.get_element(i, j) - other.get_element(i, j))
        return result

    # Matrix multiplication or scalar multiplication.
    def __mul__(self,other):
        if isinstance(other, (int,float)):
            result = Matrix(self.rows(), self.cols())
            for i in range(self.rows()):
                for j in range(self.cols()):
                    result.set_element(i, j, self.get_element(i, j) * other)
            return result
        
        if isinstance(other, Matrix):
            if self.cols() != other.rows() :
                raise ValueError("Matrices must have compatible dimensions")
            result = Matrix(self.rows(), other.cols())
            for i in range(self.rows()):
                for j in range(other.cols()):
                    total = 0
                    for k in range(self.cols()):
                        total += self.get_element(i, k) * other.get_element(k, j)
                    result.set_element(i, j, total)
            return result

        if isinstance(other, Vector):
            if self.cols() != len(other):
                raise ValueError("Matrix and Vector must have compatible dimensions")
            result = []
            for i in range(self.rows()):
                total = 0
                for k in range(self.cols()):
                    total += self.get_element(i, k) * other.coordonnees[k]
                result.append(total)
            return Vector(result)

        raise TypeError("Multiplication is only supported with a integer, Matrix, or Vector")
    

    # Check if two Matrix are equal element by element.
    def __eq__(self,other):
        if not isinstance(other, Matrix):
            return False
        if self.rows() != other.rows() or self.cols() != other.cols():
            return False
        for i in range(self.rows()):
            for j in range(self.cols()):
                if self.get_element(i, j) != other.get_element(i, j):
                    return False
        return True


if __name__ == "__main__":

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    scalar = 2.5

    print("m1 =", m1)
    print("m2 =", m2)
    print("Scalaire =", scalar)
    print("m1 lignes =", m1.rows())
    print("m1 colonnes =", m1.cols())

    print("Addition (m1 + m2) :")
    print(m1 + m2)

    print("Soustraction (m1 - m2) :")
    print(m1 - m2)

    print("Multiplication par un scalaire (m1 * 2.5) :")
    print(m1 * scalar)

    print("Multiplication matricielle (m1 * m2) :")
    print(m1 * m2)

    # Tests d'erreurs
    # Matrix("a", 2)
    # Matrix(2, "b")
    # Matrix([], None)
    # Matrix([])
    # Matrix([1, 2, 3])
    # Matrix([[1, 2], [3]])
    # Matrix([[1, 2], ["x", 4]])
    # Matrix([[1, 2], []])
    # m1 + "abc"
    # m1 + Matrix([[1, 2, 3]])
    # m1 - "abc"
    # m1 - Matrix([[1, 2, 3]])
    # m1 * "abc"
    # m1 * Matrix([[1, 2, 3]])




    
        