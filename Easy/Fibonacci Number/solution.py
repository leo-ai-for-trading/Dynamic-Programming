class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            #binet's formula
            first_term = pow((1+sqrt(5)),n)
            second_term = pow((1-sqrt(5)),n)
            f = (first_term - second_term)/(pow(2,n)*sqrt(5))
            return int(f)
