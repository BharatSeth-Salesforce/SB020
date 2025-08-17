from Inharitance.Parent import Parent


class Child(Parent) :
    def getme(self):
        return "Hello I am From Child Class"

    def getmeFromChild(self):
        print("I am getmeFromChild ")