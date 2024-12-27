class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        n = len(values)
        max_score = 0

        max_left_score = values[0]

        for i in range(1, n):
            curr_score = values[i] - i

            max_score = max(max_score, max_left_score + curr_score)

            curr_score = values[i] + i

            max_left_score = max(max_left_score, curr_score)
        

        return max_score
        