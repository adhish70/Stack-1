# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# Logic: We keep on pushing into the stack if the incomming number is 
# less than the top of the stack. If the incoming number is more then 
# until all the numbers less than it are found we pop and calculate the 
# answer.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0 for _ in range(n)]
        
        stack = []
        
        for i in range(n):
            if stack:                
                while stack and temperatures[i] > stack[-1][0]:
                    num, idx = stack.pop()
                    res[idx] = i - idx
                    
            stack.append((temperatures[i], i))
        
        return res