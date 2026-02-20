# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Example:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.


nums = [0,0,1,1,1,2,2,3,3,4]
print(nums)
i = 0
while i < len(nums):
    if(i>0 and nums[i] == nums[i-1]):
        nums.pop(i)
    else:
        i += 1
    # print(nums[i])
print(nums)
return len(nums)

