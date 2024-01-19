class Solution:
    def countPairs(self, nums, target):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                soma = nums[i] + nums[j]
                if soma < target:
                    count +=1
        return count

nums = Solution()
print(nums.countPairs([-1,1,2,3,1], 2))