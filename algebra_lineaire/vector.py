from math import sqrt

class Vector:
    def __init__(self, coordonnees):
        self.coordonnees = coordonnees


    def __str__(self):
        result = "["
        for i, x in enumerate(self.coordonnees):
            result += str(x)
            if i < len(self.coordonnees) - 1:
                result += ", "
        result += "]"
        return result


    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Addition is only supported between two Vector objects")
        
        if len(self.coordonnees) != len(other.coordonnees):
            raise ValueError("Vectors must have the same length")
    
        sum_coordonnees = []
        for i in range(len(self.coordonnees)):
            sum_coordonnees.append(self.coordonnees[i] + other.coordonnees[i])
        return Vector(sum_coordonnees)
    

    def __sub__(self,other):
        if not isinstance(other, Vector):
            raise TypeError("Soustraction is only supported between two Vector objects")
        
        if len(self.coordonnees) != len(other.coordonnees):
            raise ValueError("Vectors must have the same length")

        sub_coordonnees = []
        for i in range(len(self.coordonnees)):
            sub_coordonnees.append(self.coordonnees[i] - other.coordonnees[i])
        return Vector(sub_coordonnees)
    

    def __mul__(self, other):
        if not isinstance(other, (Vector, int, float)):
            raise TypeError("Multiplication is only supported between two Vectors or between a Vector and a number")
        
        if isinstance(other, Vector) and len(self.coordonnees) != len(other.coordonnees):
            raise ValueError("Vectors must have the same length")
        
        if isinstance(other, Vector):
            produit_scalaire = 0
            for i in range(len(self.coordonnees)):
                produit_scalaire += self.coordonnees[i] * other.coordonnees[i]
            return produit_scalaire

        if isinstance(other, (int,float)):
            mul_coordonnees = []
            for i in range(len(self.coordonnees)):
                mul_coordonnees.append(self.coordonnees[i] * other)
            return Vector(mul_coordonnees)


    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        
        if len(self.coordonnees) != len(other.coordonnees):
            return False
        
        for i in range(len(self.coordonnees)):
            if self.coordonnees[i] != other.coordonnees[i]:
                return False
        
        return True
    
    
    def norme(self):
        sum_coordonnees = 0
        for i in range(len(self.coordonnees)):
            sum_coordonnees+= self.coordonnees[i] **2
        return sqrt(sum_coordonnees)


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
