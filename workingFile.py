def sort_deck(input):
    customOreder = {'Jack':0, 'Queen':1, 'King':2,'Ace':3}
    strs = list(filter(lambda x : type(x) ==str,input))
    ints = list(filter(lambda x: type(x) == int, input))

    output =  sorted(ints) + sorted(strs,key=customOreder.__getitem__)
    return output
# print(sort_deck([2,3,5,4,'Queen','King',7,'Ace','Queen', 9,'Jack','King']))
