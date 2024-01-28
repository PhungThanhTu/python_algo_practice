nums = [9,1,4,7,3,-1,0,5,8,-1,6]

# convert to set
nums_set = set(nums)

# sort the set
sorted_nums_set = sorted(nums_set)
sorted_nums_list = list(sorted_nums_set)
print(sorted_nums_list)

consecutive_elements_count = 1
max_consecutive_element_count = 1
for i in range(1, len(sorted_nums_list)):
    if sorted_nums_list[i] - sorted_nums_list[i-1] == 1:
        consecutive_elements_count += 1
        if consecutive_elements_count > max_consecutive_element_count:
            max_consecutive_element_count = consecutive_elements_count
    else:
        consecutive_elements_count = 1
print("Result:")
print(max_consecutive_element_count)