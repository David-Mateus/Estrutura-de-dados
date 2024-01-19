class Solution:
    def countNegatives(grid):
        sum = 0;
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    sum += 1
        return sum

arr = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,- 3]]

arr.sort()
find_target = Solution()
print(find_target.countNegatives(arr))

