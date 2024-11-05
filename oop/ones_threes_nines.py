class OnesThreesNines:
    def __init__(self, number):
        self.ones = number // 1
        self.threes = number // 3
        self.nines = number // 9


n1 = OnesThreesNines(5)
print(n1.nines)
print(n1.ones)
print(n1.threes)
