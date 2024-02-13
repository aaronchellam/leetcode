from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        count = 1
        array_pointer = 1
        insert_pointer = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1

                if count <= 2:
                    nums[insert_pointer] = nums[i]
                    insert_pointer += 1

            elif nums[i] != nums[i-1]:
                count = 1
                nums[insert_pointer] = nums[i]
                insert_pointer += 1




        print(nums)
        return insert_pointer


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    res = Solution().removeDuplicates(nums)
    print(res)
