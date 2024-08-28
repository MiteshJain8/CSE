def backtrack(r):
    if r==n:
        res.append([" ".join(row) for row in board])
        return
    for c in range(n):
        if c in col or (r+c) in posDiag or (r-c) in negDiag:
            continue
        col.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)
        board[r][c] = 'Q'

        backtrack(r+1)

        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)
        board[r][c] = '_'

n = int(input("Enter the number of queens: "))
col = set()
negDiag = set() #(r-c) \
posDiag = set() #(r+c) /
res = []
board = [['_'] * n for _ in range(n)]
backtrack(0)
print("Number of ways:",len(res))
print("\nPossible arrangements:")
for r in res:
    print(r)