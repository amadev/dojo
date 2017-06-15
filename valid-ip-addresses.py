

class Solution:
    def check_ip(self, ip):
        for i in range(4):
            try:
                n = int(ip[i])
            except ValueError:
                return False
            if n <  0 or n > 255:
                return False
            if ip[i][0] == '0' and len(ip[i]) > 1:
                return False
        return True

    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        A = A.strip()
        n = len(A)
        if n < 4:
            return []
        if n == 4:
            return ['.'.join([A[0], A[1], A[2], A[3]])]
        r = []
        points = [1, 2, 3]
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    points = [i, j, k]
                    ip = [A[0:points[0]], A[points[0]:points[1]],
                          A[points[1]:points[2]], A[points[2]:]]
                    #print 'ip', ip
                    if self.check_ip(ip):
                        r.append('.'.join(ip))
        return r



s = Solution()
assert ['255.255.11.135', '255.255.111.35'] ==  s.restoreIpAddresses('25525511135')
assert ['1.2.3.4'] ==  s.restoreIpAddresses('1234')
assert [] ==  s.restoreIpAddresses('00000')
assert ['0.0.0.0'] ==  s.restoreIpAddresses('0000')
assert ['0.10.0.100', '0.100.10.0'] == s.restoreIpAddresses('0100100')
assert [] == s.restoreIpAddresses('     ')
assert [] == s.restoreIpAddresses('abcde')
