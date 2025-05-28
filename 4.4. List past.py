def is_palindrome(mun_list):
    reverse_list= num_list[::-1]
    if mun_list == reverse_list:
        return True
    else:
        return False

nums = [1,2,3,4,5,6,7,8,9]

for i_nums in range(0,len(nums)):
    if is_palindrome(nums[i_nums:len(nums)]):
        answer = nums[i_nums:]
        answer.reverse()
        break

print(answer)

