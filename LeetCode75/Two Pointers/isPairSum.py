def isTroca(nums):
    l=0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[r], nums[l] = nums[l], nums[r]
            l+=1
    return nums

meu_array = [0,1,0,3,12]
# print(isTroca(meu_array))
