#txt1

# lists = ['w','e','w','e','w','e','w','e','w','e','w','e']
# ['n','s','n','s','n','s','n','s','n','s'] -> True
# ['n','n','n','s','n','s','n','s','n','s'] -> False
# ['e', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] -> False
# ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] -> True


def txt1(lists):
    if len(lists) != 10:
        return False
    n_s = lists.count("n") - lists.count("s")
    e_w = lists.count("e") - lists.count("w")
    if n_s == 0 and e_w == 0:
        return True
    else:
        return False
    

print(txt1(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(txt1([['n','s','n','s','n','s','n','s','n','s']]))
print(txt1([['n','n','n','s','n','s','n','s','n','s']]))




    