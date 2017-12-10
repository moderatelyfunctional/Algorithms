import math

# Implementation is written assuming Python 3.6.1

TWO_BASE = 2
ONE_MASK = 0x1

class Proto_Van_Emde:

    def  __init__(self, universe):
        self.u = universe
        self.elts = [0 for _ in range(universe)]

        if self.u == 2:
            return

        u_bits = math.floor(math.log(universe, TWO_BASE))
        k = math.log(u_bits, TWO_BASE)
        integer_k = math.floor(k)
        assert(k == integer_k)

        self.sqrt_u = math.floor(math.sqrt(self.u))
        self.u_bits = math.floor(u_bits / 2)
        self.low_mask = (ONE_MASK << self.u_bits) - 1
        self.high_mask = self.low_mask << self.u_bits

        self.summary = Proto_Van_Emde(self.sqrt_u)
        self.cluster = [Proto_Van_Emde(self.sqrt_u) for _ in range(self.sqrt_u)]

    def high(self, x):
        # assert(math.floor(x / self.sqrt_u) == (x & self.high_mask) >> self.u_bits)
        return (x & self.high_mask) >> self.u_bits

    def low(self, x):
        # assert(math.floor(x % self.sqrt_u) == x & self.low_mask)
        return x & self.low_mask

    def index(self, s_index, c_index):
        return s_index * self.sqrt_u + c_index

    def member(self, x):
        if self.u == 2:
            return self.elts[x]
        return self.cluster[self.high(x)].member(self.low(x))

    def insert(self, x):
        if self.u == 2:
            self.elts[x] = 1
        else:
            self.summary.insert(self.high(x))
            self.cluster[self.high(x)].insert(self.low(x))

    def __min_max_helper(self, find_min=True):
        if self.u == 2:
            first_elt = 0 if find_min else 1
            second_elt = 1 if find_min else 0
            if self.elts[first_elt]:
                return first_elt
            if self.elts[second_elt]:
                return second_elt
            return None
        c_index = self.summary.__min_max_helper(find_min)
        if c_index == None:
            return None
        offset = self.cluster[c_index].__min_max_helper(find_min)
        return self.index(c_index, offset)

    def minimum(self):
        return self.__min_max_helper(True)

    def maximum(self):
        return self.__min_max_helper(False)

p_ve = Proto_Van_Emde(16)

#for i in range(16):
#    s_index = p_ve.high(i)
#    c_index = p_ve.low(i)
#    assert(i == p_ve.index(s_index, c_index))

p_ve.insert(10)
p_ve.insert(15)
print(p_ve.member(8))
print(p_ve.minimum())
print(p_ve.maximum())

