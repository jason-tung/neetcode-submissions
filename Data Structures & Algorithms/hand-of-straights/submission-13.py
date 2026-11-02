class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = Counter(hand)
        for k in d:
            if d[k]:
                start = k
                while d[start - 1]:
                    start -=1
                for i in range(start, k + 1):
                    if d[i]:
                        amnt = d[i]
                        for j in range(i, i+groupSize):
                            d[j] -= amnt
                            if d[j] < 0:
                                return False
        return True