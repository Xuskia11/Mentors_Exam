# Write python program that will turn decimal number into binary number.

# Test Cases:
# 32 -> 100000
# 31 -> 11111
# 8 -> 1000

def aialgo3(test):
    binary = ""
    while test > 0:
        x = test % 2
        binary = str(x) + binary
        test //= 2
    return binary

print(aialgo3(8)) 