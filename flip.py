  def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        for rev in A:
            rev = rev[::-1]
            rev = [x ^ 1 for x in rev] 
            A[i] = rev
            i+=1
        
            
        return A