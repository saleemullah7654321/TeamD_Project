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
