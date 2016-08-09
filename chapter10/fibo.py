#フィボナッチ数モジュール
def fib(n):
    a,b=0,1
    while b<n:
        print(b,end='')
        a,b=b,a+b


def fib2(n):
    resuld=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result

if_name_=='_mian_':
    import sys
    fib(int(sys.argv[1]))
