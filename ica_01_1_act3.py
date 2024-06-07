print("The function str_mult() has been called.  For this activity, we won't print out any details about its parameters.")
def str_mult(a, b):
    out = ''
    for _ in range(b):
        out += a
    return out