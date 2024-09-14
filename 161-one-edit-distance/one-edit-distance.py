class Solution:
    def isOneEditDistance(self, s: "str", t: "str") -> "bool":

        len_s, len_t = len(s), len(t)

        if s == t or (abs(len_s - len_t) > 1):
            return False
        
        length = min(len_s, len_t)

        for i in range(length):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:] or s[i+1:] == t[i:]

        return len(s[length:] + t[length:]) <= 1

        # return len_s + 1 == len_t

        # i = 0

        # while i < len_s and i < len_t and s[i] == t[i]:
        #     i += 1
        
        # if i == len(s) and i == len(t):
        #     return False

        # if(len_s > len_t):
        #      return s[i+1:] == t[i:]
        # elif(len_s < len_t):
        #     return s[i:] == t[i+1:]
        # else:
        #     return s[i+1:] == t[i+1:]
        



        
        
        