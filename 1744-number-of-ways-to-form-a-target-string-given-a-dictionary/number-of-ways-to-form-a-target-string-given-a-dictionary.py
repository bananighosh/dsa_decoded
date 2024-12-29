class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        word_length = len(words[0])
        target_length = len(target)
        mod = 1000000007

        char_frequency = [[0] * 26 for _ in range(word_length)]
        for word in words:
            for j in range(word_length):
                char_frequency[j][ord(word[j]) - ord("a")] += 1

        dp = [[0] * (target_length + 1) for _ in range(word_length + 1)]

        for curr_word in range(word_length + 1):
            dp[curr_word][0] = 1

        for curr_word in range(1, word_length + 1):
            for curr_target in range(1, target_length + 1):

                dp[curr_word][curr_target] = dp[curr_word - 1][curr_target]

                cur_pos = ord(target[curr_target - 1]) - ord("a")
                dp[curr_word][curr_target] += (
                    char_frequency[curr_word - 1][cur_pos]
                    * dp[curr_word - 1][curr_target - 1]
                ) % mod
                dp[curr_word][curr_target] %= mod

        return dp[word_length][target_length]
        