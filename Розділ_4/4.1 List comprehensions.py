from test import new_num


def is_palindrome(num_list):
    reverse_list =[]
    for i_num in range(len(num_list) -1,-1,-1,):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False

nums = [1,2,3,2,1]
new_num = []
anser = []


for i_nums in range(len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_num.append(nums[j_elem])
    if is_palindrome(new_num):
        for i_answer in range(0, i_nums):
            anser.append(nums[i_answer])
            anser.reverse()
            break

    new_num = []
print('',nums)
print('',len(anser))
print('',anser)
