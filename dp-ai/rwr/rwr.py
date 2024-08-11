import csv
import numpy as np


def rwr(weighted_edges, seed_node, restart_prob=0.15, max_iters=100, tol=1e-6):
    """
    Random Walk with Restart 알고리즘을 이용하여 특정 노드와 연관이 있는 노드들의 순위 리스트를 반환합니다.

    Parameters:
        weighted_edges (list): 가중치가 포함된 방향 그래프의 간선 정보
        seed_node (str): 시작 노드
        restart_prob (float): 리스타트 확률 (기본값은 0.15)
        max_iters (int): 최대 반복 횟수 (기본값은 100)
        tol (float): 수렴 기준 (기본값은 1e-6)

    Returns:
        list: 특정 노드와 연관이 있는 노드들의 순위 리스트
    """
    # 노드 목록 생성
    nodes = set()
    for edge in weighted_edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    nodes = list(nodes)
    n = len(nodes)

    # 노드의 이름을 정수 인덱스로 매핑
    node_to_index = {node: i for i, node in enumerate(nodes)}

    # 전이 확률 행렬 생성
    transition_matrix = np.zeros((n, n))
    for edge in weighted_edges:
        i = node_to_index[edge[0]]
        j = node_to_index[edge[1]]
        transition_matrix[j, i] = edge[2]  # 가중치는 A에서 B로 이동할 확률로 사용됨

    # 리스타트 벡터 생성
    restart_vector = np.zeros(n)
    restart_vector[node_to_index[seed_node]] = 1

    scores = np.zeros(n)
    scores[node_to_index[seed_node]] = 1  # 시작 노드의 스코어를 1로 초기화

    # 반복적으로 스코어 계산
    for _ in range(max_iters):
        prev_scores = np.copy(scores)
        scores = restart_prob * np.dot(transition_matrix, scores) + (1 - restart_prob) * restart_vector

        if np.linalg.norm(scores - prev_scores, ord=1) < tol:
            break

    # 결과를 정렬하여 반환
    ranked_nodes = sorted(zip(nodes, scores), key=lambda x: x[1], reverse=True)
    return ranked_nodes


# 가중치 정보
weighted_edges = []

with open('directed.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        weighted_edges.append((row[0], row[1], row[2]))

# 사용자로부터 시작 노드 입력 받기
while True:
    seed_node = input("시작 노드를 입력하세요: ")
    if seed_node not in [edge[0] for edge in weighted_edges]:
        print("해당 노드가 그래프에 존재하지 않습니다. 다시 입력하세요.")
    else:
        break

# RWR 알고리즘 적용
result = rwr(weighted_edges, seed_node)

# 결과 출력
print(f"특정 노드({seed_node})와 연관이 있는 상위 20개의 노드:")
for node, score in result[:20]:
    print(f"{node}: {score:.8f}")
