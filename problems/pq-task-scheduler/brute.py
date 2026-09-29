"""작업 스케줄러 - 규칙을 그대로 시뮬레이션하는 O(N^2) 검증용 풀이."""

import sys

from solution import format_output, parse


def schedule(tasks):
    n = len(tasks)
    done = [False] * n
    order = []
    total_wait = 0
    now = 0
    for _ in range(n):
        waiting = [i for i in range(n) if not done[i] and tasks[i][0] <= now]
        if not waiting:
            now = min(tasks[i][0] for i in range(n) if not done[i])
            waiting = [i for i in range(n) if not done[i] and tasks[i][0] <= now]
        i = min(waiting, key=lambda j: (tasks[j][2], tasks[j][0], j))
        done[i] = True
        total_wait += now - tasks[i][0]
        now += tasks[i][1]
        order.append(i + 1)
    return order, total_wait


def solve(data):
    return format_output(*schedule(parse(data)))


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))
