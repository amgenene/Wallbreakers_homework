 def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper():
            return True
        if word.islower():
            return True
        for letter in range(len(word)):
            if letter == 0 and ord(word[letter]) >= 65 and  ord(word[letter]) <= 90:
                flag = 0
                continue
            elif letter != 0 and ord(word[letter]) >= 65 and  ord(word[letter]) <= 90:
                return False
        if flag == 0: return True