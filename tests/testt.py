class Example:
    def __init__(self, name):
        self.name = name


object1 = Example("Check")
object2 = Example("Whatever")
liststr = {"Checkkey": object1, "whateverkey": object2}

print(liststr)
liststr.pop("Checkkey")
print(liststr)
