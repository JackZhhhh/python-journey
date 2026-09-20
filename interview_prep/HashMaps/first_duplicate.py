def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

if __name__ == "__main__":
    print(first_duplicate([2, 5, 3, 5, 2]))   # expect 5
    print(first_duplicate([1, 2, 3]))          # expect -1
    print(first_duplicate([]))                 # expect -1