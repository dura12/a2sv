class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        lis = 0
        s = [a - b for a , b in zip(nums1 , nums2)]
        def merge_sort(left , right , arr):
            nonlocal lis
            if left >= right:
                return [arr[left]]
            mid = left + (right - left)//2
            left_half = merge_sort(left , mid , arr)
            right_half = merge_sort(mid + 1 , right , arr)
            i = 0 
            j = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] - right_half[j] <= diff:
                    lis += len(right_half) - j
                    i += 1
                else:
                    j += 1

            return merge(left_half , right_half)
        def merge(left_half, right_half):
            left_index = 0
            right_index = 0
            sorted_subarray = []
            while left_index < len(left_half) and right_index < len(right_half):
                if left_half[left_index] < right_half[right_index]:
                    sorted_subarray.append(left_half[left_index])
                    left_index += 1
                else:
                    sorted_subarray.append(right_half[right_index])
                    right_index += 1
            sorted_subarray.extend(left_half[left_index:])
            sorted_subarray.extend(right_half[right_index:])
            return sorted_subarray
        (merge_sort( 0 , len(s)-1 , s))
        return lis