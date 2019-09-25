 def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = 2 ** 0
        i = 0
        if n % 2 != 0 and n != 1:
            return False
        else:
            while num <= n:
                if num == n:
                    return True
                else:
                    i+=1
                    num = 2 ** i
                    continue
            return False