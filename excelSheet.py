 def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = ["", "A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        ret = 0
        it = 0
        for i in reversed(s):
            idx = str.index(i)
            ret += ((26 ** it) * idx)
            it +=1
        return ret