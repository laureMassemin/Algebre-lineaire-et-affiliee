try:
    from .vector import Vector
    from .matrix import Matrix
except ImportError:
    from vector import Vector
    from matrix import Matrix


class ApplicationLineaire:
    """Represents a linear application"""
    
    def __init__(self, matrix):
        """Initialize a linear application from a matrix."""
        if not isinstance(matrix, Matrix):
            raise TypeError("matrix have to be a Matrix")
        self.matrix = matrix
    
    def __call__(self, vector):
        """Apply the linear transformation to a vector."""
        if not isinstance(vector, Vector):
            raise TypeError("You can only apply with a Vector")
        return self.matrix * vector
    
    def __str__(self):
        return "Linear Application:\n" + str(self.matrix)
    
    def compose(self, other):
        """Compose with another linear application."""
        if not isinstance(other, ApplicationLineaire):
            raise TypeError("You can only compose with a ApplicationLineaire")
        return ApplicationLineaire(self.matrix * other.matrix)
    
    def transpose(self):
        """Return the transpose of this linear application."""
        return ApplicationLineaire(self.matrix.transpose())
    
    def is_invertible(self):
        """Check if the application is invertible."""
        if self.matrix.rows() != self.matrix.cols():
            return False
        try:
            det = self.matrix.determinant()
            return abs(det) > 1e-10
        except NotImplementedError:
            return None


if __name__ == "__main__":
    print("=" * 60)
    print("TESTS: Linear Applications")
    print("=" * 60)
    
    # Test 1: Basic application
    print("\nTest 1: Basic linear transformation")
    print("Matrix:")
    m1 = Matrix([[1, 2], [3, 4]])
    print(m1)
    
    app1 = ApplicationLineaire(m1)
    v1 = Vector([1, 2])
    
    print("Input vector:", v1)
    result1 = app1(v1)
    print("Output:", result1)
    print("Expected: [5, 11] (1*1+2*2=5, 3*1+4*2=11)")
    
    # Test 2: Composition
    print("\nTest 2: Composition of applications")
    m2 = Matrix([[2, 0], [0, 2]])  # Scaling by 2
    m3 = Matrix([[1, 1], [0, 1]])  # Shear transformation
    
    app2 = ApplicationLineaire(m2)
    app3 = ApplicationLineaire(m3)
    
    # Compose: first apply app3, then app2
    app_composed = app2.compose(app3)
    
    v2 = Vector([1, 1])
    print("Input vector:", v2)
    print("app2(app3(v)):", app_composed(v2))
    
    # Verify manually
    temp = app3(v2)
    print("app3(v) =", temp)
    print("app2(app3(v)) =", app2(temp))
    
    # Test 3: Transpose
    print("\nTest 3: Transpose of application")
    m4 = Matrix([[1, 2, 3], [4, 5, 6]])
    app4 = ApplicationLineaire(m4)
    
    print("Original matrix (2x3):")
    print(m4)
    
    app4_transposed = app4.transpose()
    print("Transposed matrix (3x2):")
    print(app4_transposed.matrix)
    
    # Test 4: Invertibility
    print("\nTest 4: Invertibility check")
    m5 = Matrix([[1, 2], [3, 4]])
    app5 = ApplicationLineaire(m5)
    
    print("Matrix:")
    print(m5)
    det5 = m5.determinant()
    print("Determinant:", det5)
    print("Is invertible:", app5.is_invertible())
    
    # Singular matrix
    m6 = Matrix([[1, 2], [2, 4]])  # Singular
    app6 = ApplicationLineaire(m6)
    
    print("\nSingular matrix:")
    print(m6)
    det6 = m6.determinant()
    print("Determinant:", det6)
    print("Is invertible:", app6.is_invertible())

    
    # Test 7: 3D rotation-like application
    print("\nTest 7: 3D linear transformation")
    m9 = Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    app9 = ApplicationLineaire(m9)
    
    v9 = Vector([1, 2, 3])
    print("Matrix (rotation-like):")
    print(m9)
    print("Vector:", v9)
    print("Transformed:", app9(v9))
    
    print("\n" + "=" * 60)
    print("Tests completed")
    print("=" * 60)



