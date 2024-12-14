from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}

        length = len(nums)

        for i in range(length):
            complement = target - nums[i]

            if complement in map_dict:
                return sorted([i, map_dict[complement]])

            map_dict[nums[i]] = i

        return []


# Create an instance of the Solution class
solution = Solution()

# Define a list of numbers and a target sum
nums = [2, 7, 11, 15]
target = 9

# Call the twoSum method
result = solution.twoSum(nums, target)

# Print the result
print(result)
