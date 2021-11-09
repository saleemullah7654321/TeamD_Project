def get_depth_path(d):
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
    
    return 0
