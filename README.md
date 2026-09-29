# 자료구조 문제

| 문제 | 주제 | 폴더 |
|---|---|---|
| 작업 스케줄러 | 우선순위 큐 (최소 힙) | [`problems/pq-task-scheduler`](problems/pq-task-scheduler/README.md) |

각 문제 폴더에는 문제 설명(`README.md`), 참고 풀이(`solution.py`), 검증용 완전 탐색(`brute.py`),
예제 입출력(`examples/`), 테스트(`test_solution.py`)가 들어 있다. Python 3 표준 라이브러리만 사용한다.

```
python3 -m unittest discover -s problems/pq-task-scheduler -p "test_*.py"
```
