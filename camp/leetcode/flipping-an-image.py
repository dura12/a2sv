from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(image)):
            temp = []
            for j in range(len(image[0])):
                if image[i][j] == 1:
                    temp.append(0)
                else:
                    temp.append(1)
            temp.reverse()
            res.append(temp)
        return res