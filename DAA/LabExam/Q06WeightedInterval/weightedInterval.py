def ComputeOpt(x):
    if x == 0:
        return 0
    elif M[x - 1]:
        return M[x - 1]
    else:
        M[x - 1] = max(ComputeOpt(x - 1), lst[x - 1][2] + ComputeOpt(p[x - 1]))
        return M[x - 1]


def findSolution(k):
    if k < 1:
        return
    i = k
    while i > 1 and M[i - 1] == M[i - 2]:
        i -= 1
    selected.append(lst[i - 1])
    findSolution(p[i - 1])


n = int(input("Enter number of events: "))
lst = []
print("Enter start time, finish time and profit of each event separated by space")
for i in range(n):
    tup = tuple(map(int, input(f"Schedule {i+1}: ").split()))
    lst.append(tup)
lst = sorted(lst, key=lambda x: x[1])

p = [0 for i in range(len(lst))]
for i in range(len(lst) - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        if lst[i][0] >= lst[j][1]:
            p[i] = j + 1
            break

M = [0 for i in range(len(lst))]
selected = []
print("\nMax profit: ",ComputeOpt(len(lst)))
findSolution(len(lst))
print("\nEvents selected: ",selected)