class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        sorted_hand = sorted(hand)
        d = Counter(hand)
        for k in sorted_hand:
            if d[k] == 0:
                continue
            for i in range(groupSize):
                j = k + i
                d[j] -= 1
                if d[j] < 0:
                    return False
        return True