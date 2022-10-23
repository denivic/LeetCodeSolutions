from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionaries allow lookup in O(n) because they are
        # implemented using hash tables.
        values = {}

        for i, value in enumerate(nums):
            # Make use of the fact that target - value equals
            # the value you're looking for.
            if target - value in values:
                return [values[target - value], i]
            else:
                # When said value is not found, add it to
                # the dictionary so you can check next iteration.
                values[value] = i


solution = Solution()
