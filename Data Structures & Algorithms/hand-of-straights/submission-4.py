class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        for n in hand:
            start = n
            while count[start - 1]:
                start -= 1
            while start <= n:
                while count[start]:
                    for i in range(groupSize):
                        if not count[start + i]:
                            return False
                        count[start + i] -= 1
                start += 1
        return True