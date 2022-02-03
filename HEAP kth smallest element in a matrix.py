import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        T=[]
        for i in range(len(matrix)):
            for item in matrix[i]:
                T.append(item)
        heapq.heapify(T)
        for i in range(k-1):
            heapq.heappop(T)
        return T[0]
            
        