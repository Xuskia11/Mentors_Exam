# Test Cases:
# 70304 -> '70000 + 300 + 4'
# 42 -> '40 + 2'
# 710163 -> '700000 + 10000 + 100 + 60 + 3'
# 853546 -> '800000 + 50000 + 3000 + 500 + 40 + 6'
# 511604 -> '500000 + 10000 + 1000 + 600 + 4'

def txt3(numbers):
    word = str(numbers)
    lists = []
    for i,num in enumerate(word):
        if num != 0:
            lists.append(num + ("0" * (len(word) - i - 1)))
    return " + ".join(lists)

print(txt3(70304))
print(txt3(710163))
