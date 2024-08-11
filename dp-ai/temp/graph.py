import csv
import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations


def get_all_hashtags_from_csv(filename):
    tokens_list = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            tokens_list.extend(row)
    return list(set(tokens_list))


if __name__ == '__main__':
    G = nx.Graph()

    hashtags_list = get_all_hashtags_from_csv('data.csv')
    G.add_nodes_from(hashtags_list)

    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            com = list(combinations(row, 2))
            for c in com:
                if not G.has_edge(c[0], c[1]):
                    G.add_edge(c[0], c[1], weight=1)
                else:
                    G[c[0]][c[1]]['weight'] += 1

    directed_graph = nx.Graph()
    directed_graph.add_nodes_from(hashtags_list)

    for u, v, weight in G.edges(data='weight'):
        u_adj_sum = 0
        for node in G[u]:
            u_adj_sum += G[u][node]['weight']
        directed_graph.add_edge(u, v, weight=G[u][v]['weight'] / u_adj_sum)

        v_adj_sum = 0
        for node in G[v]:
            v_adj_sum += G[v][node]['weight']
        directed_graph.add_edge(v, u, weight=G[v][u]['weight'] / v_adj_sum)

    # 방향 그래프 CSV 파일로 저장
    with open('directed.csv', 'w', newline='') as csvfile:
        for u, v, weight in directed_graph.edges(data='weight'):
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([u, v, weight])
