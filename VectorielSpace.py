from vector import Vector

class VectorielSpace : 

    def __init__(self, vectors):
        if len(vectors) == 0:
            raise ValueError("Base cannot be empty")
        dim = len(vectors[0])
        for v in vectors:
            if len(v) != dim:
                raise ValueError("All vector have to have the same lenght")
            if not isinstance(v,Vector):
                raise ValueError("Vector have to be a List of Vector")
        self.vectors = vectors 
        self.dimension = len(vectors)
    
    def __str__(self):
        result = "("
        for v in self.vectors : 
            result += str(v)
        result += ")"
        return result
    
    def dimension(self):
        return self.dimension
    
    


if __name__ == "__main__":

    v1 = Vector([1, 2, -58])
    v2 = Vector([3, -1, 4])

    space = VectorielSpace([v1,v2])
    print(space)