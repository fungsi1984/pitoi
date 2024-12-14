from typing import List, Optional


class HashTableEntry:
    def __init__(self, key: int, value: int, next: Optional[int] = None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, size: int):
        self.buckets = [None] * size
        self.entries = []
        self.size = size
        self.entry_count = 0

    def custom_hash(self, key: int) -> int:
        return abs(key) % self.size

    def insert(self, key: int, value: int):
        index = self.custom_hash(key)
        entry_index = self.buckets[index]

        while entry_index is not None:
            if self.entries[entry_index].key == key:
                self.entries[entry_index].value = value
                return
            entry_index = self.entries[entry_index].next

        new_entry_index = self.entry_count
        self.entries.append(HashTableEntry(key, value, self.buckets[index]))
        self.buckets[index] = new_entry_index
        self.entry_count += 1

    def search(self, key: int) -> Optional[int]:
        index = self.custom_hash(key)
        entry_index = self.buckets[index]

        while entry_index is not None:
            if self.entries[entry_index].key == key:
                return self.entries[entry_index].value
            entry_index = self.entries[entry_index].next

        return None


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        ht = HashTable(size * 2)

        for i, num in enumerate(nums):
            complement = target - num
            found_index = ht.search(complement)
            if found_index is not None:
                return [found_index, i]
            ht.insert(num, i)

        return []


nums = [0, 4, 3, 0]
target = 0

solution = Solution()
indices = solution.twoSum(nums, target)

if indices:
    print(f"Indices: {indices[0]}, {indices[1]}")
else:
    print("No solution found.")
