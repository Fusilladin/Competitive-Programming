def modify_multiply(st, loc, num):
    _var = st.split()
    _pos = _var[loc]
    a = (_pos+"-")*num
    return a.rstrip("-")