try:
    from .matrix import Matrix
    from .vector import Vector
except ImportError:
    from matrix import Matrix
    from vector import Vector

class LinearSystem:
    """Represents a system of linear equations Ax = b."""
    
    def __init__(self, matrix_a, vector_b):
        """Initialize a linear system."""
        if not isinstance(matrix_a, Matrix):
            raise TypeError("matrix_a must be a Matrix")
        if not isinstance(vector_b, Vector):
            raise TypeError("vector_b must be a Vector")
        if matrix_a.rows() != len(vector_b):
            raise ValueError("Incompatible dimensions: A has {} rows, b has {} elements".format(matrix_a.rows(), len(vector_b)))
        
        self.A = matrix_a
        self.b = vector_b
        self.m = matrix_a.rows()
        self.n = matrix_a.cols()
    
    def create_augmented_matrix(self):
        """Create augmented matrix [A|b]."""
        aug = Matrix(self.m, self.n + 1)
        for i in range(self.m):
            for j in range(self.n):
                aug.set_element(i, j, self.A.get_element(i, j))
            aug.set_element(i, self.n, self.b.get_element(i))
        return aug
    
    def forward_elimination(self, aug):
        """Forward elimination with partial pivoting."""
        for col in range(min(self.m, self.n)):
            # Find pivot.
            max_row = col
            for row in range(col + 1, self.m):
                if abs(aug.get_element(row, col)) > abs(aug.get_element(max_row, col)):
                    max_row = row
            
            # Swap rows if needed.
            if max_row != col:
                for j in range(self.n + 1):
                    temp = aug.get_element(col, j)
                    aug.set_element(col, j, aug.get_element(max_row, j))
                    aug.set_element(max_row, j, temp)
            
            # Check for zero pivot.
            if abs(aug.get_element(col, col)) < 1e-10:
                continue
            
            # Eliminate below.
            for row in range(col + 1, self.m):
                factor = aug.get_element(row, col) / aug.get_element(col, col)
                for j in range(col, self.n + 1):
                    new_val = aug.get_element(row, j) - factor * aug.get_element(col, j)
                    aug.set_element(row, j, new_val)
    
    def back_substitution(self, aug):
        """Back substitution to find solution."""
        solution = [0] * self.n
        
        for i in range(min(self.m, self.n) - 1, -1, -1):
            if abs(aug.get_element(i, i)) < 1e-10:
                continue
            
            val = aug.get_element(i, self.n)
            for j in range(i + 1, self.n):
                val -= aug.get_element(i, j) * solution[j]
            
            solution[i] = val / aug.get_element(i, i)
        
        return Vector(solution)
    
    def solve_gaussian(self):
        """Solve using Gaussian elimination with partial pivoting."""
        if self.m < self.n:
            raise ValueError("Underdetermined system: more unknowns than equations")
        
        aug = self.create_augmented_matrix()
        self.forward_elimination(aug)
        
        # Check for inconsistency.
        for i in range(self.m):
            all_zero = True
            for j in range(self.n):
                if abs(aug.get_element(i, j)) > 1e-10:
                    all_zero = False
                    break
            if all_zero and abs(aug.get_element(i, self.n)) > 1e-10:
                raise ValueError("Inconsistent system: no solution exists")
        
        return self.back_substitution(aug)
     
    def __str__(self):
        result = "Linear System Ax = b:\n"
        result += "A =\n" + str(self.A)
        result += "b = " + str(self.b) + "\n"
        return result


if __name__ == "__main__":
    print("=" * 50)
    print("TESTS: Linear System Solver")
    print("=" * 50)
    
    # Test 1: Simple 2x2 system
    print("\nTest 1: Simple 2x2 system")
    print("2x + 3y = 8")
    print("4x + y = 10")
    A1 = Matrix([[2, 3], [4, 1]])
    b1 = Vector([8, 10])
    sys1 = LinearSystem(A1, b1)
    
    sol1_gauss = sys1.solve_gaussian()
    print("Solution (Gaussian):", sol1_gauss)
    
    # Verify: Ax = b
    result = A1 * sol1_gauss
    print("Verification A*x =", result)
    print("Expected b =", b1)
    
    # Test 2: 3x3 system
    print("\nTest 2: 3x3 system")
    print("x + 2y + 3z = 14")
    print("2x + 3y + z = 11")
    print("3x + y + 2z = 11")
    A2 = Matrix([[1, 2, 3], [2, 3, 1], [3, 1, 2]])
    b2 = Vector([14, 11, 11])
    sys2 = LinearSystem(A2, b2)
    
    sol2 = sys2.solve_gaussian()
    print("Solution:", sol2)
    
    result2 = A2 * sol2
    print("Verification A*x =", result2)
    print("Expected b =", b2)
    
    # Test 3: Overdetermined system (more equations than unknowns)
    print("\nTest 3: Overdetermined system (3 equations, 2 unknowns)")
    print("x + y = 3")
    print("2x + y = 5")
    print("x + 2y = 4")
    A3 = Matrix([[1, 1], [2, 1], [1, 2]])
    b3 = Vector([3, 5, 4])
    
    try:
        sys3 = LinearSystem(A3, b3)
        sol3 = sys3.solve_gaussian()
        print("Solution:", sol3)
    except ValueError as e:
        print("Error:", e)
    
    # Test 4: Singular matrix (no unique solution)
    print("\nTest 4: Singular matrix")
    A4 = Matrix([[1, 2], [2, 4]])
    b4 = Vector([3, 6])
    
    try:
        sys4 = LinearSystem(A4, b4)
        sol4 = sys4.solve_gaussian()
        print("Solution:", sol4)
    except ValueError as e:
        print("Error (expected):", e)
    
    # Test 5: Inconsistent system
    print("\nTest 5: Inconsistent system")
    A5 = Matrix([[1, 2], [2, 4]])
    b5 = Vector([3, 7])  # Incompatible with row 2
    
    try:
        sys5 = LinearSystem(A5, b5)
        sol5 = sys5.solve_gaussian()
        print("Solution:", sol5)
    except ValueError as e:
        print("Error (expected):", e)
    
    print("\n" + "=" * 50)
    print("Tests completed")
    print("=" * 50)
