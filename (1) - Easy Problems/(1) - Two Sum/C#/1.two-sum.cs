/*
 * @lc app=leetcode id=1 lang=csharp
 *
 * [1] Two Sum
 */

// @lc code=start
public class Solution {
    public int[] TwoSum(int[] nums, int target)
        {
            Dictionary<int, int> intStore = new Dictionary<int, int>();
            for (int i = 0; i < nums.Length; i++)
            {
                if (intStore.ContainsKey(target - nums[i]))
                {
                    return new int[] { intStore[target - nums[i]], i };
                }
                else
                {
                    intStore[nums[i]] = i;
                }
            }

            return new int[2];
        }
}
