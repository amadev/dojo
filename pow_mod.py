# private int ipow(int base, int exp)
# {
#     int result = 1;
#     while (exp != 0)
#     {
#         if ((exp & 1) == 1)
#             result *= base;
#         exp >>= 1;
#         base *= base;
#     }

#     return result;
# }

#         while(n != 0){
# 22	            if(n % 2 != 0){
# 23	                result = result *  square;
# 24	            }
# 25	            square = (square * square) % d;
# 26	            n = n/2;
# 27	            if(result > d)
# 28	                result = result % d;
# 29	        }


class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if d < 1:
            raise ValueError('not implemented for negative and zero d')
        if n == 0:
            if d == 1:
                return 0
            return 1
        if n < 0:
            raise ValueError('not implemented for negative n')
        if not isinstance(n, (int, long)):
            raise ValueError('not implemented for not int n')
        r = 1
        while (n != 0):
            if n % 2 != 0:
                r *= x
            x = (x * x) % d
            n /= 2
            if r > d or r < 0:
                r %= d
        return r

s = Solution()
# assert 2 == s.pow(2, 3, 3)
# assert 1 == s.pow(2, 0, 3)
# assert 0 == s.pow(2, 0, 1)
assert 19 == s.pow(-1, 1, 20)
