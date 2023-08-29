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
    def countList(self):
        n=self.head
        count=0
        while n is not None:
            n=n.next
            count+=1
        print(f"number of element in the lis:{count}")
    def searchInList(self,data):
        n=self.head
        found = False
        while n is not None:
            if(n.value==data):
                found=True
                break
            else:
                n=n.next
        if found:
            print(f" {data} the was found in the list")
            return True
        else:
            print(f" {data} the was  not found in the list")
            return False
    def deleteNode(self,data):
        if self.searchInList(data):
            n=self.head
            if n.value==data:
                self.head=n.next
                return
            else:
                while n.value is not data:
                    prevNode= n
                    n=n.next
                nextNode=n.next
                prevNode.next=nextNode   
        else:
            print("data not found to delete")
    
                          
mylist=List()
mylist.append(5)
mylist.append(9)
mylist.append(10)

