class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert to string, reverse, and finally check against x
        return True if str(x)[::-1] == str(x) else False


sol = Solution()
assert sol.isPalindrome(121) is True    # True
assert sol.isPalindrome(10) is False    # False
assert sol.isPalindrome(-121) is False  # False
