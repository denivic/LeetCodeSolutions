class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
            Take this list as an example where each element after
            the first is the next step towards 0:

                [31, 30, 15, 14, 7, 6, 3, 2, 0]

            The bit representation for each element is as follows:

                    001 | 00011111
                    002 | 00011110
                    003 | 00001111
                    004 | 00001110
                    005 | 00000111
                    006 | 00000110
                    007 | 00000011
                    008 | 00000010
                    009 | 00000000

            The pattern here is:                   i: 001      i: 002
            Step 1: Flip the rightmost bit to 0. (00011111 -> 00011110)        i: 003
            Step 2: Shift everything to the right and pad the left with a 0. (00001111)
            Step 3: Repeat until you reach 0.

            This process can be done instantly as is done below.
            31 in binary is 00011111 (see 001) above. So:

            Bit length: 5 (length as in how many bits)
            Bit count: 5 (how many 1s or 'active bits' there are)
            Steps = (5 - 1) + 5 = 4 + 5 = 9

            Which is equivalent to the length of the list.
        """
        print(f'Bit length: {num.bit_length()}, Bit count: {num.bit_count()}, Bit representation: {bin(num)}, Steps: {num.bit_length() - 1 + num.bit_count()}')
        return 0 if num == 0 else num.bit_length() - 1 + num.bit_count()


sol = Solution()
assert sol.numberOfSteps(31) == 9
assert sol.numberOfSteps(14) == 6
assert sol.numberOfSteps(8) == 4
assert sol.numberOfSteps(123) == 12
