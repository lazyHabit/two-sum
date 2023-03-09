def twoSum(nums, target):

    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i,j]