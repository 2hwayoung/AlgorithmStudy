# 이것이 취업을 위한 코딩 테스트다 with 파이썬 p.237

# 간단한 다익스트라 알고리즘
# 최단 거리가 가장 짧은 노드를 찾기 위해, 매번 최단 거리 테이블을 선형적으로 탐색해야 함
# 시간 복잡도 : O(V^2) , V: 노드의 개수
# 전체 노드의 개수가 5,000개 이하라면 일반적으로 이 코드로 문제를 풀 수 있다.
# 노드의 개수 및 간선의 개수가 많을 때는 '개선된 다익스트라 알고리즘' 이용

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]  (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 모드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(1, n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])


# 개선된 다익스트라 알고리즘
# 특정 노드까지의 최단 거리에 대한 정보를 힙(Heap)에 넣어서 처리하므로 
# 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.
# 비용이 적은 노드를 우선하여 방문하므로 최소 힙 구조를 기반으로 적용하면 된다.
# 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용한다.
# 시간 복잡도 : O(ElogV), V는 노드의 개수, E는 간선의 개수
# 앞의 코드와 비교팼을 때 get_smallest_node() 함수를 작성할 필요가 없다는 특징이 있다.
# -> '최단 거리가 가장 짧은 노드'를 선택하는 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용하는 방식으로 대체할 수 있기 때문
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스르틀 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않으면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])