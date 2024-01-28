class Solution:
    def kidsWithCandies(self, candies, extraCandies ):
        list = []
        lenght = len(candies)
        maximum = max(candies)
        
        
        for i in range(lenght):
           sumValue = (candies[i] + extraCandies)
           if(sumValue < maximum):
               list.append(False)
           else:
               list.append(True)
        return list
           
           
        
        
        
candies = Solution()
print(candies.kidsWithCandies([2,3,5,1,3], 3))

    
        