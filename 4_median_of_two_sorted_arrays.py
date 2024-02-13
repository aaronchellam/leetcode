from typing import List
import statistics


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for simplicity.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            # Partition point in nums1.
            partitionX = (low + high) // 2

            # Corresponding partition point in nums2.
            partitionY = (y + x + 1) // 2 - partitionX

            # Values to the left and right of the partitions.
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if the partitions are in the correct place.
            if maxX <= minY and maxY <= minX:
                # Median found.

                # If the total length is even, return the average of max of left and min of right.
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2.0
                else:
                    # If the total length is odd, return the max of the left.
                    return float(max(maxX, maxY))

            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1

    # Naive. O((N + M) * Log (N + M)) due to sorting.
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)

        # If merged array is even.
        if n % 2 == 0:
            mid_left = (n // 2) - 1
            mid_right = mid_left + 1
            return (merged[mid_left] + merged[mid_right]) / 2

        # If the length of the array is odd.
        else:
            return merged[n // 2]

    # Efficient merging.
    def findMedianSortedArrays3(self, nums1: List[int], nums2: List[int]) -> float:
        # Handle edge case in which one of the arrays is empty.
        if len(nums1) == 0:
            return statistics.median(nums2)
        elif len(nums2) == 0:
            return statistics.median(nums1)

        # Array lengths.
        n = len(nums1)
        m = len(nums2)
        total = n + m

        is_odd = total % 2 == 1

        i, j = 0, 0

        # The candidate median number.
        candidate = None

        # Compute number of iterations required depending on whether the total number of elements is odd/even.
        iterations = (total // 2) + 1 if is_odd else total // 2

        # Find the halfway point across both lists by iterating in ascending order.
        for _ in range(iterations):
            if i < len(nums1) and (j >= len(nums2) or nums1[i] < nums2[j]):
                candidate = nums1[i]
                i += 1
            else:
                candidate = nums2[j]
                j += 1

        if is_odd:
            return candidate
        else:
            # If even number of numbers, find the next number to compute the median.
            if i < len(nums1) and j < len(nums2):
                next_num = min(nums1[i], nums2[j])
            elif i < len(nums1):
                next_num = nums1[i]
            else:
                next_num = nums2[j]

            return (candidate + next_num) / 2


if __name__ == '__main__':
    # nums1 = [1, 3, 5, 7, 9]
    # nums2 = []
    nums1 = [1]
    nums2 = [2, 3]
    sol = Solution().findMedianSortedArrays3(nums1, nums2)
    print(sol)
