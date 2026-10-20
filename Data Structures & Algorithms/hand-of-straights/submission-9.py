class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = Counter(hand)
        for n in d:
            if d[n]:
                start = n
                while d[start - 1]:
                    start -= 1
                for i in range(start, n + 1):
                    if d[i]:
                        size_start = d[i]
                        for j in range(i, i + groupSize):
                            d[j] -= size_start
                            if d[j] < 0:
                                return False
        return True