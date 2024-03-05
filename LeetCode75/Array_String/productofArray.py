

def productExceptSelf(nums) :
        pre = 1
        pro = 1
        result = [0]*4
        for i in range(len(nums)):
                result[i] = pre
                pre *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            result[i] *= pro
            pro *= nums[i] 
        print(result)
                
             
productExceptSelf([-1,1,0,-3,3])

