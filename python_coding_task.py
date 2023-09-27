# Problem 1
# Given an array of integers nums and an integer target, return indices of the two numbers such that
# they add up to target.

def target_number_sum(numbers, target):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i,j]
                

nums1 = [2, 7, 11, 15]
target1 = 9
print(target_number_sum(nums1, target1))


nums = [3,3]
target = 6
print(target_number_sum(nums, target))



# Problem 2
# Given a string s containing characters '(', ')', '{', '}', '[' and ']'
# determine if the string is valid

def string_is_valid(string):
    list = []
    characters = {')': '(', '}': '{', ']': '['}
    for c in string:
        if c in characters:
            char = list.pop() if list else '#'
            if characters[c] != char:
                return False
        else:
            list.append(c)
    return not list

print(string_is_valid("[}"))
print(string_is_valid("[]"))


# Problem 3
# Given an integer array nums and an integer k, return the k most frequent elements. You may return
# the answer in any order.
def frequent_elements(list, k):
    d = {}
    l =[]
    for n in list:
        d[n] = d.get(n, 0) + 1
    sort = sorted(d.items(), key=lambda x: x[1], reverse=True)

    for item in sort[:k]:
        l.append(item[0])
    return l

n1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(frequent_elements(n1, k1))

n2 = [1,2,3,3,4,4,4,5,5,6,6]
k2 = 3
print(frequent_elements(n2, k2))