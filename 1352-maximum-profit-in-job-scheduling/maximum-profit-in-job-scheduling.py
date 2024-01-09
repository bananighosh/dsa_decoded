class Job:
    def __init__(self, startTime, endTime, profit):
        self.startTime = startTime
        self.endTime = endTime
        self.profit = profit

class Solution:
    # def schedule(self, i, job, startTime, n, slots):
    #     if i >= n:
    #         return 0
        
    #     if slots[i] != -1:
    #         return slots[i]
        
    #     curr_start = startTime.index(job[i][1])

    #     pick = job[i][2] + self.schedule(curr_start, job, startTime, n, dp)
    #     np_pick = self.schedule(i + 1, job, startTime, n, dp)
    #     dp[i] = max(pick, no_pick)

    #     return dp[i]

        
    def next_idx(self, jobs, end_index, target_time):
        low = 0
        high = end_index

        while low < high:
            mid = (low + high) // 2
            # if jobs[mid].endTime <= target_time:
            if jobs[mid][0] <= target_time:
                low = mid + 1
            else:
                high = mid

        return low
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = sorted(zip(endTime, startTime, profit))
      
        number_of_jobs = len(profit)
      
        slots = [0] * (number_of_jobs + 1)
      
        for i, (current_end_time, current_start_time, current_profit) in enumerate(jobs):
            # index = bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])
            index = self.next_idx( jobs, i, current_start_time)
            slots[i + 1] = max(slots[i], slots[index] + current_profit)
      
        return slots[number_of_jobs]



        # slots = [-1] * (len(startTime) +1)

        # max_profit = 0
        # # j = len(endTime) - 1

        # # n = len(startTime)

        # # job = [[[startTime[i], endTime[i], profit]] for i in range(n)]

        # # job.sort(key=lambda x: x[1])
        # # startTime.sort()

        # # return self.schedule(0, job, startTime, len(startTime), slots)

        # jobs = sorted(zip(endTime, startTime, profit))
        # num_of_jobs  = len(startTime)

        # for i, (curr_end_time, curr_start_time, curr_profit) in enumerate(jobs):
        #     idx = = bisect_right(jobs, curr_start_time, hi=i, key=lambda x: x[0])
        #     slots[i+1] = max(slots[i], slots[idx] + curr_profit)

        # return dp[num_of_jobs]




        # # for i in range(len(startTime)):
        # #     while j > 0:
        # #         if slots[j] == -1:
        # #             max_profit = max(max_profit, max_profit + profit[j])
        # #             slots[i] += 1
        
        # # return max_profit
