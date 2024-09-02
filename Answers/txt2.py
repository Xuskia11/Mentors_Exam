

#[] -> True
# [1, 2, 3, 4] -> True
# [1.0, 2.0, 3.0] -> True
# [1.0, 2.0, 3.0001] -> False
# ["-1"] -> False


def txt2(lists):
    if len(lists) == 0:
        return True
    
    for i in lists:
        if not isinstance(i, (int,float)):
            return False
        elif type(i) == float and i.is_integer() == False:
            return False
        else:
            return True

print(txt2([1, 2, 3, 4]))
print(txt2([1.0, 2.0, 3.0]))
print(txt2([1.0, 2.0, 3.0001]))