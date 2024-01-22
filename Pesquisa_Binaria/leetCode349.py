class Solution:
    def intersection(self, nums1, nums2):
        output = []
        for i in nums1:
            for j in nums2:
                if i == j and i not in output:
                    output.append(i)
                    break
        return output
arr_input = Solution()
print(arr_input.intersection([4,9,5],
[9,4,9,8,4]))

#Neste código, eu substituí for i in nums1 por for valor in nums1 para iterar diretamente sobre os valores. Além disso, adicionei uma condição and valor not in output para garantir que cada valor seja adicionado apenas uma vez à lista output. O break é usado para sair do loop interno assim que um valor correspondente for encontrado na segunda lista.