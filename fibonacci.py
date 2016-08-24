def main(x):
    for i in range(x):
        print(fibonacciLoop(i))

def fibonacciLoop(number):
    fib1,fib2,result = 1,1,1
    if(number == 1 or number == 2):
        return 1
    
    for i in range(3, number, 1):
        result = fib1 + fib2
        fib1 = fib2
        fib2 = result
    
    return result

main(15)
        
    