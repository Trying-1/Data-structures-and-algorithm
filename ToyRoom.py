#first, we need a special room for each toy animal
class ToyRoom:
    def __init__(self,number):
        self.toy_number=number
        self.left_toy=None  #this is left door to another room
        self.right_toy=None #this is right door to another room

# Now, lets make out toy tree
class ToyTree:
    def __init__(self, king_toy_number):
        self.king_toy = ToyRoom(king_toy_number)  # the king toy sits on the top

    # when we want to add a new toy, we decide where it goes
    def add_toy(self, number):
        self._add_toy_recursive(self.king_toy, number)

    # this is like a magical helper that helps us to decide where the new toy goes
    def _add_toy_recursive(self, current_toy, number):
        if number < current_toy.toy_number:
            if current_toy.left_toy is None:
                current_toy.left_toy = ToyRoom(number)
            else:
                self._add_toy_recursive(current_toy.left_toy, number)
        else:
            if current_toy.right_toy is None:
                current_toy.right_toy = ToyRoom(number)
            else:
                self._add_toy_recursive(current_toy.right_toy, number)
    
    #lets paly a game : we'll ask if a toy is in our tree
    def find_toy(self, number):
        return self._find_toy_recursive(self.king_toy,number)
    
    #another magical helper that helps us find the toy
    def _find_toy_recursive(self,current_toy,number):
        if current_toy is None:
            return False
        if current_toy.toy_number == number:
            return True
        elif number< current_toy.toy_number:
            return self._find_toy_recursive(current_toy.left_toy,number)
        else:
            return self._find_toy_recursive(current_toy.right_toy,number)
        
# lets create out toy tree and play the game
toy_tree=ToyTree(10) # our king toy has number 10
    
# add more toy animals to the tree
toy_tree.add_toy(5)
toy_tree.add_toy(15)
toy_tree.add_toy(3)

    
#lets play the game 
print(toy_tree.find_toy(7)) # can you find the toy with number7?
    
print(toy_tree.find_toy(12))
