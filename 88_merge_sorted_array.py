from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers for each array.
        p1 = m-1
        p2 = n-1
        p = m + n - 1

        # Merge nums1 and nums2 in reverse order.
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them to nums1.
        nums1[: p2+1] = nums2[:p2 + 1]

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    res = Solution().merge(nums1, 3, nums2, 3)
    print(res)