def twoSum(nums: list[int], target: int) -> list[int]:
    remainings = {}
    for i in range(0,len(nums)):
        if(nums[i] in remainings):
            return [remainings[nums[i]], i]
        rem = target - nums[i]
        remainings[rem] = i
    return [-1, -1]



tc1 = twoSum(nums=[2,7,11,15], target=9)
print(f'Expected [0, 1] ; Actual {tc1}')