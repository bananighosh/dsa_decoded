class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        map1 = Counter(s1)
        map2 = Counter(s2[:len(s1) - 1])

        left = 0

        # for char in s1:
        #     map1[char] += 1
        
        # for i in range(len(s1)):
        #     map2[s2[i]] += 1

        for right in range(len(s1) - 1, len(s2)):
            map2[s2[right]] += 1
            if map1 == map2:
                return True

            map2[s2[left]] -= 1
            if map2[s2[left]] == 0:
                del map2[s2[left]]
            left += 1
        
        return False
        