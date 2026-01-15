class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def maxArea(bars: list[int]) -> int:
            bars.sort()
            res = 1
            streak = 1
            for i in range(1, len(bars)):
                if bars[i] - bars[i - 1] == 1:
                    streak += 1
                else:
                    streak = 1
                res = max(res, streak)
            return res + 1
        
        return min(maxArea(hBars), maxArea(vBars)) ** 2
        