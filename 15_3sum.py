from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = []

        # Consider all i from 0 to n-2 as candidates for the first number.
        for i in range(n - 2):

            # Skip duplicate candidates for i.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find two other values for the triple.
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # If total too small, increment left to increase total.
                if total < 0:
                    left += 1

                # If total too big, decrement right to decrease total.
                elif total > 0:
                    right -= 1

                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left = + 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets
