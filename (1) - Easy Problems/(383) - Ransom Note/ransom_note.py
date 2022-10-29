from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
            Counter from collections is a dictionary subclass
            for counting occurences of something in hashable items.

            E.g. for ransomNote = 'aa' and magazine = 'aab' we have:

                        Counter({'a': 2})
                        Counter({'a': 2, 'b': 1})

            Substracting the second Counter object from the first gives
            will tell you whether all of the first string is contained
            within the second. We have to return a boolean value in this
            problem, so to achieve that we add 'not' in front of the
            subtraction.

            The reason this works is because 'not' takes a value, converts
            it to a boolean, and then inverts it. Like this:

                        print(not True) = False
                        print(not False) = True
                        print(not []) = True
                        print(not [1,2,3]) = False
        """
        return not Counter(ransomNote) - Counter(magazine)


sol = Solution()
print(sol.canConstruct('a', 'b'))
print(sol.canConstruct('aa', 'ab'))
print(sol.canConstruct('aa', 'aab'))
print(sol.canConstruct('aab', 'baa'))
print(sol.canConstruct('bg', 'efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj'))
