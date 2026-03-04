class Vector: 
    def __init__(self, coordonnees):
        """Initialize a vector with coordinates."""
        self.coordonnees = coordonnees

    def __str__(self):
        """Return a readable string representation."""
        result = "["
        for i, x in enumerate(self.coordonnees):
            result += str(x)
            if i < len(self) - 1:
                result += ", "
        result += "]"
        return result
    
    def __len__(self):
        """Return the number of coordinates."""
        return len(self.coordonnees)

    def get_element(self, i):
        """Get coordinate at index i."""
        return self.coordonnees[i]

    def set_element(self, i, value):
        """Set coordinate at index i."""
        self.coordonnees[i] = value

    def __add__(self, other):
        """Add two vectors of the same length."""
        if not isinstance(other, Vector):
            raise TypeError("Addition is only supported between two Vector objects")
        
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length")
    
        sum_coordonnees = []
        for i in range(len(self)):
            sum_coordonnees.append(self.get_element(i) + other.get_element(i))
        return Vector(sum_coordonnees)

    def __sub__(self,other):
        """Subtract two vectors of the same length."""
        if not isinstance(other, Vector):
            raise TypeError("Soustraction is only supported between two Vector objects")
        
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length")

        sub_coordonnees = []
        for i in range(len(self)):
            sub_coordonnees.append(self.get_element(i) - other.get_element(i))
        return Vector(sub_coordonnees)

    def __mul__(self, other):
        """Dot product with a vector or scalar multiplication."""
        if not isinstance(other, (Vector, int, float)):
            raise TypeError("Multiplication is only supported between two Vectors or between a Vector and a number")
        
        if isinstance(other, Vector) and len(self) != len(other):
            raise ValueError("Vectors must have the same length")
        
        if isinstance(other, Vector):
            produit_scalaire = 0
            for i in range(len(self)):
                produit_scalaire += self.get_element(i) * other.get_element(i)
            return produit_scalaire

        if isinstance(other, (int,float)):
            mul_coordonnees = []
            for i in range(len(self)):
                mul_coordonnees.append(self.get_element(i) * other)
            return Vector(mul_coordonnees)

    def __eq__(self, other):
        """Check if two vectors are equal."""
        if not isinstance(other, Vector):
            return False
        
        if len(self) != len(other):
            return False
        
        for i in range(len(self)):
            if self.get_element(i) != other.get_element(i):
                return False
        
        return True
    
    def norme(self):
        """Compute the norm."""
        sum_coordonnees = 0
        for i in range(len(self)):
            sum_coordonnees+= self.get_element(i) **2
        return sum_coordonnees**0.5

    def normalize(self):
        """Return the unit vector with norm 1."""
        n = self.norme()
        if n == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self * (1 / n)
    
    def distance(self, other):
        """Compute the distance between two vectors."""
        result = self - other
        return result.norme()
    
    
if __name__ == "__main__":
    print("=" * 60)
    print("TESTS: Vector Operations")
    print("=" * 60)

    v1 = Vector([1, 2, -58])
    v2 = Vector([3, -1, 4])
    scalar = 2.5

    print("\nv1 =", v1)
    print("v2 =", v2)
    print("Scalaire =", scalar)

    print("\n--- Basic Operations ---")
    print("Addition (v1 + v2) :")
    print(v1 + v2)  

    print("Soustraction (v1 - v2) :")
    print(v1 - v2)  

    print("Produit scalaire (v1 * v2) :")
    print(v1 * v2)  

    print("Multiplication par un scalaire (v1 * 2.5) :")
    print(v1 * scalar)  

    print("\n--- Equality Tests ---")
    print("v1 == v1 :", v1 == v1)  
    print("v1 == v2 :", v1 == v2)  

    print("\n--- Norms and Normalization ---")
    print("Norme de v1 :")
    print(v1.norme()) 

    print("Vecteur normalise de v1 :")
    print(v1.normalize())

    print("\n--- Distance ---")
    print("Distance entre v1 et v2 :")
    print(v1.distance(v2))

    print("\n--- Element Access ---")
    v3 = Vector([1, 2, 3])
    v3.set_element(1, 99)
    print("v3 apres set_element(1, 99) :")
    print(v3)
    print("v3[1] via get_element :", v3.get_element(1))


    print("\n--- Error Handling Tests ---")
    try:
        print("Testing error: v1 + 'abc'")
        v1 + "abc"
    except TypeError as e:
        print("✓ Caught:", e)

    try:
        print("Testing error: v1 + Vector([1, 2])")
        v1 + Vector([1, 2])
    except ValueError as e:
        print("✓ Caught:", e)

    try:
        print("Testing error: Vector([0, 0, 0]).normalize()")
        Vector([0, 0, 0]).normalize()
    except ValueError as e:
        print("✓ Caught:", e)

    try:
        print("Testing error: v1.distance(Vector([1, 2]))")
        v1.distance(Vector([1, 2]))
    except ValueError as e:
        print("✓ Caught:", e)

    print("\n" + "=" * 60)
    print("Tests completed successfully")
    print("=" * 60)
