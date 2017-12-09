import math

# Implementation is written assuming Python 3.6.1

TWO_BASE = 2
ONE_MASK = 0x1

class Proto_Van_Emde:

    def  __init__(self, universe):
        k = math.log(universe, TWO_BASE) / 2
        integer_k = math.floor(k)
        assert(k == integer_k)

        self.k = integer_k
        self.universe = universe
        self.sqrt_universe = math.floor(math.sqrt(self.universe))
        self.low_mask = (ONE_MASK << self.k) - 1
        self.high_mask = self.low_mask << self.k

    def high(self, x):
        assert(math.floor(x / math.sqrt(self.universe)) == (x & self.high_mask) >> self.k)
        return (x & self.high_mask) >> self.k

    def low(self, x):
        assert(math.floor(x % math.sqrt(self.universe)) == x & self.low_mask)
        return x & self.low_mask

    def index(self, s_index, c_index):
        return s_index * self.sqrt_universe + c_index

p_ve = Proto_Van_Emde(64)
for i in range(64):
    s_index = p_ve.high(i)
    c_index = p_ve.low(i)
    sert(i == p_ve.index(s_index, c_index))


# 2^(2k) = 64. k = 3. sqrt(64) = 8.
