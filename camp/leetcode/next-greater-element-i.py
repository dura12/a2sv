class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        stack=[]
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                n = stack.pop()
                if n in nums1:
                    idx = nums1.index(n)
                    ans[idx] = nums2[i]

            stack.append(nums2[i])
        return ans    



        


        