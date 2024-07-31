def ComputeOpt(j):
    if j < 0:
        return 0
    if M[j]:
        return M[j]
    M[j] = max(ComputeOpt(j - 1), lst[j][2] + ComputeOpt(p[j]))
    return M[j]

def findSolution(k):
    if k < 0:
        return
    if k == 0 or M[k] != M[k - 1]:
        selected.append(lst[k])
        findSolution(p[k])
    else:
        findSolution(k - 1)

n = int(input("Enter number of events: "))
lst = []
print("Enter start time, finish time, and profit of each event separated by space")
for i in range(n):
    tup = tuple(map(int, input(f"Schedule {i + 1}: ").split()))
    lst.append(tup)

lst = sorted(lst, key=lambda x: x[1])

p = [0] * len(lst)
for i in range(len(lst)):
    for j in range(i - 1, -1, -1):
        if lst[i][0] >= lst[j][1]:
            p[i] = j
            break
    else:
        p[i] = -1

M = [0] * len(lst)
selected = []
print("\nMax profit:", ComputeOpt(len(lst) - 1))
findSolution(len(lst) - 1)
print("\nEvents selected:", selected)