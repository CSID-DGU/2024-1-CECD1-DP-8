import pandas as pd
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# CSV 파일 읽어들이기
data = pd.read_csv('전처리6.csv')

# 텍스트 데이터 전처리
sentences = [text.split() for text in data['data']]

# Word2Vec 모델 훈련
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# 단어 벡터 추출
word_vectors = model.wv.vectors

# KMeans 클러스터링
kmeans = KMeans(n_clusters=20)
clusters = kmeans.fit_predict(word_vectors)

# 각 클러스터에 속한 단어 출력
for cluster_idx in range(20):  # 클러스터 개수에 따라서 수정
    print(f"Cluster {cluster_idx}:")
    words_in_cluster = [model.wv.index_to_key[idx] for idx, cluster_label in enumerate(clusters) if
                        cluster_label == cluster_idx]
    print(words_in_cluster)
    print()

# TSNE를 사용하여 단어 벡터를 2차원으로 축소
tsne = TSNE(n_components=2, random_state=42)
word_vectors_2d = tsne.fit_transform(word_vectors)

# 시각화
plt.figure(figsize=(20, 7))
for cluster in range(10):  # 클러스터 개수에 따라서 수정
    plt.scatter(word_vectors_2d[clusters == cluster, 0], word_vectors_2d[clusters == cluster, 1],
                label=f'Cluster {cluster}')
plt.title('Word2Vec Clustering with TSNE Visualization')
plt.legend()
plt.show()
