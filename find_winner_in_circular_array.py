class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queued=deque(range(1,n+1))
        while len(queued)>1:
            for _ in range(k-1):
                queued.append(queued.popleft())
                
            queued.popleft()
        return queued[0]
# i did't get it, I just memorized it