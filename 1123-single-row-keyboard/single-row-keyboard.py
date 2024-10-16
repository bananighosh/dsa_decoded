class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        indexMap = defaultdict(int)

        for idx, c in enumerate(keyboard):
            indexMap[c] = idx

        time = 0
        prev_idx = 0
        for c in word:
            idx = indexMap[c]
            time += abs(idx - prev_idx)
            prev_idx = idx
        return time



        