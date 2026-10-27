class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = Counter(hand)
        for c in d:
            if d[c]:
                start = c
                while d[start - 1]:
                    start -= 1
                for i in range(start, c+1):
                    amnt = d[i]
                    if d[i]:
                        for j in range(i, i + groupSize):
                            d[j] -= amnt
                            if d[j] < 0:
                                return False
        return True