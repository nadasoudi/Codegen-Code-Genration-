class MyList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__data = []
    
    def __getitem__(self, index):
        return self.__data[index]
    
    def __setitem__(self, index, value):
        self.__data[index] = value
    
    def __delitem__(self, index):
        del self.__data[index