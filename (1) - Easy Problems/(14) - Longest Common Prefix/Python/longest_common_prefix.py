from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            zip(*strs) unpacks each word in the list
            and then zips each letter e.g.

            *strs = ['flower', 'flow', 'flight'] = flower flow flight
            zip(*strs) = ('f', 'f', 'f') <- 1st iteration
                       = ('l', 'l', 'l') <- 2nd iteration
                       = ('o', 'o', 'i') <- 3rd iteration
                       = ('w', 'w', 'g') <- 4th iteration

            It stops at the 4th iteration because that's
            the length of the shortest word: flow.

            For each iteration convert the tuple into a set.
            A set can *not* have duplicates in it, which means that
            if the length of a set is bigger than 1 then there
            is more than 1 item in the set i.e. the longest
            common prefix ends at that point. In order to get
            the index at that point, we use enumerate() while
            looping. In the example above the sets would be:

            1st iteration: set of ('f', 'f', 'f') = {'f'}       | len = 1, i = 0
            2nd iteration: set of ('l', 'l', 'l') = {'l'}       | len = 1, i = 1
            3rd iteration: set of ('o', 'o', 'i') = {'o', 'i'}  | len = 2, i = 2

            which means the longest common prefix is everything
            in the first word up until char at index i = 2. In
            other words: strs[0][:i]

            If the condition never holds then return the smallest
            string in the list as this is the only choice left.
        """
        for i, letters in enumerate(zip(*strs)):
            if len(set(letters)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


# Test cases
sol = Solution()
assert sol.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
assert sol.longestCommonPrefix(['dog', 'racecar', 'car']) == ''
