# 외판원 순회 2

N = int(input())
weightList = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]

answer = float('inf')


def travelCity(start, now, count, sumWeight):
    global answer
    if N == count+1 and weightList[now][start] != 0:
        sumWeight += weightList[now][start]
        answer = min(answer, sumWeight)
        return

    for i in range(N):
        if not visited[i] and weightList[now][i] != 0:
            visited[i] = True
            travelCity(start, i, count+1, sumWeight+weightList[now][i])
            visited[i] = False


for i in range(N):
    visited[i] = True
    travelCity(i, i, 0, 0)

print(answer)
