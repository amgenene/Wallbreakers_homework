 def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = -1
        counter = 0
        while i >= (len(s)/2) * -1:
            temp = s[counter]
            s[counter] = s[i]
            s[i] = temp
            i-=1
            counter +=1