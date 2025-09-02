

def loop_plus(n : int) -> int:
    all = 0
    for i in range(1,n+1):
        all = all +i

    return all

def loop_plus2():
    i = 1
    all = 0
    while i <10:
        i = i+1
        all = all + i

    return all

def loop_plus3():
    all = 0
    n = 10
    for i in range(n,n+1):
        print(i)
        for j in range (5):
            all = i + j
            print(all)
    return all

def loop_plus4(i : int) -> int:
    if i == 1:
        return 1

    res = loop_plus4(i - 1)
    #10+9+8+7+6+5+4+3+2+1

    return i + res

def loop_plus5(n,res):
    if n == 0 :
        return res
    return loop_plus5(n - 1 , res + n)

if __name__ == '__main__':
    print(loop_plus2())
    print(loop_plus3())
    print(loop_plus4(10))
    print(loop_plus5(10))