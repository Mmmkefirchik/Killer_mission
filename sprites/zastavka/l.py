
r=5

print(r)
def t():
    global r
    print(r)
    # r=5
    print(r)
    if False:
        r=5
    # r=r-1
    print(r)
t()
t()
