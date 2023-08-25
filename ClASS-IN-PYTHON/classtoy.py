class ToyRoom:
    def __init__(self,toy):
        self.left=None
        self.toy=toy
        self.right=None

Toys=ToyRoom("Cars")
print(Toys.toy)