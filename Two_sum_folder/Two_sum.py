class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j])  == target:
                    return[i, j]

        return[]

sum = Solution.twoSum("", [2, 7, 11, 15], 9)
# a = [2, 7, 11, 15]
# t = 9
# sum(a, t)
print(sum)