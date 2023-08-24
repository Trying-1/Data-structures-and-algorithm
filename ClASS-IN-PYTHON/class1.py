class person:
    def __init__(self,name):
        self.name=name
    def introduce(self): # here we defined a method inside the class
        print(f"Hello, I am {self.name}")

person1=person("Ren")
person2=person("Trying")

person1.introduce()