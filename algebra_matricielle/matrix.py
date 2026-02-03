class Matrix :

    def __init__(self, n, p):
        if isinstance(n, int) and isinstance(p, int):
            self.n = n
            self.p = p
            self.matrice = [[None for _ in range(p)] for _ in range(n)]
        else:
            raise TypeError("n et p doivent être des entiers")
        
    def __add__(self, other):
        pass

    def __sub__(self,other):
        pass

    def __mul__(sel,other):
        pass

    
        