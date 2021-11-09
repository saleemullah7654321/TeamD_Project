import re


def count_evens(a):
    b=[i for i in a if i%2==0]
    return len(b)

# count_evens([1,2,3,2,4,4,4])
# Question #2:
def analyze(str1):
    d=0
    l=0
    for i in str1:
        if i.isnumeric():
            d+=1
        elif i.isalpha():
            l=l+1
        else:
            pass
    return (l,d)

# analyze("2345ab")

def sort_deck(input):
    customOreder = {'Jack':0, 'Queen':1, 'King':2,'Ace':3}
    strs = list(filter(lambda x : type(x) ==str,input))
    ints = list(filter(lambda x: type(x) == int, input))

    output =  sorted(ints) + sorted(strs,key=customOreder.__getitem__)
    return output
# print(sort_deck([2,3,5,4,'Queen','King',7,'Ace','Queen', 9,'Jack','King']))

def int_to_col(n):
    if n==0:
        return 'Invalid column number'
    elif not isinstance(n,int):
        return 'Invalid column number'
    string = ''
    while n > 0:
        rem = n%26
        print('rem:',rem)
        if rem == 0:
            string+='Z'
            n = int((n/26)-1)
        else:
            string+= chr(rem + (ord('A')-1))
            n = int(n/26)

        print('n:',n)
        print(string)
    string1 = string[::-1]
    return string1

def get_depth(d):
    o=[]
    def v_check(val):
        if isinstance(val,(int,str)):
            o.append(val)
    def check(d):
        if isinstance(d, dict):
            for v in d.values():
                if isinstance(v, (dict,list)):
                    check(v)
                else:
                    v_check(v)
        elif isinstance(d, list):
            for v in d:
                if isinstance(v, (dict,list)):
                    check(v)
                else:
                    v_check(v)
    check(d)
    
    return o
