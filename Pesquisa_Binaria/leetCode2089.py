class Solution:
    def targetIndices(self, nums, target):
        list = []
        arr = sorted(nums)
        for index, valor in enumerate(arr):
            if valor == target:
                list.append(index)
        return list

target_indices = Solution()
arr = [1,2,5,2,3]

print(target_indices.targetIndices(arr, 5))
