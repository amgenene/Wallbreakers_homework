def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        strv = []
        if n == 1:
            strv.append("1")
            return strv
        for i in range(1, n+1): 
            if i % 3 != 0 and i % 5 != 0: 
                strv.append(str(i))
            elif i % 3 == 0 and i % 5 == 0:
                strv.append("FizzBuzz")
            elif i % 3 == 0:
                strv.append("Fizz")
            elif i % 5 == 0:
                strv.append("Buzz")
        return strv