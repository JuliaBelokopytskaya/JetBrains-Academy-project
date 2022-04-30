class FibonacciGenerator:
    def __init__(self, limit):
        self.prev = 0 
        self.cur = 1
        self.limit = limit
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.limit:
            result = self.prev
            self.prev, self.cur =self.cur, self.prev + self.cur
            self.i += 1
            return result
        else:
            raise StopIteration
for i in FibonacciGenerator(15):
    print(i)

def fibonacciGenerator(limit):
    prev = 0
    cur = 1
    count = 0
    while count < limit:
        result = prev
        prev, cur = cur, prev+cur
        count += 1
        yield result

for item in fibonacciGenerator(15):
    print(item)