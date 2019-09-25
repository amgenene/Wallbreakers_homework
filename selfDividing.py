def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        strv = []
        final = []
        flag = 0
        counter = 0
        for a in range(left, right + 1): 
            strv.append(str(a))
        for i in range(left, right + 1):
            if i <= 9:
                final.append(i)
                counter+=1
            elif i % 10 == 0:
                counter+=1
                continue
            else:
                flag = 0
                for s in range(len(strv[counter])):
                    if "0" in strv[counter]:
                            flag = 1
                            break
                    elif i % int(strv[counter][s]) == 0:
                        continue
                    else:
                        flag = 1
                if flag == 0:
                    final.append(i)
                counter+=1
        return final