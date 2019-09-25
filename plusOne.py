 def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        new_list = []
        digits = digits[::-1]
        for i in range(len(digits)):
            num += (digits[i] * (10 ** i))
        num += 1
        num = str(num)
        for num in num:
            new_list.append(num)      
        return new_list