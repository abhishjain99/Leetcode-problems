class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxAbility = max(worker)
        jobs = [0] * (maxAbility + 1) # storing profits in array
        for i in range(len(difficulty)):
            if difficulty[i] <= maxAbility:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
        
        for i in range(1, maxAbility+1):
            jobs[i] = max(jobs[i], jobs[i-1])
        
        ans = 0
        for ability in worker:
            ans += jobs[ability]
        return ans