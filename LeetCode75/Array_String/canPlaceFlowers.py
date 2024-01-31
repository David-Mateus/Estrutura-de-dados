class Solution:
    def canPlaceFlowers(self, flowerbed, n) :
        newBed = [0] + flowerbed + [0]
        for i in range(1, len(newBed)-1):
            if(newBed[i-1] == 0 and newBed[i] == 0 and  newBed[i+1] == 0):
                newBed[i]=1
                n -=1
            
        return n <= 0
                         

placeFlowers = Solution()
print(placeFlowers.canPlaceFlowers([1,0,0,1], 2))