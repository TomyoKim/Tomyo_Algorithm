from collections import deque


def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))

    q = deque([(["ICN"], tickets)])

    while q:
        np, nt = q.popleft()

        if len(nt) == 0:
            answer = np
            break

        v = -1
        for i in range(len(nt)):
            if nt[i][0] == np[-1]:
                v = i
                break

        if v == -1:
            continue

        while v < len(nt) and nt[v][0] == np[-1]:
            q.append((np + [nt[v][1]], nt[:v] + nt[v + 1:]))

            v += 1

    return answer