def ComputeOpt(j):
    if j < 0:
        return 0
    if M[j]:
        return M[j]
    M[j] = max(ComputeOpt(j - 1), events[j][2] + ComputeOpt(p[j]))
    return M[j]

def findSolution(k):
    if k < 0:
        return
    if k == 0 or M[k] != M[k - 1]:
        selected.append(events[k])
        findSolution(p[k])
    else:
        findSolution(k - 1)

n = int(input("Enter number of events: "))
events = []

print("Enter start time, finish time, and profit of each event (space separated):")
for i in range(n):
    events.append(tuple(map(int, input(f"Schedule {i + 1}: ").split())))

events = sorted(events, key=lambda x: x[1])

p = [0] * n
for i in range(n):
    for j in range(i - 1, -1, -1):
        if events[i][0] >= events[j][1]:
            p[i] = j
            break
    else:
        p[i] = -1

M = [0] * n
selected = []
print("\nMax profit:", ComputeOpt(n - 1))
findSolution(n - 1)
print("\nEvents selected:", selected)