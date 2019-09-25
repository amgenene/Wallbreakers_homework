def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 1:
            return A
        even = []
        odd = []
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else: 
                odd.append(a)        
        for o in odd:
            even.append(o)
            
        return even
        