try:
    from .vector import Vector
except ImportError:
    from vector import Vector


class VectorielSpace:
    """Represents a vector space defined by a basis."""
    
    def __init__(self, vectors):
        """Initialize a vector space with a basis."""
        if len(vectors) == 0:
            raise ValueError("Base cannot be empty")
        
        dim = len(vectors[0])
        for v in vectors:
            if len(v) != dim:
                raise ValueError("All vectors have to have the same length")
            if not isinstance(v, Vector):
                raise ValueError("Vector have to be a List of Vector")
        
        self.vectors = vectors 
        self.dim = len(vectors)
        self.ambient_dimension = dim
    
    def __str__(self):
        result = "Vectorial Space with basis:\n("
        for i, v in enumerate(self.vectors):
            result += str(v)
            if i < len(self.vectors) - 1:
                result += ",\n "
        result += ")\n"
        return result
    
    def dimension(self):
        """Return the dimension of this vector space."""
        return self.dim
    
    def ambient_dim(self):
        """Return the dimension of the ambient space."""
        return self.ambient_dimension
    
    def get_basis_vector(self, index):
        """Get the basis vector at given index."""
        if index < 0 or index >= len(self.vectors):
            raise IndexError("Index out of range")
        return self.vectors[index]
    
    def get_basis(self):
        """Return the list of basis vectors."""
        return self.vectors


if __name__ == "__main__":
    print("=" * 60)
    print("TESTS: Vector Space")
    print("=" * 60)

    # Test 1: Basic vector space
    print("\nTest 1: Basic 2D vector space")
    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    space1 = VectorielSpace([v1, v2])
    print(space1)
    print("Dimension:", space1.dimension())
    print("Ambient dimension:", space1.ambient_dim())

    # Test 2: 3D vector space
    print("\nTest 2: 3D vector space")
    v3 = Vector([1, 0, 0])
    v4 = Vector([0, 1, 0])
    v5 = Vector([0, 0, 1])
    space2 = VectorielSpace([v3, v4, v5])
    print(space2)
    print("Dimension:", space2.dimension())

    # Test 3: Basis vector access
    print("\nTest 3: Basis vector access")
    print("First basis vector:", space1.get_basis_vector(0))
    print("Basis:", space1.get_basis())


    # Test 7: Error cases
    print("\nTest 7: Error handling")
    try:
        print("Testing error: empty vector space")
        VectorielSpace([])
    except ValueError as e:
        print("✓ Caught:", e)

    try:
        print("Testing error: vectors of different lengths")
        VectorielSpace([Vector([1, 2]), Vector([3, 4, 5])])
    except ValueError as e:
        print("✓ Caught:", e)

    try:
        print("Testing error: invalid index")
        space1.get_basis_vector(10)
    except IndexError as e:
        print("✓ Caught:", e)

    print("\n" + "=" * 60)
    print("Tests completed successfully")
    print("=" * 60)