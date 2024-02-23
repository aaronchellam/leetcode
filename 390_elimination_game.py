class Solution:
    def lastRemaining2(self, n):
        return self.helper(n, True)

    def helper(self, n: int, left_to_right:bool):
        if n == 1:
            return 1

        # If it's a left-to-right pass.
        if left_to_right:
            # After the left-to-right pass, the size of the remaining list is halved.
            return 2 * self.helper(n//2, False)
        else:
            return 2 * self.helper(n // 2, True) - ((n-1) % 2)



    def lastRemaining(self, n: int) -> int:




        arr = list(range(1, n+1))


        def lastRemainingRecursive(array, sign):
            if len(array) == 1:
                return array
            print("\nDeleting half the elements")
            print(f"Array before: {array}")
            print(f"Deleted Elements: {array[:: sign*2]}")
            del array[:: sign*2]

            print(f"Array {array}")
            sign = sign * -1
            return lastRemainingRecursive(array, sign)

        final_array = lastRemainingRecursive(arr, 1)
        return final_array[0]

if __name__ == '__main__':
    n = 4
    sol = Solution().lastRemaining2(n)
    print(sol)