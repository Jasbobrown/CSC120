class Counter:
    def __init__(self):
        self._count = 0
    def click(self):
        self._count += 1 
    def count(self):
        return self._count 
    
x, y, z = Counter(), Counter(), Counter()
x.click()
y.click()
y.click()
z.click()
z.click()
z.click()
print(x.count(), y.count(), z.count())