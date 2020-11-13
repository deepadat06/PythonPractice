# Code starts here

# lambda function to calculate square

square = lambda x : x ** 2

# natural numbers list

nums = [1,2,3,4,5,6,7,8,9,10]

# empty list

square_nums = []

# loop through every element in list

for i in range(0,10):
    sum_sq = square(nums[i])
    square_nums.append(sum_sq)  

# display new list
print(square_nums)
