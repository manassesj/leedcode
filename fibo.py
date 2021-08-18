n = int(input())

if n == 1:
    print("0")
elif n == 2:
    print("0 1")
else:  
    fib = "0 1"
    prev = 0
    curr_number = 1
    for n in range(n - 2):
        sm = prev + curr_number
        fib += " {}".format(sm)
        prev = curr_number
        curr_number = sm
    print(fib)


