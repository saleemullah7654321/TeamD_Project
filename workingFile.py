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
    print(l,d)

analyze("2345ab")