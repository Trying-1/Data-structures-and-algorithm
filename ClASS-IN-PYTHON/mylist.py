class node:
    def __init__(self,data):
        self.value=data
        self.next= None
        
class List:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=newNode
        
    def displayList(self):
        n=self.head
        while  n is not None:
            print(n.value)
            n=n.next
        
mylist=List()
mylist.append(5)
mylist.append(9)
mylist.append(10)
mylist.displayList()
