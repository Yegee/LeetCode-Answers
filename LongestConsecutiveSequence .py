def longestConsecutive(nums: List[int]) -> int:
    highest = 0

    for index in range(len(nums)):
        temp = nums[index]
        current = 1
        if ((temp - 1) not in nums):
            while (temp + 1) in nums:
                current += 1
                temp += 1
    
        if current > highest:
            highest = current
    return highest


nums = [0,3,2,5,4,6,1,1]

print(longestConsecutive(nums))