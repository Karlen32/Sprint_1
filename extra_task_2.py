def digit_root(num):
    while num > 9:
        num = sum(int(i) for i in str(num))
    return num
print (digit_root(12345))
print (digit_root(943))
print (digit_root(999998888))
