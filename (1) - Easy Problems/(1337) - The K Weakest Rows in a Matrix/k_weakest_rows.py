from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
            The problem states you have to find the rows with the fewest
            number of 1s, sort them based on the count of 1s, and return
            the indices of said rows from 0 up to k.

            This can be done using a single list comprehension as seen
            below instead of two loops. In the list comprehension below
            we loop through each sublist in the matrix (the "rows"). At
            each iteration we save the index and count the 1s in the row.
            Both values are put in a single tuple which, after we have
            finished looping through all rows, sorts the tuples based on
            the amount of 1s (in this case, the second value of each tuple).
            The first value of each tuple is saved in the final list and
            at the end we use slicing to go from 0 up to k as specified in
            the problem description.
        """
        return [tup[0] for tup in sorted([(i, row.count(1)) for i, row in enumerate(mat)], key=lambda x: x[1])][:k]


# Test cases
sol = Solution()
assert sol.kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]], 3) == [2, 0, 3]
assert sol.kWeakestRows([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 4) == [0, 2, 3, 1]
