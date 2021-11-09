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