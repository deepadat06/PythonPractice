# Code starts here

# natural numbers from 1 to 20

natural_nums = []
for i in range (0,20):
    natural_nums.append(i+1)

# lambda function for even numbers

is_even = lambda x : x % 2 == 0

# filter() to filter out even elements

filtered = list(filter(is_even,natural_nums))

print(filtered)

# Code ends here
