class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp=[0]*(len(books)+1)
        for i in range(len(books)-1,-1,-1):
            current_width = shelfWidth
            max_height=0
            dp[i] = float('inf')
            for j in range(i,len(books)):
                width,height = books[j]
                if current_width< width:
                    break
                current_width-=width
                max_height = max(max_height,height)
                dp[i]=min(dp[i],dp[j+1]+max_height)
        return dp[0]