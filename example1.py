class MyClass:
    variable ="blah"
    
    def addition(self,x,y):
        """
        testing:
        >>> c= MyClass()
        blah
        >>> print.(c.addition(3,4))
        4
        """
        return x+y
    def __init__(self):
        print(self.variable)

c= MyClass()
print(c.addition(3,4))

if __name__=="__main__":
    import doctest
    doctest.testmod()