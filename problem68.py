from itertools import permutations

class gonring:
    nodes = []

    def __init__(self, nodes):
        self.nodes = nodes
    
    def is_valid(self):
        total = self.__total1(0)
        for i in range(1, 5):
            if self.__total1(i) != total:
                return False
        return True
    
    def value(self):
        digits = self.nodes[:5]
        start = digits.index(min(digits))
        value = ""
        for i in range(5):
            value += str(self.nodes[(start+i)%5]) + str(self.nodes[(start+i)%5+5]) + str(self.nodes[(start+i+1)%5+5])
        return int(value)
    
    def __str__(self):
        outer_digits = self.nodes[:5]
        inner_digits = self.nodes[5:]
        start = outer_digits.index(min(outer_digits))
        outer_str = ""
        inner_str = ""
        for i in range(5):
            outer_str += str(outer_digits[(start+i)%5])
            inner_str += str(inner_digits[(start+i)%5+5])

        return f"{outer_str} {inner_str}"
        
    def __total1(self, start):
        total = self.nodes[start] + self.nodes[start+5] + self.nodes[(start+6)%5+5]
        return total
    
def get_permutations():
    nodes = [1,2,3,4,5,6,7,8,9,10]
    perms = permutations(nodes)
    for perm in perms:
        perm = list(perm)
        # print(perm)
        ring = gonring(perm)
        if ring.is_valid() and ring.value() < 10**16:
            yield ring

print(max([ring.value() for ring in get_permutations()]))
