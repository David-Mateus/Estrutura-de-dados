class Solution:
    def kWeakestRowns(self, list, k):
        arr = []
        countSold = 0
        countCivis = 0
        for sold in list:
            for civis in sold:
                if civis== 0:
                    countCivis+=1
                else:
                    countSold+=1
        print(countSold, countCivis)
        #NÃO CONSEGUIR FAZER. ESTUDAR MAIS!
                


arr_input = Solution()
arr_input.kWeakestRowns([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3)