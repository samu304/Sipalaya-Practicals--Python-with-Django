# 12. Given an integer array nums, rotate the array to the right by k steps, where k is non-negative. For example nums = [1,2,3,4,5,6,7], k=3 should output [5,6,7,1,2,3,4] Do it with the least possible space. I.e O(1) space complexity.Make your code as “pythonic” as you possibly can use shortcuts that may not be available 


array1 = [1,2,3,4,5,6,7]

# rotate the array to the right by k steps
def right_array_rotation(nums, k):
    for i in range(0,k):
        temp = nums[len(array1) - 1]
        for j in range(len(array1) - 1, 0, -1):
            nums[j] = nums[j - 1]
        nums[0] = temp
    return nums


# rotate the array to the left by k steps
def left_array_rotation(nums, k):
    for a in range(0, k):
        temp = nums[0]
        for b in range(0, len(array1)-1):
            nums[b] = nums[b + 1]
        nums[len(array1) - 1] = temp
    return nums


print(f'The original array is : {array1}\n')

right = right_array_rotation(array1, 2)
print(f"The right array rotated is : {right}\n")

left = left_array_rotation(array1, 2)
print(f"The left array rotated is {left}")