class ProtectedExample:
    def __init__(self):
        self._protectedVar = 0

obj = ProtectedExample()
obj._protectedVar = 25
print(obj._protectedVar)
        
class Protected2:
    def __init__(self):
        self._privateEx = 25

    def getPrivate1(self):
        print(self._privateEx)

    def setPrivate1(self, private):
        self._privateEx = private

obj = Protected2()
obj.getPrivate1()
obj.setPrivate1(100)
obj.getPrivate1()
