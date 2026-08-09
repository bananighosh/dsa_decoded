class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        n = len(num)
        temp = t
        factors = [2,3,5,7]

        for primeFact in factors:
            while temp % primeFact == 0:
                temp /= primeFact
        
        if temp != 1:
            return "-1"
        
        remainingFactor = [0] * (n + 1)
        remainingFactor[0] = t
        pos = n - 1
        for i in range(n):
            if num[i] == "0":
                pos = i
                break
            digit = ord(num[i]) - ord('0')
            remainingFactor[i + 1] = remainingFactor[i] // math.gcd(remainingFactor[i], digit)
        
        if remainingFactor[n] == 1:
            return num
        
        def fillFreeSlots(required, length):
            res = []
            for digit in range(9, 1, -1):
                while required % digit == 0:
                    res.append(digit)
                    required //= digit
            
            while len(res) < length:
                res.append(1)
            
            return "".join(map(str, reversed(res)))


        for i in range(pos, -1, -1):
            required = remainingFactor[i]
            freeSlots = n - 1 - i

            for digit in range(int(num[i]) + 1, 10):
                furtherRequired = required // gcd(required, digit)
                requiredNumber = fillFreeSlots(furtherRequired, freeSlots)

                if len(requiredNumber) == freeSlots:
                    return num[:i] + str(digit) +requiredNumber

        return fillFreeSlots(t, n + 1)        
