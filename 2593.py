class Solution:
    def findScore(self, nums: list[int]) -> int:
        ans = 0
        seen = set()

        for key, value in sorted([(num, i) for i, num in enumerate(nums)]):
            if value in seen:
                continue
            seen.add(value - 1)
            seen.add(value + 1)
            seen.add(value)
            ans += key

        return ans


# Create an instance of the Solution class
solution = Solution()

# Define the input array
nums = [2, 3, 2]

# Call the findScore method and print the result
score = solution.findScore(nums)
print(f"The maximum score is: {score}")
