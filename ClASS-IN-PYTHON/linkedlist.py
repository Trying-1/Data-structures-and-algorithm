#creating the node class, which will be the container  like for the list. node will contain two things data and the reference to the next node
class node:
    def __init__(self,data): # the self is the whole node container which has two partitions for data and next
        self.data=data
        self.next=None

class linkedList: # here we create a list class means all the collections of node. well structured from head, 
    def __init__(self): # self is the list instance, like we can create many list use this and self represent them
        self.head=None  # head of list is set to None in the begining
        
    def append(self,data):   # the function for appending or adding data in the list
        newNode=node(data)  # creating a new node instance that will contain the data,
        if not self.head:  # check if the list already contain head
            self.head=newNode # if not then the new node we just created will be head node
        else: # or else 
            current=self.head # but if there exist a head then we will get that head using self.head, and assign it to new variable current
            while(current.next): # now iterating throug the list till the next is None of the node,where we can add newnode
                current=current.next #
            current.next=newNode # after we reach the end we add newNode to the next partition of current node

# to display the list we define new method display      
    def display(self): # self here is still representing the list as it is inside the class Linkedlist
        current=self.head # intializing the from where we want to iterate
        while(current): # here we iterate till the last node, means till the end of list.
            print(current.data) # printing or say displaying the data of node
            current=current.next # again going to next node
    def countNode(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.next
        print(f"the length of the list is : {count}")
        
        
        
            

list=linkedList()
list.append(5)
list.append(7)
list.append(8)
list.display()
list.countNode()
