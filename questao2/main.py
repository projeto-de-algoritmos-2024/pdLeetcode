class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * (len(jobs) + 1)
        times = [0] + [job[1] for job in jobs]
        
        for i in range(1, len(jobs) + 1):
            s, e, p = jobs[i - 1]
            idx = bisect.bisect_right(times, s) - 1
            dp[i] = max(dp[i - 1], dp[idx] + p)
        
        return dp[-1]
        