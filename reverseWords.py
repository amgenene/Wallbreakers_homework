def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        newstr = []
        beginningOfWord = -1
        endOfWord = 0
        i = 0
        for i in range(-1, -len(s), -1):
            if s[i] == " ":
                endOfWord = i+1
                if beginningOfWord == -1:
                    newstr.append(s[endOfWord:])
                    beginningOfWord = i
                else:
                    newstr.append(s[endOfWord:beginningOfWord])
                    beginningOfWord = i
        newstr.append(s[0:endOfWord])
        newstr = ' '.join(newstr)
        newstr = newstr.strip()
        if beginningOfWord != -1:
            return newstr
        else:
            return s