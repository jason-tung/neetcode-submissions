SWAP_STEPS = (
    (16, 0x0000FFFF),
    (8,  0x00FF00FF),
    (4,  0x0F0F0F0F),
    (2,  0x33333333),
    (1,  0x55555555),
)
class Solution:
    def reverseBits(self, n: int) -> int:
        for bits, lowmask in SWAP_STEPS:
            n = ((n & ~lowmask) >> bits) | ((n & lowmask) << bits)
        return n