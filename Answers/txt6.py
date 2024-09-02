# Test Cases:
# 'Pig latin is cool' -> 'igPay atinlay siay oolcay'
# 'This is my string' -> 'hisTay siay ymay tringsay'
# "Ultima necat" -> 'ltimaUay ecatnay'
# "Lux in tenebris lucet" -> 'uxLay niay enebristay ucetlay'
# "Cucullus non facit monachum" -> 'ucullusCay onnay acitfay onachummay'


def txt6(word):
    words = word.split()
    lists = []
    for i in words:
        if i[0].isalpha():
            first = i[0]
            remain = i[1:]
            lists.append(remain + first + "ay")
        else:
            lists.append(i)
    return " ".join(lists)

print(txt6("Pig latin is cool"))