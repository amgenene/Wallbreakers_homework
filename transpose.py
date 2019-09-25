def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        columns = []
        for i in range(len(A[0])):
            for a in A:
                columns.append(a[i])
        final = []
        delimeter = len(A)
        for i in range(0, len(columns), len(A)):
            if i < len(columns) - len(A):
                final.append(list(columns[i:delimeter]))
                print(delimeter)
                delimeter+= (len(A))
            else:
                final.append(list(columns[i:]))
        print(final)
        return final