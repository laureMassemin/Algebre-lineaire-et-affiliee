from .vector import Vector
from .matrix import Matrix

class ApplicationLineaire:
    def __init__(self, matrix):
        if not isinstance(matrix, Matrix):
            raise TypeError("Matrix have to be a Matrix")
        self.matrix = matrix
            
    
    def __call__(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError("You can only apply with a Vector")
        return self.matrix * vector
    
    def compose(self, other):
        if not isinstance(other, ApplicationLineaire):
            raise TypeError("You can only compose with a Application Lineaire")
        return ApplicationLineaire(self.matrix * other.matrix)
    
    
        



if __name__ == "__main__":
    m = Matrix([[1, 2], [3, 4]])
    v = Vector([1, 2])
    
    app = ApplicationLineaire(m)

    print(app.apply(v))



