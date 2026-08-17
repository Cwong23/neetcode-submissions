class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board[0]), len(board)
        if m * n < len(word):
            return False

        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, x, y):
            # i is the current position in word
            # pos is the current position in the board
            if i == len(word):
                return True
            
            possibles = []
            for d in directions:
                search_x = x + d[0]
                search_y = y + d[1]
                if (search_x, search_y) in visited:
                    continue
                if search_x < 0 or search_x >= m or search_y < 0 or search_y >= n:
                    continue
                if board[search_y][search_x] == word[i]:
                    possibles.append((search_x, search_y))

            if len(possibles) == 0:
                return False
            for p in possibles:
                visited.add(p)
                if dfs(i+1, p[0], p[1]):
                    return True
                visited.remove(p)
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited.add((j, i))
                    if dfs(1, j, i):
                        return True
                    visited.remove((j, i))
        return False
                    
        
            