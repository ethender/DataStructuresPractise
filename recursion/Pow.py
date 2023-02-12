class Solution:

    def __init__(self):
        pass

    def myPow(self,x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1/x*self.myPow(x,n+1)
        return x*self.myPow(x,n-1)


    def myPowTwo(self,x,n):
        n = abs(n)
        if n ==0:
            return 1
        elif n%2 == 0:
            return self.myPowTwo(x*x,n//2)
        else:
            return x*self.myPowTwo(x*x,(n-1)//2)

'''
Maths formula for power
 x^n = x(x^2)^(n-1/2) <- n is odd
     = (x^2)^(n/2) <- n is even
'''
if __name__ == '__main__':
    solution = Solution()
    #print(solution.myPow(0.00001,2147483647))
    #print(solution.myPowTwo(0.00001,2147483647))
    print(solution.myPowTwo(2.00000, -2))