class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        last_empty = -2
        for i in range(len(flowerbed) + 2):
            if i < len(flowerbed) and flowerbed[i] or i == len(flowerbed) + 1:
                n -= (i - last_empty - 2)//2 
                last_empty = i
        return n <= 0
