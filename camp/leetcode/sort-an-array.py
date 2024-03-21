class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(left , right , num):
            if left == right:
                return [num[left]]
            mid = left + (right - left)//2
            left_h = merge_sort(left , mid, num)
            right_h = merge_sort(mid+1, right , num)
            return merge(left_h , right_h)
        def merge(left_half , right_half):
            l = 0
            r = 0
            sorted_array = []
            while l < len(left_half) and r < len(right_half):
                if left_half[l] < right_half[r]:
                    sorted_array.append(left_half[l])
                    l += 1
                else:
                    sorted_array.append(right_half[r])
                    r += 1
            sorted_array.extend(left_half[l:])
            sorted_array.extend(right_half[r:])
            return sorted_array
        return merge_sort(0 , len(nums)-1 , nums)



