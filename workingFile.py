
import re
def count_evens(a):
    b=[i for i in a if i%2==0]
    print(len(b))

count_evens([1,2,3,2,4,4,4])

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
