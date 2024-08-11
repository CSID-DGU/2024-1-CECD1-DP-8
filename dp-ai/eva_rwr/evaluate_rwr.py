import csv
import numpy as np
from collections import defaultdict
from sklearn.metrics import precision_score, recall_score, f1_score
import math

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
        transition_matrix[j, i] = float(edge[2])

    # 전이 확률 행렬의 열 정규화
    for i in range(n):
        col_sum = np.sum(transition_matrix[:, i])
        if col_sum > 0:
            transition_matrix[:, i] /= col_sum

    # 리스타트 벡터 생성
    restart_vector = np.zeros(n)
    restart_vector[node_to_index[seed_node]] = 1

    # 스코어 벡터 초기화
    scores = np.zeros(n)
    scores[node_to_index[seed_node]] = 1

    # 반복적으로 스코어 계산
    for _ in range(max_iters):
        prev_scores = np.copy(scores)
        scores = restart_prob * np.dot(transition_matrix, scores) + (1 - restart_prob) * restart_vector

        if np.linalg.norm(scores - prev_scores, ord=1) < tol:
            break

    # 결과를 정렬하여 반환
    ranked_nodes = sorted(zip(nodes, scores), key=lambda x: x[1], reverse=True)
    return ranked_nodes

def load_ground_truth(file_path):
    """
    ground_truth.csv 파일에서 데이터를 로드합니다.

    Parameters:
        file_path (str): 파일 경로

    Returns:
        defaultdict: 해시태그와 연관된 해시태그 및 가중치 정보
    """
    ground_truth = defaultdict(list)
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 헤더 건너뛰기
        for row in reader:
            data = row[0].split()
            ground_truth[data[0]].append((data[1], float(data[2])))
    return ground_truth

def load_weighted_edges(file_path):
    """
    directed.csv 파일에서 데이터를 로드합니다.

    Parameters:
        file_path (str): 파일 경로

    Returns:
        list: 가중치가 포함된 방향 그래프의 간선 정보
    """
    weighted_edges = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            weighted_edges.append((row[0], row[1], float(row[2])))
    return weighted_edges

def precision_at_k(ranked_list, ground_truth, k):
    """
    Precision@K 계산

    Parameters:
        ranked_list (list): 순위 리스트
        ground_truth (list): 실제 연관된 해시태그 리스트
        k (int): 상위 K개 항목

    Returns:
        float: Precision@K
    """
    top_k = [node for node, score in ranked_list[:k]]
    relevant = [node for node, score in ground_truth]
    true_positives = len(set(top_k) & set(relevant))
    return true_positives / k

def mean_reciprocal_rank(ranked_list, ground_truth):
    """
    Mean Reciprocal Rank 계산

    Parameters:
        ranked_list (list): 순위 리스트
        ground_truth (list): 실제 연관된 해시태그 리스트

    Returns:
        float: MRR
    """
    relevant = {node for node, score in ground_truth}
    for i, (node, score) in enumerate(ranked_list):
        if node in relevant:
            return 1 / (i + 1)
    return 0

def mean_average_precision(ranked_list, ground_truth):
    """
    Mean Average Precision 계산

    Parameters:
        ranked_list (list): 순위 리스트
        ground_truth (list): 실제 연관된 해시태그 리스트

    Returns:
        float: MAP
    """
    relevant = {node for node, score in ground_truth}
    ap_sum = 0.0
    relevant_count = 0
    for i, (node, score) in enumerate(ranked_list):
        if node in relevant:
            relevant_count += 1
            ap_sum += relevant_count / (i + 1)
    return ap_sum / len(relevant) if relevant else 0

def ndcg(ranked_list, ground_truth, k):
    """
    Normalized Discounted Cumulative Gain 계산

    Parameters:
        ranked_list (list): 순위 리스트
        ground_truth (list): 실제 연관된 해시태그 리스트
        k (int): 상위 K개 항목

    Returns:
        float: NDCG@K
    """
    def dcg(rel_scores):
        return sum((2 ** score - 1) / math.log2(idx + 2) for idx, score in enumerate(rel_scores))

    relevant_scores = {node: score for node, score in ground_truth}
    ranked_scores = [relevant_scores.get(node, 0) for node, score in ranked_list[:k]]
    ideal_scores = sorted(relevant_scores.values(), reverse=True)[:k]

    return dcg(ranked_scores) / dcg(ideal_scores) if ideal_scores else 0

def calculate_precision_recall_f1(ranked_list, ground_truth, k):
    """
    Precision, Recall, F1-Score 계산

    Parameters:
        ranked_list (list): 순위 리스트
        ground_truth (list): 실제 연관된 해시태그 리스트
        k (int): 상위 K개 항목

    Returns:
        tuple: Precision, Recall, F1-Score
    """
    relevant = set(node for node, score in ground_truth)
    top_k = [node for node, score in ranked_list[:k]]

    y_true = [1 if node in relevant else 0 for node in top_k]
    y_pred = [1] * len(y_true)  # y_pred는 top_k 리스트의 길이만큼 1로 설정

    # Extend y_true와 y_pred를 동일한 길이로 맞추기
    max_len = max(len(y_true), k)
    y_true.extend([0] * (max_len - len(y_true)))
    y_pred.extend([0] * (max_len - len(y_pred)))

    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    return precision, recall, f1

# 데이터 로드
ground_truth = load_ground_truth('ground_truth.csv')
weighted_edges = load_weighted_edges('directed.csv')

# 사용자로부터 시작 노드 입력 받기
while True:
    seed_node = input("시작 노드를 입력하세요: ")
    if seed_node not in [edge[0] for edge in weighted_edges]:
        print("해당 노드가 그래프에 존재하지 않습니다. 다시 입력하세요.")
    else:
        break

# RWR 알고리즘 적용
rwr_result = rwr(weighted_edges, seed_node)

# 시작 노드에 대한 ground truth 준비
gt_for_seed = ground_truth.get(seed_node, [])

# 평가
k = 10
prec_at_k = precision_at_k(rwr_result, gt_for_seed, k)
mrr = mean_reciprocal_rank(rwr_result, gt_for_seed)
map_score = mean_average_precision(rwr_result, gt_for_seed)
ndcg_score = ndcg(rwr_result, gt_for_seed, k)
precision, recall, f1 = calculate_precision_recall_f1(rwr_result, gt_for_seed, k)

print(f"Precision@{k}: {prec_at_k:.4f}")
print(f"MRR: {mrr:.4f}")
print(f"MAP: {map_score:.4f}")
print(f"NDCG@{k}: {ndcg_score:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
