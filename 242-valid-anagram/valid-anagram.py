class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_hash = Counter(s)
        t_hash = Counter(t)
        print(s_hash, t_hash)
        return s_hash == t_hash
        