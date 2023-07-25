class stack:
    def __init__(self, *iterable) -> None:
        iterable = list(iterable)
        for item in iterable:
            self.__checkDtype(item)
        self.__iterable = iterable
    
    def push(self, item):
        self.__checkDtype(item)
        self.__iterable.append(item)
    
    def pop(self):
        return self.__iterable.pop() if not self.isEmpty() else None
    
    def peek(self):
        return self.__iterable[-1] if not self.isEmpty() else None
    
    def __checkDtype(self, item):
        if len(self.__iterable)>0 and type(item) != type(self.__iterable[0]):
            raise TypeError("All items in the stack must be of the same data type, mumu")
    
    def isEmpty(self):
        return len(self.__iterable)==0

a = stack(1)