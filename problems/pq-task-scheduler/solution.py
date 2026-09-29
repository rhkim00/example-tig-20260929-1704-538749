"""작업 스케줄러 - 우선순위 큐(최소 힙)를 이용한 O(N log N) 풀이."""

import heapq
import sys


def schedule(tasks):
    """tasks: (도착 시각, 실행 시간, 우선순위) 튜플의 리스트.

    (1부터 시작하는 실행 순서, 대기 시간의 합)을 반환한다.
    """
    n = len(tasks)
    by_arrival = sorted(range(n), key=lambda i: (tasks[i][0], i))
    heap = []
    order = []
    total_wait = 0
    now = 0
    k = 0
    while len(order) < n:
        # 대기 중인 작업이 없으면 다음 도착 시각까지 CPU가 쉰다.
        if not heap and now < tasks[by_arrival[k]][0]:
            now = tasks[by_arrival[k]][0]
        while k < n and tasks[by_arrival[k]][0] <= now:
            i = by_arrival[k]
            heapq.heappush(heap, (tasks[i][2], tasks[i][0], i))
            k += 1
        _, arrival, i = heapq.heappop(heap)
        total_wait += now - arrival
        now += tasks[i][1]
        order.append(i + 1)
    return order, total_wait


def parse(data):
    it = iter(data.split())
    n = int(next(it))
    return [(int(next(it)), int(next(it)), int(next(it))) for _ in range(n)]


def format_output(order, total_wait):
    return " ".join(map(str, order)) + "\n" + str(total_wait) + "\n"


def solve(data):
    return format_output(*schedule(parse(data)))


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
