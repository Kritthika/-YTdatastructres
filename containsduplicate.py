def contains_duplicate(nums):
    seen= set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
nums = [1,2,3,1]
print(contains_duplicate(nums) )      
