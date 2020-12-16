'''
The word starts in the top left corner, continues downwards for 2 more letters, then the letter to the right followed by 2 letters moving upwards, the final letter at the right of the penultimate one.

Write a function which takes in a target word and a grid of letters and returns a list of tuples, each tuple being the row and column of the corresponding letter in the grid (numbered from 0). If the word cannot be found, output the string "Not present".
'''

def trace_word_path(word, grid):
    n, m = len(grid), len(grid[0])
    dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}
    ans = [[(i, j)] for j in range(m) for i in range(n) \
						if grid[i][j] == word[0]]
    for k in range(1, len(word)):
        ans = [a+[(a[-1][0]+i, a[-1][1]+j)] for a in ans for (i, j) in dirs
               if a[-1][0]+i in range(n) and a[-1][1]+j in range(m) and
               word[k] == grid[a[-1][0]+i][a[-1][1]+j]
							 and (a[-1][0]+i,a[-1][1]+j) not in a]
    return 'Not present' if not ans else ans[0]
