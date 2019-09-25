def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        newstr = []
        counter = 0
        for i in reversed(s):
            if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                vowels.append(i)
        for i in s:
            if i not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                newstr.append(i)
            else:
                newstr.append(vowels[counter])
                counter+=1
        finalstr = ''.join(newstr)
        return finalstr