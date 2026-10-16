class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = Counter(hand)
        for anchor in hand:
            start = anchor
            while d[start - 1]:
                start -= 1
            for i in range(start, anchor + 1):
                num_starting = d[i]
                if num_starting > 0:
                    for j in range(groupSize):
                        d[i + j] -= num_starting
                        if d[i + j] < 0:
                            return False 
        return True
        
            