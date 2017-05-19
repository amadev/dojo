class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        r = []
        for i in range(1, A + 1):
            n = ''
            if i % 3 == 0:
                n += 'Fizz'
            if i % 5 == 0:
                n += 'Buzz'
            if not n:
                n = str(i)
            r.append(n)
        return r

s = Solution()
print s.fizzBuzz(15)
print s.fizzBuzz(0)
