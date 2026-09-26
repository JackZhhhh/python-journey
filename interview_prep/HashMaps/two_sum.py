def two_sum(nums, target):
    d = {}
    for i in range(len(nums)):
        if d.get(target - nums[i], -1) > -1:
            return [d[target-nums[i]], i]
        d[nums[i]] = i
    return []

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # expect 0,1
    print(two_sum([3, 2, 4], 6))          # expect 1,2
    print(two_sum([3, 3], 6))                 # expect 0,1