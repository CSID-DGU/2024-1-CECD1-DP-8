import dgl
import torch
import torch.nn as nn
import torch.nn.functional as F

# 각 해시태그 리스트
hashtags1 = ["#food", "#travel", "#fitness", "#foodie", "#photography", "#nature", "#fashion", "#art", "#love",
             "#music"]
hashtags2 = ["#travel", "#nature", "#photography", "#food", "#traveling", "#adventure", "#explore", "#wanderlust",
             "#landscape", "#vacation", "#foodie", "#fitness", "#fun"]
hashtags3 = ["#food", "#fitness", "#healthy", "#cooking", "#nutrition", "#health", "#diet", "#workout", "#recipes",
             "#gym", "#foodie", "#travel"]
hashtags4 = ["#music", "#art", "#fashion", "#photography", "#artist", "#painting", "#design", "#style", "#creative",
             "#drawing", "#photography", "#travel"]
hashtags5 = ["#love", "#travel", "#foodie", "#photography", "#fashion", "#friends", "#fun", "#happy", "#smile",
             "#memories", "#traveling", "#food"]
hashtags6 = ["#food", "#recipes", "#cooking", "#foodporn", "#yum", "#delicious", "#eat", "#homemade", "#chef",
             "#dinner", "#foodie", "#travel"]
hashtags7 = ["#travel", "#adventure", "#explore", "#wanderlust", "#nature", "#photography", "#vacation", "#trip",
             "#travelgram", "#traveling", "#food", "#fitness"]
hashtags8 = ["#fitness", "#health", "#workout", "#exercise", "#gym", "#fitfam", "#healthy", "#motivation", "#training",
             "#running", "#fitness", "#foodie"]
hashtags9 = ["#photography", "#nature", "#landscape", "#art", "#travel", "#beautiful", "#photooftheday", "#sky",
             "#sunset", "#beach", "#photography", "#food"]
hashtags10 = ["#food", "#music", "#love", "#fashion", "#photography", "#travel", "#art", "#fun", "#friends", "#happy",
              "#traveling", "#foodie"]

hashtags_list = [hashtags1, hashtags2, hashtags3, hashtags4, hashtags5, hashtags6, hashtags7, hashtags8, hashtags9, hashtags10]

# 그래프 생성
G = dgl.DGLGraph()
G.add_nodes(len(set(sum(hashtags_list, []))))  # 모든 해시태그를 노드로 추가

# 각 해시태그 간의 연관 관계를 엣지로 표현
for hashtags in hashtags_list:
    for i in range(len(hashtags)):
        for j in range(i+1, len(hashtags)):
            G.add_edges(hashtags.index(hashtags[i]), hashtags.index(hashtags[j]))

# GNN 모델 정의
class GCN(nn.Module):
    def __init__(self, in_feats, hidden_size, out_feats):
        super(GCN, self).__init__()
        self.conv1 = dgl.nn.GraphConv(in_feats, hidden_size)
        self.conv2 = dgl.nn.GraphConv(hidden_size, out_feats)

    def forward(self, g, inputs):
        h = self.conv1(g, inputs)
        h = F.relu(h)
        h = self.conv2(g, h)
        return h

# 모델 및 데이터 준비
model = GCN(1, 16, 1)  # 입력 특성은 임의로 1로 설정
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 학습
for epoch in range(100):
    logits = model(G, torch.ones(len(G.nodes())).unsqueeze(1).float())  # 임의의 입력 특성 설정
    targets = torch.tensor([1] * len(G.edges()))  # 모든 엣지를 1로 레이블링
    loss = F.binary_cross_entropy_with_logits(logits, targets.float())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# 예측
with torch.no_grad():
    logits = model(G, torch.ones(len(G.nodes())).unsqueeze(1).float())
    predictions = torch.sigmoid(logits)

# 결과 출력
print("Predictions:")
for i, edge in enumerate(G.edges()):
    print(f"{edge[0]} <-> {edge[1]}: {predictions[i].item()}")
