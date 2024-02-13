from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialise a variable to keep track of unique elements.
        unique_count = 1

        # Iterate through list, starting from second element.
        for i in range(1, len(nums)):
            # If the current element is not equal to the previous element, it's a unique element
            if nums[i] != nums[i - 1]:
                # Move the unique element to the appropriate position in the list.
                nums[unique_count] = nums[i]
                unique_count += 1

        print(nums)
        return unique_count

if __name__ == '__main__':
    sol = Solution()
    input = [0,0,1,1,1,2,2,3,3,4]
    input = [1, 1, 2]
    print(sol.removeDuplicates(input))