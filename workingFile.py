import re
def count_evens(a):
    b=[i for i in a if i%2==0]
    print(len(b))

count_evens([1,2,3,2,4,4,4])