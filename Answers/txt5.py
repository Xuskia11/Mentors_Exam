# Test Cases:
# a=[1,2] b=[1] -> [2]
# a=[1,2,2,2,3] b=[2,3] -> [1]
# a=[18, 8, -14] b=[8, -20, -16, -18] -> [18, -14]
# a=[6, -9, -1] b=[-3, -4, 17, -4, 10, -16, -12, 11, -2, 17, 2, 1, 6] -> [-9, -1]
# a=[-8, -2, -4, 13, 10, -12, -3, 6] b=[-3, 17] -> [-8, -2, -4, 13, 10, -12, 6]


def txt5(lists,listn):
    return [i for i in lists if i not in listn]

print(txt5([1,2],[1]))