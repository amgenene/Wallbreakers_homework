def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = []
        n = 0
        while num:
            binary.append(num & 1)
            num >>= 1
        counter = 0
        for bin in range(len(binary)):
            if binary[bin] == 0:
                binary[bin] += 1
            else: binary[bin] -= 1
        # binary = binary[::-1]
        for i in range(len(binary)):
            if binary[i] == 1:
                n += (2**i)
        # num ^= mask
        return n