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
