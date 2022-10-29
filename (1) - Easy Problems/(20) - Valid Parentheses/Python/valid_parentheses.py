class Solution:
    def isValid(self, s: str) -> bool:
        """
            If we don't have an even number of characters in the string
            then we know that the string is not valid and we return False.
            Likewise if it's empty then it is obviously not valid either
            as there are no brackets so once again we return False.
        """
        if len(s) % 2 != 0 or s == '':
            return False
        else:
            # Dict lookup is O(1) and also makes it easy to compare pairs.
            brackets = {'(': ')',
                        '[': ']',
                        '{': '}'}

            """
                Stack structures follow the LIFO principle (Last in, First out)
                and this makes it useful for finding valid opening and ending
                brackets. Say we have the string '([])' and we are looping through
                each character in said string. For each *opening* bracket we
                push (append) to the stack. If we encounter a a closing bracket
                then we pop (remove) the character at the top of the stack. It
                often helps to think of the stack structure as a list that has been
                rotated 90 degrees to the left such that it now is a vertical "list".

                For example, with the string given above, the list would look like:
                                    ['(', '[']
                                      ↑    ↑
                                  i:  0    1

                This is essentially our stack. When rotated 90 degreees to the left:
                                  i:
                                  1 -> ['[']
                                  0 -> ['(']

                So as mentioned previously, for each iteration add opening bracket
                and for each closing bracket pop the top item in the stack. If at
                any point the popped bracket doesn't match the current bracket we
                return False. So for each iteration:

                1st Iteration
                -------------
                string index        = 0
                string at index     = '('
                bracket_stack       = ['(']
                bracket             = ''      (Empty since we didn't pop anything)
                pop top item        = False

                2nd Iteration
                -------------
                string index        = 1
                string at index     = '['
                bracket_stack       = ['(', '[']
                bracket             = ''    (Empty since we didn't pop anything)
                pop top item        = False

                3rd Iteration
                -------------
                string index            = 2
                string at index         = ']'
                bracket_stack           = ['(', '[']
                bracket                 = '[' (First time encountering closing bracket. Has this value because bracket == bracket_stack[-1])
                bracket_stack after pop = ['(']

                4th Iteration
                -------------
                string index            = 4
                string at index         = ')'
                bracket_stack           = ['(']
                bracket                 = '('
                pop top item            = True (Same as above, but with ')')
                bracket_stack after pop = []

                Now that we have reached the end of the string, we can confirm that
                there are no missing brackets by checking whether the stack is
                empty. If it is not empty then there is an unmatched bracket, which
                means False is returned since the string is not valid - otherwise True.
            """
            bracket_stack = []

            for char in s:
                if char in brackets.keys():
                    bracket_stack.append(char)
                else:
                    if len(bracket_stack) == 0:
                        return False

                    bracket = bracket_stack.pop()

                    if char != brackets[bracket]:
                        return False

            return bracket_stack == []


# Test cases
sol = Solution()
assert sol.isValid('()') is True
assert sol.isValid('') is False
assert sol.isValid('))') is False
assert sol.isValid('([}}])') is False
assert sol.isValid('([}]}])') is False
assert sol.isValid('){') is False
assert sol.isValid('()[]{}') is True
assert sol.isValid('(]') is False
