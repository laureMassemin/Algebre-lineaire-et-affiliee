try:
    from .vector import Vector
except ImportError:
    from vector import Vector

class Matrix :
    """Build a matrix from dimensions or a list of lists."""

    def __init__(self, n, p= None):
        """Initialize a matrix from dimensions or a 2D list."""
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
    
    def rows(self):
        """Return the number of rows."""
        return self.n

    def cols(self):
        """Return the number of columns."""
        return self.p
    
    def get_element(self, i, j):
        """Get element at row i, column j."""
        return self.matrice[i][j]

    def set_element(self, i, j, value):
        """Set element at row i, column j."""
        self.matrice[i][j] = value
    
    def __str__(self):
        """Return a readable string representation."""
        result = "\n"
        for i in range(self.rows()):
            result += "  " + str(self.matrice[i])
            if i < self.rows() - 1:
                result += "\n"
        result += "\n"
        return result
    
    def __add__(self, other):
        """Add two matrices."""
        if not isinstance(other, Matrix):
            raise TypeError("Addition is only supported between two Matrix objects")
        
        if self.rows() != other.rows() or self.cols() != other.cols():
            raise ValueError("Matrices must have the same dimensions")
        
        result = Matrix(self.rows(), self.cols())
        for i in range(self.rows()):
            for j in range(self.cols()):
                result.set_element(i, j, self.get_element(i, j) + other.get_element(i, j))
        return result
    
    def __sub__(self,other):
        """Subtract two matrices"""
        if not isinstance(other, Matrix):
            raise TypeError("Soustraction is only supported between two Matrix objects")
        
        if self.rows() != other.rows() or self.cols() != other.cols():
            raise ValueError("Matrices must have the same dimensions")
        
        result = Matrix(self.rows(), self.cols())
        for i in range(self.rows()):
            for j in range(self.cols()):
                result.set_element(i, j, self.get_element(i, j) - other.get_element(i, j))
        return result

    def __mul__(self,other):
        """Matrix multiplication or scalar multiplication."""
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

    def __eq__(self,other):
        """Check if two Matrix are equal"""
        if not isinstance(other, Matrix):
            return False
        if self.rows() != other.rows() or self.cols() != other.cols():
            return False
        for i in range(self.rows()):
            for j in range(self.cols()):
                if self.get_element(i, j) != other.get_element(i, j):
                    return False
        return True
    
    def transpose(self):
        """Transpose the matrix."""
        result = Matrix(self.cols(), self.rows())
        for i in range(self.rows()):
            for j in range(self.cols()):
                result.set_element(j, i, self.get_element(i, j))
        return result
    
    def determinant(self):
        """Calculate determinant"""
        if self.rows() != self.cols():
            raise ValueError("Determinant only defined for square matrices")
        
        n = self.rows()
        
        # Special case for 1x1 matrix
        if n == 1:
            return self.get_element(0, 0)
        
        # Create a working copy of the matrix
        temp = Matrix(n, n)
        for i in range(n):
            for j in range(n):
                temp.set_element(i, j, self.get_element(i, j))
        
        det = 1.0
        sign = 1
        
        # Gaussian elimination with partial pivoting
        for col in range(n):
            # Find pivot (row with largest absolute value in column col)
            pivot_row = col
            max_val = abs(temp.get_element(col, col))
            for row in range(col + 1, n):
                if abs(temp.get_element(row, col)) > max_val:
                    max_val = abs(temp.get_element(row, col))
                    pivot_row = row
            
            # If pivot is zero, determinant is zero
            if abs(temp.get_element(pivot_row, col)) < 1e-10:
                return 0.0
            
            # Swap rows if needed
            if pivot_row != col:
                for j in range(n):
                    t = temp.get_element(col, j)
                    temp.set_element(col, j, temp.get_element(pivot_row, j))
                    temp.set_element(pivot_row, j, t)
                sign *= -1  # Row swap changes sign of determinant
            
            # Update determinant (multiply by diagonal element)
            det *= temp.get_element(col, col)
            
            # Eliminate below
            for row in range(col + 1, n):
                if abs(temp.get_element(row, col)) > 1e-10:
                    factor = temp.get_element(row, col) / temp.get_element(col, col)
                    for j in range(col, n):
                        new_val = temp.get_element(row, j) - factor * temp.get_element(col, j)
                        temp.set_element(row, j, new_val)
        
        return sign * det


if __name__ == "__main__":
    print("=" * 60)
    print("TESTS: Matrix Operations")
    print("=" * 60)

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    scalar = 2.5

    print("\nm1 =", m1)
    print("m2 =", m2)
    print("Scalaire =", scalar)
    print("m1 lignes =", m1.rows())
    print("m1 colonnes =", m1.cols())

    print("\n--- Basic Matrix Operations ---")
    print("Addition (m1 + m2) :")
    print(m1 + m2)

    print("Soustraction (m1 - m2) :")
    print(m1 - m2)

    print("Multiplication par un scalaire (m1 * 2.5) :")
    print(m1 * scalar)

    print("Multiplication matricielle (m1 * m2) :")
    print(m1 * m2)

    print("\n--- Matrix-Vector Multiplication ---")
    v1 = Vector([1, 2])
    print("m1 * v1 where v1 =", v1)
    print(m1 * v1)

    print("\n--- Transpose ---")
    m3 = Matrix([[1, 2, 3], [4, 5, 6]])
    print("Original matrix (2x3):")
    print(m3)
    m3_t = m3.transpose()
    print("Transposed (3x2):")
    print(m3_t)

    print("\n--- Determinant ---")
    print("2x2 matrix:")
    print(m1)
    det_m1 = m1.determinant()
    print("Determinant:", det_m1)
    print("Expected: 1*4 - 2*3 = -2")

    m4 = Matrix([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    print("\n3x3 matrix:")
    print(m4)
    det_m4 = m4.determinant()
    print("Determinant:", det_m4)
    
    # Test for larger matrices
    m_4x4 = Matrix([[2, 1, 0, 1], 
                     [1, 2, 1, 0], 
                     [0, 1, 2, 1], 
                     [1, 0, 1, 2]])
    print("\n4x4 matrix:")
    print(m_4x4)
    det_4x4 = m_4x4.determinant()
    print("Determinant:", det_4x4)
    
    m_5x5 = Matrix([[1, 2, 0, 0, 1],
                     [0, 3, 1, 0, 0],
                     [2, 0, 1, 2, 0],
                     [0, 1, 0, 4, 1],
                     [1, 0, 2, 0, 2]])
    print("\n5x5 matrix:")
    print(m_5x5)
    det_5x5 = m_5x5.determinant()
    print("Determinant:", det_5x5)

    print("\n--- Equality ---")
    m5 = Matrix([[1, 2], [3, 4]])
    m6 = Matrix([[1, 2], [3, 4]])
    m7 = Matrix([[1, 2], [3, 5]])
    
    print("m5 =", m5)
    print("m6 = (same as m5)")
    print("m7 = (different)")
    print("m5 == m6:", m5 == m6)
    print("m5 == m7:", m5 == m7)

    print("\n--- Element Access ---")
    m8 = Matrix([[10, 20], [30, 40]])
    print("Matrix:", m8)
    print("Element at (0, 0):", m8.get_element(0, 0))
    print("Element at (1, 1):", m8.get_element(1, 1))
    
    m8.set_element(0, 1, 99)
    print("After set_element(0, 1, 99):")
    print(m8)

    print("\n--- Size Variations ---")
    m9 = Matrix(2, 3)
    print("Empty 2x3 matrix:")
    print(m9)

    print("\n--- Error Handling Tests ---")
    try:
        print("Testing error: Matrix('a', 2)")
        Matrix("a", 2)
    except TypeError as e:
        print("✓ Caught:", e)

    try:
        print("Testing error: Matrix([[1, 2], [3]])")
        Matrix([[1, 2], [3]])
    except ValueError as e:
        print("✓ Caught:", e)

    try:
        print("Testing error: m1 + Matrix([[1, 2, 3]])")
        m1 + Matrix([[1, 2, 3]])
    except ValueError as e:
        print("✓ Caught:", e)

    try:
        print("Testing error: m1 * Matrix([[1, 2, 3]])")
        m1 * Matrix([[1, 2, 3]])
    except ValueError as e:
        print("✓ Caught:", e)

    try:
        print("Testing error: Determinant of non-square 2x3 matrix")
        m3.determinant()
    except ValueError as e:
        print("✓ Caught:", e)

    print("\n" + "=" * 60)
    print("Tests completed successfully")
    print("=" * 60)