class Stack():
    
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0
        
    def push(self,item):
        self.stack_size += 1
        self.stack_list.append(item)
        
    def peak(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]
        
    def is_empty(self):
        return self.stack_size == []
    
    def pop(self):
        if self.stock_size == 0:
            return None
        self.stack_size -= 1
        return self.stack_list.pop()
    
    def get_content(self):
        return self.stack_list
        
