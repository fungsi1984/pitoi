from typing import List


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the value-index pairs
        hashmap = {}

        # Iterate through the list of numbers
        for key, value in enumerate(nums):
            # Calculate the complement that would add up to the target
            result = target - value

            # Check if the complement is already in the dictionary
            if result in hashmap:
                # If found, return the indices of the two numbers
                return sorted([hashmap[result], key])

            # Otherwise, add the current value and its index to the dictionary
            hashmap[value] = key

        # If no solution is found, return an empty list (though the problem guarantees a solution)
        return []


# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]
