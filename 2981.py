from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        count = defaultdict(int)
        substringLength = 0

        for start in range(len(s)):
            character = s[start]
            substringLength = 0
            for end in range(start, len(s)):
                if character == s[end]:
                    substringLength += 1
                    count[(character, substringLength)] += 1
                else:
                    break

        ans = 0
        for (char, length), freq in count.items():
            if freq >= 3 and length > ans:
                ans = length

        if ans == 0:
            return -1
        return ans


solution = Solution()
s = "aaabb"
result = solution.maximumLength(s)
print(
    f"The maximum length of a substring that appears at least three times is: {result}"
)
