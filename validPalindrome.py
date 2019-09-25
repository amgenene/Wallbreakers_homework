  def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        if len(s) == 1:
            return True
        i = 0
        e = -1
        letter_counter = 0
        while i > e and e > -len(s):
            if s[i].isalnum() and s[e].isalnum():
                if s[i] == s[e]:
                    i += 1
                    e -= 1
                    continue
                else:
                    return False
            elif not (s[e].isalnum()):
                e-=1
            elif not (s[i].isalnum()):
                i+=1
        return True 