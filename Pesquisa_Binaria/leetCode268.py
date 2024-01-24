class Solution:
    def missingNumber(self, nums1):
        nums1.sort()
        for index, num in enumerate(nums1):
            if(num != index):
                return index
        return len(nums1)
arr_input = Solution()
print(arr_input.missingNumber([9,6,4,2,3,5,7,0,1]))

