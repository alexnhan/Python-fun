#!/usr/bin/python

def fibonacciMem(n, mem):
        try:
                val=mem[n]
                print "found in mem"
                return val
        except IndexError:
                if n==0:
                        mem.append(0)
                        return mem[0]
                elif n==1:
                        mem.append(1)
                        return mem[1]
                elif n==2:
                        mem.append(1)
                        return mem[2]
                else:
                        mem.append(fibonacciMem(n-1,mem)+fibonacciMem(n-2,mem))
                        return mem[n]

def printFibMem(n,mem):
        for i in xrange(0,n):
              print fibonacciMem(i,mem)

def fibonacci(n):
        if n==0:
                return 0
        elif n==1 or n==2:
                return 1
        else:
                return fibonacci(n-1)+fibonacci(n-2)

def printFib(n):
        for i in xrange(0,n):
                print fibonacci(n)
if __name__ == "__main__":
        n=500
        mem=[]
        printFibMem(n,mem)
        #printFib(n)
