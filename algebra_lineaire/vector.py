class Vector:
    # Build a vector from a list of coordinates.
    def __init__(self, coordonnees):
        self.coordonnees = coordonnees

    # Return a readable string representation.
    def __str__(self):
        result = "["
        for i, x in enumerate(self.coordonnees):
            result += str(x)
            if i < len(self) - 1:
                result += ", "
        result += "]"
        return result
    
    # Return the number of coordinates.
    def __len__(self):
        return len(self.coordonnees)

    # Get coordinate at index i.
    def get_element(self, i):
        return self.coordonnees[i]

    # Set coordinate at index i.
    def set_element(self, i, value):
        self.coordonnees[i] = value


    # Add two vectors of the same length.
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Addition is only supported between two Vector objects")
        
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length")
    
        sum_coordonnees = []
        for i in range(len(self)):
            sum_coordonnees.append(self.get_element(i) + other.get_element(i))
        return Vector(sum_coordonnees)
    

    # Subtract two vectors of the same length.
    def __sub__(self,other):
        if not isinstance(other, Vector):
            raise TypeError("Soustraction is only supported between two Vector objects")
        
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length")

        sub_coordonnees = []
        for i in range(len(self)):
            sub_coordonnees.append(self.get_element(i) - other.get_element(i))
        return Vector(sub_coordonnees)
    

    # Dot product with a vector or scalar multiplication.
    def __mul__(self, other):
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


    # Check if two vectors are equal element by element.
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        
        if len(self) != len(other):
            return False
        
        for i in range(len(self)):
            if self.get_element(i) != other.get_element(i):
                return False
        
        return True
    
    # Compute the Euclidean norm.
    def norme(self):
        sum_coordonnees = 0
        for i in range(len(self)):
            sum_coordonnees+= self.get_element(i) **2
        return sum_coordonnees**0.5

    # Return the unit vector with norm 1.
    def normalize(self):
        n = self.norme()
        if n == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self * (1 / n)
    
    # Compute the distance between two vectors.
    def distance(self, other):
        result = self - other
        return result.norme()


if __name__ == "__main__":

    v1 = Vector([1, 2, -58])
    v2 = Vector([3, -1, 4])
    scalar = 2.5

    print("v1 =", v1)
    print("v2 =", v2)
    print("Scalaire =", scalar)

    print("Addition (v1 + v2) :")
    print(v1 + v2)  

    print("Soustraction (v1 - v2) :")
    print(v1 - v2)  

    print("Produit scalaire (v1 * v2) :")
    print(v1 * v2)  

    print("Multiplication par un scalaire (v1 * 2.5) :")
    print(v1 * scalar)  

    print("Test d'égalité :")
    print("v1 == v1 :", v1 == v1)  
    print("v1 == v2 :", v1 == v2)  

    print("Norme de v1 :")
    print(v1.norme()) 

    print("Vecteur normalise de v1 :")
    print(v1.normalize())

    print("Distance entre v1 et v2 :")
    print(v1.distance(v2))

    v3 = Vector([1, 2, 3])
    v3.set_element(1, 99)
    print("v3 apres set_element(1, 99) :")
    print(v3)
    print("v3[1] via get_element :", v3.get_element(1))

    # Tests d'erreurs (decommenter un par un)
    # v1 + "abc"
    # v1 + 3
    # v1 + Vector([1, 2])
    # v1 - "abc"
    # v1 - 3
    # v1 - Vector([1, 2])
    # v1 * "abc"
    # v1 * [1, 2, 3]
    # v1 * Vector([1, 2])
    # Vector([0, 0, 0]).normalize()
    # v1.distance("abc")
    # v1.distance(Vector([1, 2]))
