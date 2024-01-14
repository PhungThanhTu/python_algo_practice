def check_neg(i, j, nums, map, result):
    product_by_neg_1 = -1 * (nums[i] + nums[j])
    if product_by_neg_1 in map:
        result.append(sorted((nums[i], nums[j], product_by_neg_1)))

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    pos_nums = []
    neg_nums = []
    nums_map = {
        key: True
        for key in nums
    }
    print(nums)
    result = []

    for num in nums:
        if num > 0:
            pos_nums.append(num)
        if num < 0:
            neg_nums.append(num)
    print(pos_nums)
    print(neg_nums)

    neg_nums_len = len(neg_nums)
    if neg_nums_len > 1:
        for i in range(neg_nums_len):
            for j in range (i+1, neg_nums_len):
               check_neg(i, j, neg_nums, nums_map, result)
    pos_nums_len = len(pos_nums)
    if pos_nums_len > 1:
        for i in range(pos_nums_len):
            for j in range(i+1, pos_nums_len):
               check_neg(i, j, pos_nums, nums_map, result)

    zero_checking_nums = neg_nums if neg_nums_len < pos_nums_len else pos_nums
    zero_checking_nums_len = neg_nums_len if neg_nums_len < pos_nums_len else pos_nums_len
    zero_checking_map = {}
    if zero_checking_nums_len >= 1 and 0 in nums_map:
            for i in range(zero_checking_nums_len):
                print(f'inspecting {i}')
                if -1 * zero_checking_nums[i] in nums_map:
                    if not zero_checking_nums[i] in zero_checking_map:
                        zero_checking_map[zero_checking_nums[i]] = True
                        result.append(sorted((zero_checking_nums[i], 0, -1 * zero_checking_nums[i])))
                    
    return result

nums = [-2,0,0,2,2]

print(threeSum(nums))