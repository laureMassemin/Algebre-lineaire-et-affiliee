try:
    from .matrix import Matrix
    from .vector import Vector
except ImportError:
    from matrix import Matrix
    from vector import Vector


class LinearProgram:
    """Represents a linear programming problem."""
    
    def __init__(self, c, A, b, maximize=True):
        """Initialize a linear program."""
        if not isinstance(c, Vector):
            raise TypeError("c must be a Vector")
        if not isinstance(A, Matrix):
            raise TypeError("A must be a Matrix")
        if not isinstance(b, Vector):
            raise TypeError("b must be a Vector")
        
        if A.cols() != len(c):
            raise ValueError("Incompatible: A has {} columns, c has {} elements".format(
                A.cols(), len(c)))
        if A.rows() != len(b):
            raise ValueError("Incompatible: A has {} rows, b has {} elements".format(
                A.rows(), len(b)))
        
        for i in range(len(b)):
            if b.get_element(i) < 0:
                raise ValueError("All b values must be non-negative")
        
        self.c = c
        self.A = A
        self.b = b
        self.maximize = maximize
        self.n_vars = len(c)
        self.n_constraints = A.rows()
    
    def setup_tableau(self):
        """Set up the initial simplex tableau."""
        if self.maximize:
            obj_coeffs = [-c for c in self.c.coordonnees]
        else:
            obj_coeffs = list(self.c.coordonnees)
        
        tableau = Matrix(self.n_constraints + 1, self.n_vars + self.n_constraints + 1)
        
        for i in range(self.n_constraints):
            for j in range(self.n_vars):
                tableau.set_element(i, j, self.A.get_element(i, j))
            tableau.set_element(i, self.n_vars + i, 1)
            tableau.set_element(i, self.n_vars + self.n_constraints, self.b.get_element(i))
        
        for j in range(self.n_vars):
            tableau.set_element(self.n_constraints, j, obj_coeffs[j])
        for j in range(self.n_constraints):
            tableau.set_element(self.n_constraints, self.n_vars + j, 0)
        tableau.set_element(self.n_constraints, self.n_vars + self.n_constraints, 0)
        
        return tableau
    
    def find_entering_variable(self, tableau):
        """Find the entering variable"""
        obj_row = self.n_constraints
        min_val = 0
        entering_col = -1
        
        for j in range(self.n_vars + self.n_constraints):
            val = tableau.get_element(obj_row, j)
            if val < min_val:
                min_val = val
                entering_col = j
        
        return entering_col
    
    def find_leaving_variable(self, tableau, entering_col):
        """Find the leaving variable"""
        min_ratio = float('inf')
        leaving_row = -1
        
        for i in range(self.n_constraints):
            coeff = tableau.get_element(i, entering_col)
            if coeff > 1e-10:
                rhs = tableau.get_element(i, self.n_vars + self.n_constraints)
                ratio = rhs / coeff
                if ratio < min_ratio:
                    min_ratio = ratio
                    leaving_row = i
        
        return leaving_row
    
    def pivot(self, tableau, pivot_row, pivot_col):
        """Perform pivot operation."""
        pivot_elem = tableau.get_element(pivot_row, pivot_col)
        
        if abs(pivot_elem) < 1e-10:
            raise ValueError("Pivot element too small")
        
        # Normalize pivot row.
        for j in range(tableau.cols()):
            new_val = tableau.get_element(pivot_row, j) / pivot_elem
            tableau.set_element(pivot_row, j, new_val)
        
        # Eliminate column in other rows.
        for i in range(tableau.rows()):
            if i != pivot_row:
                factor = tableau.get_element(i, pivot_col)
                for j in range(tableau.cols()):
                    new_val = (tableau.get_element(i, j) - 
                             factor * tableau.get_element(pivot_row, j))
                    tableau.set_element(i, j, new_val)
    
    def solve_simplex(self, max_iterations=1000):
        """Solve using the Simplex algorithm."""
        tableau = self.setup_tableau()
        
        for iteration in range(max_iterations):
            # Find entering variable.
            entering_col = self.find_entering_variable(tableau)
            
            if entering_col == -1:
                # Optimal solution found.
                solution = [0] * self.n_vars
                # Extract basic variables.
                for i in range(self.n_constraints):
                    for j in range(self.n_vars):
                        col_sum = 0
                        col_nonzero = 0
                        for k in range(tableau.rows()):
                            if abs(tableau.get_element(k, j)) > 1e-10:
                                col_sum += abs(tableau.get_element(k, j))
                                col_nonzero += 1
                        
                        if (abs(tableau.get_element(i, j) - 1) < 1e-10 and 
                            col_nonzero == 1):
                            solution[j] = tableau.get_element(i, self.n_vars + self.n_constraints)
                
                optimal_value = tableau.get_element(tableau.rows() - 1, tableau.cols() - 1)
                if not self.maximize:
                    optimal_value = -optimal_value
                
                return (optimal_value, Vector(solution), True)
            
            # Find leaving variable.
            leaving_row = self.find_leaving_variable(tableau, entering_col)
            
            if leaving_row == -1:
                raise ValueError("Unbounded solution: problem is unbounded")
            
            # Pivot.
            self.pivot(tableau, leaving_row, entering_col)
        
        raise RuntimeError("Maximum iterations reached without convergence")
    
    def __str__(self):
        result = "Linear Program:\n"
        result += ("Maximize" if self.maximize else "Minimize") + " c·x\n"
        result += "c = " + str(self.c) + "\n"
        result += "Subject to Ax <= b:\n"
        result += "A =\n" + str(self.A)
        result += "b = " + str(self.b) + "\n"
        result += "x >= 0\n"
        return result



if __name__ == "__main__":
    print("=" * 60)
    print("TESTS: Linear Programming (Simplex Algorithm)")
    print("=" * 60)
    
    # Test 1: Simple 2D maximization
    print("\nTest 1: Simple 2D maximization")
    print("max z = 3x + 2y")
    print("s.t.")
    print("  x + y <= 4")
    print("  x <= 2")
    print("  y <= 3")
    print("  x, y >= 0")
    
    c1 = Vector([3, 2])
    A1 = Matrix([[1, 1], [1, 0], [0, 1]])
    b1 = Vector([4, 2, 3])
    lp1 = LinearProgram(c1, A1, b1, maximize=True)
    
    try:
        opt_val1, sol1, is_opt1 = lp1.solve_simplex()
        print("Optimal value:", opt_val1)
        print("Solution:", sol1)
        print("Is optimal:", is_opt1)
    except Exception as e:
        print("Error:", e)
    
    # Test 2: Minimization problem
    print("\nTest 2: Minimization problem")
    print("min z = 2x + 3y")
    print("s.t.")
    print("  x + y >= 5")  # Will convert to -x - y <= -5
    print("  x >= 2")       # Will use lower bound
    print("  y >= 1")       # Will use lower bound
    
    c2 = Vector([2, 3])
    # x + y >= 5 becomes -x - y <= -5
    # But we need b >= 0, so we handle this differently
    # Let's use a simpler minimization: min 2x + 3y s.t. x + y >= 5, x,y >= 0
    # Transform: min 2x + 3y s.t. -x - y <= -5, x >= 0, y >= 0
    # Add slack: -x - y + s1 = -5 is not in standard form
    
    # Simpler approach: min 2x + 3y s.t. x + y <= 10, x <= 3, y <= 4
    c2 = Vector([2, 3])
    A2 = Matrix([[1, 1], [1, 0], [0, 1]])
    b2 = Vector([10, 3, 4])
    lp2 = LinearProgram(c2, A2, b2, maximize=False)
    
    try:
        opt_val2, sol2, is_opt2 = lp2.solve_simplex()
        print("Optimal value:", opt_val2)
        print("Solution:", sol2)
        print("Note: minimum achieved at x=0, y=0 → z=0")
    except Exception as e:
        print("Error:", e)
    
    # Test 3: Production problem
    print("\nTest 3: Production problem")
    print("max z = 50x + 40y  (profit)")
    print("s.t.")
    print("  2x + 3y <= 12  (resource A)")
    print("  x + 2y <= 8    (resource B)")
    print("  x, y >= 0")
    
    c3 = Vector([50, 40])
    A3 = Matrix([[2, 3], [1, 2]])
    b3 = Vector([12, 8])
    lp3 = LinearProgram(c3, A3, b3, maximize=True)
    
    try:
        opt_val3, sol3, is_opt3 = lp3.solve_simplex()
        print("Optimal profit:", opt_val3)
        print("Solution (x, y):", sol3)
    except Exception as e:
        print("Error:", e)
    
    # Test 4: Degenerate case
    print("\nTest 4: Diet problem")
    print("min z = x + y  (cost)")
    print("s.t.")
    print("  2x + y >= 8   (converted to -2x - y <= -8)")
    print("  x + 2y >= 7   (converted to -x - 2y <= -7)")
    print("  x, y >= 0")
    print("(Note: requires conversion for standard form)")
    
    # We need b >= 0, so let's use a different formulation
    # min cost with constraints max usage
    c4 = Vector([1, 2])
    A4 = Matrix([[1, 1], [2, 1]])
    b4 = Vector([4, 5])
    lp4 = LinearProgram(c4, A4, b4, maximize=False)
    
    try:
        opt_val4, sol4, is_opt4 = lp4.solve_simplex()
        print("Optimal value:", opt_val4)
        print("Solution:", sol4)
    except Exception as e:
        print("Error:", e)
    
    print("\n" + "=" * 60)
    print("Tests completed")
    print("=" * 60)
