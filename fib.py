#!/usr/bin/python
import time
data = {}

def fib(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        if(data.has_key(n-1) and data.has_key(n-2)):
            result = data[n-1] + data[n-2]
            data[n] = result
            return result
        elif(data.has_key(n-1) or data.has_key(n-2)):
            if(data.has_key(n-1)):
                result = data[n-1] + fib(n-2)
                data[n] = result
                return result
            else:
                result = fib(n-1) + data[n-2]
                data[n] = result
                return result
        else:
            result = fib(n-1) + fib(n-2)
            data[n] = result
            return result
        
def fib_recurse(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_recurse(n-1) + fib_recurse(n-2)

if __name__ == "__main__":
    print "Find Fibonacci Number \n"
    x = raw_input("Enter a number: ")
    if x.isdigit():
            i = int(x)
            start_time = time.time()
            print "Result from Dictionary:",fib(i)
            time_dic = time.time()-start_time
            print "Runtime for Dictinary:", time_dic
            start_time = time.time()
            print "Result from Recursive:",fib_recurse(i)
            time_rec = time.time()-start_time
            print "Runtime for Recursive:",time.time()-start_time
            print "Difference in Runtime (Recursive vs Dic)",time_rec-time_dic,"\n"
    else:
        print "That is not an integer"