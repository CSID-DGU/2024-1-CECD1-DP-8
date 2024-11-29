import csv
import os

# Additional query-answer data following the specified template
qa_data = [
    {
        "query": "팔로워 수가 5000명 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 14011명의 팔로워를 보유하고 있으며, 패션 트렌드를 이끄는 콘텐츠로 인기를 끌고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 약 10495명의 팔로워가 있으며, 다양한 여행지에서 스타일을 공유하여 높은 인기를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 약 10100명의 팔로워와 스킨케어 루틴을 공유하며 신뢰도를 높이고 있습니다.""",
    },
    {
        "query": "뷰티 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 다양한 뷰티 제품을 잘 홍보하며 사용 후기를 통해 신뢰를 줍니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 피부 진정 제품을 자주 홍보하고 사용자의 경험을 공유합니다.
---
influencer_id: 8
name: 권지현
reason: 뷰티 제품 소개에 강점을 지니고 있습니다.""",
    },
    {
        "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워와의 소통이 활발하고 다양한 뷰티 제품을 자주 리뷰합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 팔로워와의 친근한 소통이 가능하여 신뢰도가 높습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글에 대한 반응이 좋고 소통이 활발합니다.""",
    },
    {
        "query": "평균 좋아요 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 평균 좋아요 수가 200개 이상이며, 콘텐츠의 질이 높아 반응이 좋습니다.
---
influencer_id: 8
name: 권지현
reason: 다양한 콘텐츠에서 평균적으로 높은 좋아요 수를 기록합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 제품 리뷰에서 항상 높은 좋아요 수를 유지합니다.""",
    },
    {
        "query": "여행지에서 찍은 사진을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 14
name: 솔솔씨
reason: 여행지에서 찍은 사진을 잘 홍보하며, 관련된 콘텐츠에 특화되어 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 여행지에서 사진을 찍고 이를 잘 홍보합니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 여행 사진을 자주 공유하며 관련 제품을 홍보합니다.""",
    },
    {
        "query": "반응 지수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 광고 게시물의 참여도가 높아 반응 지수가 우수합니다.
---
influencer_id: 8
name: 권지현
reason: 다양한 제품에 대한 높은 반응을 이끌어내고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 댓글과 좋아요 수가 많아 반응 지수가 높은 편입니다.""",
    },
    {
        "query": "패션 트렌드를 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드를 잘 소개하고, 다양한 스타일을 소화합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 트렌드를 이끄는 콘텐츠로 많은 사랑을 받고 있습니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 패션 트렌드를 자주 다루며 팔로워들에게 최신 정보를 제공합니다.""",
    },
    {
        "query": "계절별 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 계절별 스킨케어 루틴을 효과적으로 설명하여 신뢰를 얻고 있습니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 계절에 따라 적절한 스킨케어 제품을 소개하여 도움이 됩니다.
---
influencer_id: 8
name: 권지현
reason: 다양한 계절에 맞춘 스킨케어 루틴을 제안합니다.""",
    },
    {
        "query": "남성 팔로워가 많은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 남성 팔로워 비율이 높으며, 남성 패션을 주로 다룹니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 남성 팔로워가 많고, 다양한 스타일을 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 팔로워들에게 인기 있는 콘텐츠를 많이 만듭니다.""",
    },
    {
        "query": "여름 패션 아이템을 효과적으로 홍보할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 패션 아이템을 잘 홍보하며, 다양한 스타일을 소개합니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 여름 패션에 적합한 아이템을 자주 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름철 트렌디한 아이템을 효과적으로 홍보합니다.""",
    },
    {
        "query": "피부 진정 크림을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 피부 진정 크림을 자주 리뷰하며 효과를 상세히 설명합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 진정 크림을 효과적으로 홍보하고, 사용자의 경험을 공유합니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 피부 고민에 대해 진정 크림을 추천합니다.""",
    },
    {
        "query": "팔로워와 친근한 소통이 가능한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워와의 친근한 소통이 가능하여 신뢰도가 높습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 소통이 활발하며 팔로워와의 관계를 중시합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글에 대한 반응이 좋고 소통이 활발합니다.""",
    },
    {
        "query": "광고 게시물의 참여도가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 오드리
reason: 광고 게시물의 참여도가 높아 인플루언서로서 효과적인 홍보가 가능합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 광고 게시물의 반응이 뛰어나 참여도가 높습니다.
---
influencer_id: 8
name: 권지현
reason: 제품 홍보 시 높은 참여를 이끌어내고 있습니다.""",
    },
    {
        "query": "평균 댓글 수가 많은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 평균 댓글 수가 많고, 다양한 반응을 이끌어내고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 댓글 참여가 활발하며, 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 12
name: 마르 Marr
reason: 제품 리뷰에서 항상 많은 댓글을 받습니다.""",
    },
    {
        "query": "저가형 스킨케어 제품을 잘 소개할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 저가형 스킨케어 제품을 자주 소개하며, 소비자들에게 호평을 받고 있습니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 다양한 저렴한 스킨케어 제품을 리뷰하여 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 저가형 제품에 대한 실용적인 리뷰를 제공합니다.""",
    },
    {
        "query": "인테리어와 관련된 제품을 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 7
name: 인테리어 아이디어
reason: 인테리어와 관련된 제품을 잘 홍보하며, 다양한 디자인 팁을 제공합니다.
---
influencer_id: 15
name: 집꾸미기 전문가
reason: 인테리어 제품을 추천하고 효과적으로 홍보합니다.
---
influencer_id: 16
name: 인테리어 스타일러
reason: 다양한 인테리어 제품을 홍보하며 트렌디한 정보를 제공합니다.""",
    },
    {
        "query": "팔로워가 10000명 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 14011명의 팔로워를 보유하고 있으며, 패션 트렌드를 이끄는 콘텐츠로 인기를 끌고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 약 10495명의 팔로워가 있으며, 다양한 여행지에서 스타일을 공유하여 높은 인기를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 약 10100명의 팔로워와 스킨케어 루틴을 공유하며 신뢰도를 높이고 있습니다.""",
    },
    {
        "query": "여름철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수품을 효과적으로 소개하며, 다양한 제품에 대한 정보를 공유합니다.
---
influencer_id: 8
name: 권지현
reason: 여름철 필수 아이템에 대한 리뷰와 추천을 잘합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 필수품을 자주 소개하고 신뢰도를 얻고 있습니다.""",
    },
    {
        "query": "반응이 활발한 뷰티 카테고리 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 뷰티 카테고리에서 반응이 활발하며, 많은 참여를 이끌어냅니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 뷰티 제품 홍보에서 반응이 좋고 소통이 활발합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 뷰티 제품에 대한 높은 반응을 이끌어내고 있습니다.""",
    },
    {
        "query": "간편한 다이어트 제품을 잘 소개할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 간편한 다이어트 제품을 자주 소개하고, 실용적인 조언을 제공합니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 다이어트 제품을 소개하며, 사용자 경험을 공유합니다.
---
influencer_id: 8
name: 권지현
reason: 간편한 다이어트 제품에 대한 리뷰를 진행합니다.""",
    },
    {
        "query": "다양한 장소에서 찍은 여행 사진을 잘 홍보하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 14
name: 솔솔씨
reason: 다양한 장소에서 찍은 여행 사진을 잘 홍보하고, 관련된 콘텐츠에 특화되어 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여행지에서 찍은 사진을 자주 공유하며 자연스럽게 홍보합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 장소에서 촬영한 콘텐츠로 여행의 매력을 잘 전달합니다.""",
    },
    {
        "query": "겨울철 보습 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 겨울철 보습 제품을 잘 홍보하며, 사용 후기를 바탕으로 신뢰를 줍니다.
---
influencer_id: 8
name: 권지현
reason: 겨울철 필수 보습 제품을 자주 소개하고 효과를 설명합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 겨울철 스킨케어에 대한 조언을 잘 합니다.""",
    },
    {
        "query": "새로운 패션 스타일을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 새로운 패션 스타일을 자주 소개하여 팔로워들에게 트렌디한 정보를 제공합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 새로운 패션 스타일을 공유하여 큰 인기를 얻고 있습니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 최신 패션 스타일을 자주 다루며 팔로워들의 관심을 끌고 있습니다.""",
    },
    {
        "query": "남성 팔로워가 많은 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 남성 팔로워 비율이 높고, 남성 패션에 대한 깊은 이해를 바탕으로 콘텐츠를 제공합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 팔로워들에게 인기가 많은 콘텐츠를 많이 만듭니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 남성 팔로워와 소통하며 다양한 스타일을 공유합니다.""",
    },
    {
        "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 3
name: 코덕 오드리
reason: 신뢰할 수 있는 스킨케어 리뷰를 제공하여 팔로워들의 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 스킨케어 제품에 대한 솔직한 리뷰로 신뢰를 쌓고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 제품에 대한 세세한 리뷰를 남겨 신뢰를 쌓고 있습니다.""",
    },
    {
        "query": "피부 타입별 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 피부 타입별 스킨케어 루틴을 효과적으로 설명하여 많은 도움이 됩니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 각 피부 타입에 맞는 스킨케어 제품 추천을 잘합니다.
---
influencer_id: 8
name: 권지현
reason: 피부 타입별로 맞춤형 스킨케어 루틴을 소개합니다.""",
    },
    {
        "query": "제품에 대한 세세한 리뷰를 남기는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 제품에 대한 세세한 리뷰를 남겨 팔로워들에게 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 제품 사용 후기를 상세히 리뷰하여 효과를 잘 설명합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 제품에 대한 깊이 있는 리뷰를 제공하여 신뢰를 쌓고 있습니다.""",
    },
    {
        "query": "여름철 선크림을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 여름철 선크림을 잘 홍보하며, 피부 보호에 대한 중요성을 강조합니다.
---
influencer_id: 12
name: 마르Marr
reason: 여름철 필수 선크림을 자주 리뷰하고 효과를 잘 설명합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 선크림 제품을 효과적으로 홍보하며 사용자 경험을 공유합니다.""",
    },
    {
        "query": "계절에 맞는 패션 아이템을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 계절별 패션 아이템을 자주 소개하여 트렌디한 정보를 제공합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 계절에 따라 적절한 패션 아이템을 소개하며 많은 사랑을 받고 있습니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 계절에 맞는 스타일링을 잘 소개하고 다양한 아이템을 제안합니다.""",
    },
    {
        "query": "반응 지수가 높은 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 콘텐츠의 반응 지수가 높고 참여도가 우수합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 높은 반응 지수로 패션 트렌드를 잘 전달합니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 패션 콘텐츠에서 좋은 반응을 이끌어내고 있습니다.""",
    },
    {
        "query": "팔로워 수 대비 반응도가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워 수 대비 높은 반응도를 보여주며, 콘텐츠의 질이 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워 수에 비해 높은 참여를 유도하여 반응도가 뛰어납니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 팔로워 수와 반응이 잘 맞아떨어져 인기가 많습니다.""",
    },
    {
        "query": "주로 소통을 활발히 하며 제품을 자연스럽게 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 소통이 활발하며 제품을 자연스럽게 소개하는 데 능숙합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 팔로워와의 관계를 중시하며 제품 리뷰를 자연스럽게 진행합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 제품 홍보 시 소통을 잘 하며 자연스러운 리뷰를 제공합니다.""",
    },
    {
        "query": "트렌디한 패션 아이템을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 트렌디한 패션 아이템을 잘 소개하며 최신 스타일을 반영합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 트렌드를 이끄는 콘텐츠로 많은 사랑을 받고 있습니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 트렌디한 아이템을 자주 소개하여 팔로워들에게 인기가 많습니다.""",
    },
    {
        "query": "피부 개선을 위한 뷰티 제품을 잘 홍보하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 피부 개선에 효과적인 제품을 잘 홍보하며, 사용 후기를 공유합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 피부 개선에 도움이 되는 다양한 뷰티 제품을 소개합니다.
---
influencer_id: 8
name: 권지현
reason: 피부 개선을 위한 제품을 자주 리뷰하여 신뢰를 얻고 있습니다.""",
    },
    {
        "query": "평균 좋아요 수가 높은 여행 인플루언서를 추천해줘.",
        "answer": """influencer_id: 14
name: 솔솔씨
reason: 여행지에서 찍은 사진의 평균 좋아요 수가 높습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 여행지의 콘텐츠에서 높은 좋아요 수를 기록합니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 여행 관련 콘텐츠에서 좋은 반응을 이끌어내고 있습니다.""",
    },
    {
        "query": "자연스러운 일상 사진으로 홍보를 잘하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 자연스러운 일상 사진으로 제품을 잘 홍보하며 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 일상 사진을 자연스럽게 활용하여 제품 홍보를 잘합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 자연스러운 일상 속 제품 리뷰가 인상적입니다.""",
    },
    {
        "query": "다이어트 식품을 소개할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 다이어트 관련 제품을 자주 소개하며 실용적인 조언을 제공합니다.
---
influencer_id: 8
name: 권지현
reason: 다양한 다이어트 제품에 대한 리뷰를 진행합니다.
---
influencer_id: 1
name: 코덕❤
reason: 다이어트 식품을 활용한 실제 경험을 공유합니다.""",
    },
    {
        "query": "스킨케어 제품의 신뢰도가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 3
name: 코덕 오드리
reason: 스킨케어 제품에 대한 신뢰도 높은 리뷰를 제공하여 팔로워의 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 스킨케어 제품에 대한 솔직한 리뷰로 신뢰를 쌓고 있습니다.
---
influencer_id: 8
name: 권지현
reason: 제품 리뷰에서 신뢰도를 높이는 콘텐츠를 제공합니다.""",
    },
    {
        "query": "친환경 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 7
name: 인테리어 아이디어
reason: 친환경 인테리어 제품을 소개하여 지속 가능한 라이프스타일을 강조합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 친환경 뷰티 제품을 자주 리뷰하여 신뢰를 얻고 있습니다.
---
influencer_id: 8
name: 권지현
reason: 다양한 친환경 제품을 소개하며 소비자에게 효과적으로 전달합니다.""",
    },
    {
        "query": "가성비 좋은 뷰티 제품을 소개할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 가성비 좋은 뷰티 제품을 자주 리뷰하고 효과를 설명합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 다양한 저가형 뷰티 제품을 소개하여 소비자들에게 호평을 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 가성비 좋은 제품을 실용적으로 소개하여 인기를 끌고 있습니다.""",
    },
    {
        "query": "소통을 중요시하는 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워와의 소통을 중시하며 패션 아이템을 자연스럽게 소개합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 소통을 중요시하고, 패션과 관련된 다양한 조언을 제공합니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 팔로워와의 관계를 중시하며 소통을 자주 합니다.""",
    },
    {
        "query": "저자극 제품을 주로 사용하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 저자극 제품을 자주 리뷰하며 피부 고민에 대한 솔루션을 제공합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 저자극 스킨케어 제품을 자주 사용하여 경험을 공유합니다.
---
influencer_id: 8
name: 권지현
reason: 저자극 제품에 대한 리뷰를 통해 신뢰를 쌓고 있습니다.""",
    },
    {
        "query": "팔로워 수가 많고 평균 댓글이 많은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 14011명의 팔로워를 보유하고 있으며, 평균 댓글 수가 높습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 많은 팔로워와 함께 평균 댓글 수가 많아 소통이 활발합니다.
---
influencer_id: 8
name: 권지현
reason: 댓글 참여가 활발하며 평균적으로 많은 반응을 이끌어냅니다.""",
    },
    {
        "query": "피드백이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피드백에 대한 반응이 빠르고 적극적입니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 팔로워의 피드백을 잘 반영하여 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 사용자 피드백에 신속하게 반응하여 좋은 관계를 유지합니다.""",
    },
    {
        "query": "패션 브랜드와의 협업 경험이 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 패션 브랜드와 협업을 진행하여 신뢰를 쌓고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션 브랜드와의 협업 경험이 많아 효과적으로 홍보할 수 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 패션 브랜드와의 협업을 통해 다양한 제품을 소개하고 있습니다.""",
    },
    {
        "query": "계절별 피부 관리 제품을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 계절별 피부 관리 제품을 효과적으로 소개하여 도움이 됩니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 계절에 맞는 스킨케어 제품을 자주 리뷰하여 유용한 정보를 제공합니다.
---
influencer_id: 8
name: 권지현
reason: 계절별로 적절한 피부 관리 제품을 추천합니다.""",
    },
    {
        "query": "팔로워 수가 많고 반응이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 14011명의 팔로워를 보유하고 있으며, 반응이 활발합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 높은 반응으로 인플루언서로서의 신뢰도를 쌓고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 팔로워와의 소통이 원활하여 반응이 좋습니다.""",
    },
    {
        "query": "다양한 메이크업 제품을 잘 홍보하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 다양한 메이크업 제품을 잘 홍보하며 사용 팁을 제공합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 메이크업 제품에 대한 깊이 있는 리뷰를 제공하여 팔로워의 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 메이크업 제품을 다양하게 소개하며 효과를 상세히 설명합니다.""",
    },
    {
        "query": "최신 뷰티 트렌드를 반영하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 최신 뷰티 트렌드를 반영한 리뷰로 팔로워들에게 유익한 정보를 제공합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 뷰티 트렌드에 맞춘 제품을 소개하며 팔로워와 소통합니다.
---
influencer_id: 8
name: 권지현
reason: 트렌디한 뷰티 제품을 자주 리뷰하여 팔로워의 관심을 끌고 있습니다.""",
    },
    {
        "query": "평균 좋아요 수가 높아 반응이 좋은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 평균 좋아요 수가 높아 콘텐츠의 질이 우수합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 평균적으로 높은 좋아요 수를 기록하며 인기가 많습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 제품 홍보에서 평균 좋아요 수가 높은 편입니다.""",
    },
    {
        "query": "팔로워 수가 2000명 이하이면서 소통이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 신선한 소식
reason: 팔로워 수가 1500명 이하이지만 소통이 활발하여 신뢰를 얻고 있습니다.
---
influencer_id: 14
name: 소소한 일상
reason: 팔로워 수가 적지만, 사용자와의 소통이 잘 이루어집니다.
---
influencer_id: 15
name: 진솔한 리뷰
reason: 소통이 활발하여 팔로워들과의 관계를 잘 유지하고 있습니다.""",
    },
    {
        "query": "비건 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 7
name: 비건 라이프
reason: 비건 제품에 대한 정보와 사용기를 자주 공유하여 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 비건 뷰티 제품을 자주 리뷰하여 소비자에게 효과적으로 전달합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 비건 스킨케어 제품에 대한 솔직한 리뷰를 제공합니다.""",
    },
    {
        "query": "세심하게 리뷰하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 제품에 대한 세세한 리뷰를 남겨 팔로워들에게 신뢰를 얻고 있습니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 사용자의 경험을 바탕으로 상세한 리뷰를 제공합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 제품에 대한 꼼꼼한 리뷰로 팔로워들에게 유익한 정보를 전달합니다.""",
    },
    {
        "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글 참여율이 높고, 팔로워와의 소통이 활발합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 댓글에 대한 반응이 좋고 참여가 활발하여 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 참여가 많아 활발한 소통을 이어가고 있습니다.""",
    },
    {
        "query": "피부 관리 팁을 제공하는 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 피부 관리에 대한 유용한 팁을 자주 공유하여 신뢰를 얻고 있습니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 다양한 피부 관리 팁과 제품을 소개하여 팔로워에게 도움을 주고 있습니다.
---
influencer_id: 8
name: 권지현
reason: 피부 관리와 관련된 정보와 팁을 제공하여 많은 사랑을 받고 있습니다.""",
    },
    {
        "query": "겨울 패션을 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 겨울 패션 아이템을 잘 소개하며, 트렌디한 스타일을 제공합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 겨울철 패션을 자주 소개하고 다양한 스타일을 보여줍니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 겨울철 패션 아이템을 자주 리뷰하여 팔로워의 관심을 끌고 있습니다.""",
    },
    {
        "query": "학생층이 많이 팔로우하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 스타일과 저렴한 가격의 제품을 자주 소개하여 학생들에게 인기가 많습니다.
---
influencer_id: 1
name: 코덕❤
reason: 학생들이 선호하는 뷰티 제품과 팁을 자주 공유하여 신뢰를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 학생층이 선호하는 다양한 제품 리뷰를 제공하여 많은 사랑을 받고 있습니다.""",
    },
    {
        "query": "각종 이벤트에 참여하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 이벤트에 적극적으로 참여하며 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 관련 이벤트에 자주 참여하여 트렌드를 선도합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 각종 뷰티 및 패션 이벤트에 참여하여 활발한 활동을 보이고 있습니다.""",
    },
    {
        "query": "일상에서 사용하는 제품을 자주 리뷰하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 일상에서 사용한 제품을 자주 리뷰하여 팔로워에게 신뢰를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 일상 제품에 대한 리뷰를 통해 유용한 정보를 제공합니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 일상 속 패션 아이템을 자주 소개하여 팔로워의 관심을 끌고 있습니다.""",
    },
    {
        "query": "제품 홍보 경험이 많은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 다양한 제품 홍보 경험이 많아 효과적으로 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션과 뷰티 제품을 여러 차례 홍보한 경험이 있어 신뢰를 쌓고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 제품을 자주 리뷰하고 효과적으로 홍보하는 인플루언서입니다.""",
    },
    {
        "query": "계절별로 피부 관리법을 제공하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 계절별로 적절한 피부 관리법을 제공하여 많은 도움이 됩니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 계절에 맞춘 피부 관리 정보를 자주 공유하여 팔로워들에게 유익합니다.
---
influencer_id: 8
name: 권지현
reason: 계절에 따라 적합한 스킨케어 제품을 추천하여 도움이 됩니다.""",
    },
    {
        "query": "높은 팔로워 수를 가진 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 14011명의 팔로워를 보유하고 있으며, 뷰티와 패션에 대한 신뢰도를 쌓고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 약 10100명의 팔로워를 보유하고 있으며, 뷰티 관련 콘텐츠에서 인기를 끌고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 높은 팔로워 수와 다양한 뷰티 제품 리뷰로 신뢰를 얻고 있습니다.""",
    },
    {
        "query": "신제품에 대한 리뷰가 빠른 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 신제품에 대한 리뷰를 빠르게 진행하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 새로운 제품을 신속하게 리뷰하고 소통하는 데 능숙합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 신제품에 대한 솔직한 리뷰를 자주 올려 팔로워들에게 유익합니다.""",
    },
    {
        "query": "팔로워 수 대비 평균 좋아요 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워 수 대비 평균 좋아요 수가 높은 편으로 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 높은 평균 좋아요 수로 팔로워들의 관심을 받습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워 수 대비 평균 좋아요 수가 우수합니다.""",
    },
    {
        "query": "다양한 패션 브랜드와 협업 경험이 풍부한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 패션 브랜드와의 협업을 통해 신뢰를 쌓고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 브랜드와의 협업 경험이 많아 효과적으로 홍보할 수 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 패션 브랜드와 협업하여 많은 사랑을 받고 있습니다.""",
    },
    {
        "query": "댓글이 활발히 달리는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글 참여가 활발하여 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 댓글을 받고 있으며, 팔로워와의 관계를 중시합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 반응이 많아 활발한 소통을 이어가고 있습니다.""",
    },
    {
        "query": "뷰티 아이템을 주로 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 다양한 뷰티 아이템을 자주 소개하여 신뢰를 얻고 있습니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 뷰티 제품에 대한 리뷰가 많아 팔로워들에게 유익한 정보를 제공합니다.
---
influencer_id: 8
name: 권지현
reason: 뷰티 아이템을 자주 리뷰하고 많은 관심을 받고 있습니다.""",
    },
    {
        "query": "패션 콘텐츠에 집중하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 콘텐츠에 전문성을 가지고 있으며 다양한 스타일을 소개합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션에 특화된 콘텐츠로 많은 팔로워를 확보하고 있습니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 패션 콘텐츠에 집중하며 최신 트렌드를 잘 반영합니다.""",
    },
    {
        "query": "평균 댓글 수가 10개 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 평균 댓글 수가 높고, 다양한 반응을 이끌어내고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 댓글 참여가 활발하며, 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 12
name: 마르 Marr
reason: 제품 리뷰에서 항상 많은 댓글을 받습니다.""",
    },
    {
        "query": "남성 스킨케어제품을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 남성 스킨케어 제품을 자주 소개하며 실용적인 조언을 제공합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 스킨케어 제품에 대한 리뷰를 통해 신뢰를 쌓고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 남성 스킨케어 제품을 소개하고 실제 사용 경험을 공유합니다.""",
    },
    {
        "query": "최신 패션 트렌드를 자주 다루는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드를 자주 다루어 팔로워들에게 유익한 정보를 제공합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 트렌드를 이끄는 콘텐츠로 많은 사랑을 받고 있습니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 최신 트렌드에 맞춘 스타일링을 자주 소개하여 팔로워들의 관심을 끌고 있습니다.""",
    },
    {
        "query": "여름철 스킨케어 제품을 홍보할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 여름철 스킨케어 제품을 자주 리뷰하고 효과를 잘 설명합니다.
---
influencer_id: 8
name: 권지현
reason: 여름철 필수 스킨케어 제품을 잘 홍보하며, 피부 보호의 중요성을 강조합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 여름철 스킨케어 루틴에 대한 조언을 잘 제공합니다.""",
    },
    {
        "query": "남성 패션을 다루는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 남성 패션에 대한 깊은 이해를 바탕으로 다양한 스타일을 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 패션 아이템을 자주 소개하며 팔로워들의 관심을 끌고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 남성 팔로워와 소통하며 다양한 스타일을 공유합니다.""",
    },
    {
        "query": "평균 좋아요 수가 50 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 평균 좋아요 수가 150개 이상이며, 콘텐츠의 질이 높아 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 평균적으로 높은 좋아요 수를 기록하며 인기가 많습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 제품 리뷰에서 평균적으로 높은 좋아요 수를 유지합니다.""",
    },
    {
        "query": "팔로워 수가 많고 평균 댓글 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 14011명의 팔로워를 보유하고 있으며, 평균 댓글 수가 높습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 많은 팔로워와 함께 평균 댓글 수가 많아 소통이 활발합니다.
---
influencer_id: 8
name: 권지현
reason: 댓글 참여가 활발하며 평균적으로 많은 반응을 이끌어냅니다.""",
    },
    {
        "query": "피드백이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 이벤트에 적극적으로 참여하며 인기를 끌고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 팔로워의 피드백을 잘 반영하여 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 사용자 피드백에 신속하게 반응하여 좋은 관계를 유지합니다.""",
    },
    {
        "query": "패션 브랜드와의 협업 경험이 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 패션 브랜드와 협업을 진행하여 신뢰를 쌓고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션 브랜드와의 협업 경험이 많아 효과적으로 홍보할 수 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 패션 브랜드와의 협업을 통해 다양한 제품을 소개하고 있습니다.""",
    },
    {
        "query": "계절별 피부 관리 제품을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 계절별 피부 관리 제품을 효과적으로 소개하여 도움이 됩니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 계절에 맞는 스킨케어 제품을 자주 리뷰하여 유용한 정보를 제공합니다.
---
influencer_id: 8
name: 권지현
reason: 계절별로 적절한 피부 관리 제품을 추천하여 도움이 됩니다.""",
    },
    {
        "query": "높은 팔로워 수를 가진 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 14011명의 팔로워를 보유하고 있으며, 뷰티와 패션에 대한 신뢰도를 쌓고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 약 10100명의 팔로워를 보유하고 있으며, 뷰티 관련 콘텐츠에서 인기를 끌고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 높은 팔로워 수와 다양한 뷰티 제품 리뷰로 신뢰를 얻고 있습니다.""",
    },
    {
        "query": "신제품에 대한 리뷰가 빠른 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 신제품에 대한 리뷰를 빠르게 진행하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 새로운 제품을 신속하게 리뷰하고 소통하는 데 능숙합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 신제품에 대한 솔직한 리뷰를 자주 올려 팔로워들에게 유익합니다.""",
    },
    {
        "query": "팔로워 수 대비 평균 좋아요 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워 수 대비 평균 좋아요 수가 높은 편으로 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 높은 평균 좋아요 수로 팔로워들의 관심을 받습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워 수 대비 평균 좋아요 수가 우수합니다.""",
    },
    {
        "query": "다양한 패션 브랜드와 협업 경험이 풍부한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 패션 브랜드와의 협업을 통해 신뢰를 쌓고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 브랜드와의 협업 경험이 많아 효과적으로 홍보할 수 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 패션 브랜드와 협업하여 많은 사랑을 받고 있습니다.""",
    },
    {
        "query": "댓글이 활발히 달리는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글 참여가 활발하여 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 댓글을 받고 있으며, 팔로워와의 관계를 잘 유지합니다."""
   },
   {"query": "여름철 필수 뷰티 아이템을 잘 홍보할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 뷰티 아이템을 자주 홍보하며 효과적인 리뷰를 제공합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 여름철 뷰티 아이템을 잘 소개하고 사용 방법을 설명합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 필수 뷰티 아이템을 효과적으로 홍보합니다.""",
    },
    {
        "query": "여름 패션 아이템을 효과적으로 홍보할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름 패션 아이템을 잘 홍보하며 다양한 스타일을 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름철 트렌디한 아이템을 소개하여 팔로워들의 관심을 끌고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 여름 패션에 적합한 스타일을 자주 공유합니다.""",
    },
    {
        "query": "남성 스킨케어 제품을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 스킨케어 제품에 대한 리뷰를 통해 신뢰를 쌓고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 스킨케어에 대한 팁과 제품 리뷰를 자주 공유합니다.
---
influencer_id: 16
name: 민들레
reason: 남성 스킨케어 제품에 대한 관심이 높고, 관련 콘텐츠를 제공합니다.""",
    },
    {
        "query": "자연스러운 일상 사진으로 홍보를 잘하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 자연스러운 일상 사진으로 제품을 잘 홍보하며 신뢰를 얻고 있습니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 자연스러운 일상 속의 제품을 자주 소개하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 31
name: 지는빈
reason: 자연스러운 일상 사진을 통해 다양한 제품을 홍보합니다.""",
    },
    {
        "query": "피부 진정 크림을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 3
name: 코덕 오드리
reason: 피부 진정 크림을 자주 홍보하고 사용자 경험을 공유합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 진정 크림을 효과적으로 홍보하며, 사용 후기를 통해 신뢰를 높입니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 피부 진정 제품을 리뷰하여 효과를 설명합니다.""",
    },
    {
        "query": "뷰티 제품 리뷰에서 신뢰도를 높이는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 3
name: 코덕 오드리
reason: 신뢰할 수 있는 뷰티 제품 리뷰를 제공하여 팔로워들의 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 뷰티 제품에 대한 솔직한 리뷰로 신뢰를 쌓고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 뷰티 제품 리뷰에서 신뢰도가 높아 많은 팔로워들에게 사랑받고 있습니다.""",
    },
    {
        "query": "다양한 메이크업 제품을 잘 홍보하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 다양한 메이크업 제품을 잘 홍보하며 사용 팁을 제공합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 메이크업 제품에 대한 깊이 있는 리뷰를 제공하여 팔로워의 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 메이크업 제품을 다양하게 소개하고, 사용 후기를 공유합니다.""",
    },
    {
        "query": "반응 지수가 높은 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 뷰티 카테고리에서 반응이 활발하며 많은 참여를 이끌어냅니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 뷰티 제품 홍보에서 반응이 좋고 소통이 활발합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 뷰티 제품에 대한 높은 반응을 이끌어내고 있습니다.""",
    },
    {
        "query": "소통을 중요시하는 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워와의 소통을 중시하며 패션 아이템을 자연스럽게 소개합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 소통을 중요시하고, 패션과 관련된 다양한 조언을 제공합니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 팔로워와의 관계를 중시하며 소통을 자주 합니다.""",
    },
    {
        "query": "비건 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 7
name: 비건 라이프
reason: 비건 제품에 대한 정보와 사용기를 자주 공유하여 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 비건 뷰티 제품을 자주 리뷰하여 소비자에게 효과적으로 전달합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 비건 스킨케어 제품에 대한 솔직한 리뷰를 제공합니다.""",
    },
    {
        "query": "가성비 좋은 뷰티 제품을 소개할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 가성비 좋은 뷰티 제품을 자주 리뷰하고 효과를 설명합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 다양한 저가형 뷰티 제품을 소개하여 소비자들에게 호평을 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 가성비 좋은 제품을 실용적으로 소개하여 인기를 끌고 있습니다.""",
    },
    {
        "query": "겨울철 필수 스킨케어 제품을 잘 홍보할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 겨울철 필수 스킨케어 제품을 잘 홍보하며, 사용 후기를 바탕으로 신뢰를 줍니다.
---
influencer_id: 8
name: 권지현
reason: 겨울철 보습 제품을 잘 소개하고 효과를 설명합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 겨울철 피부 관리에 대한 조언을 잘 제공합니다.""",
    },
    {
        "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글 참여가 활발하여 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 댓글을 받고 있으며, 팔로워와의 관계를 중시합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 반응이 많아 활발한 소통을 이어가고 있습니다.""",
    },
    {
        "query": "다양한 장소에서 찍은 여행 사진을 잘 홍보하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 14
name: 솔솔씨
reason: 다양한 장소에서 찍은 여행 사진을 잘 홍보하고, 관련된 콘텐츠에 특화되어 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여행지에서 찍은 사진을 자주 공유하며 자연스럽게 홍보합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 장소에서 촬영한 콘텐츠로 여행의 매력을 잘 전달합니다.""",
    },
    {
        "query": "가성비 좋은 스킨케어 제품을 주로 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 가성비 좋은 스킨케어 제품을 자주 리뷰하고 효과를 설명합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 저렴한 가격의 스킨케어 제품을 효과적으로 홍보합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 다양한 저가형 스킨케어 제품을 소개하여 소비자들에게 호평을 받고 있습니다.""",
    },
    {
        "query": "피부 타입별 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 피부 타입별 스킨케어 루틴을 효과적으로 설명하여 많은 도움이 됩니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 각 피부 타입에 맞는 스킨케어 제품 추천을 잘합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 피부 타입에 따른 맞춤형 스킨케어 팁을 제공합니다.""",
    },
    {
        "query": "이벤트 참여가 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 이벤트에 적극적으로 참여하며 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 관련 이벤트에 자주 참여하여 트렌드를 선도합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 각종 뷰티 및 패션 이벤트에 참여하여 활발한 활동을 보이고 있습니다.""",
    },
    {
        "query": "평소 피드백을 잘 반영하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워의 피드백을 잘 반영하여 신뢰를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 피드백에 대한 반응이 좋고, 팔로워와의 관계를 중시합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 사용자 피드백에 신속하게 반응하여 좋은 관계를 유지합니다.""",
    },
    {
        "query": "패션 트렌드를 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 트렌드를 잘 반영하여 팔로워들에게 최신 정보를 제공합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 최신 패션 트렌드를 자주 소개하여 팔로워들에게 인기가 많습니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 다양한 패션 트렌드를 자주 다루어 많은 사랑을 받고 있습니다.""",
    },
    {
        "query": "여름철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수품을 효과적으로 소개하며, 다양한 제품에 대한 정보를 공유합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 여름철 필수 아이템을 자주 소개하고 신뢰도를 높이고 있습니다.
---
influencer_id: 8
name: 권지현
reason: 여름철 필수 아이템을 잘 홍보하며 신뢰를 얻고 있습니다.""",
    },
    {
        "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 소통이 활발하며 뷰티 제품을 자연스럽게 소개하는 데 능숙합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 팔로워와의 소통을 중요시하여 신뢰를 쌓고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 관계를 중시하며 소통을 자주 합니다.""",
    },
    {
        "query": "학생층 팔로워가 많은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 스타일과 저렴한 가격의 제품을 자주 소개하여 학생들에게 인기가 많습니다.
---
influencer_id: 1
name: 코덕❤
reason: 학생들이 선호하는 뷰티 제품과 팁을 자주 공유하여 신뢰를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 학생층이 선호하는 다양한 제품 리뷰를 제공하여 많은 사랑을 받고 있습니다.""",
    },
    {
        "query": "신제품 리뷰가 빠른 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 신제품에 대한 리뷰를 빠르게 진행하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 새로운 제품을 신속하게 리뷰하고 소통하는 데 능숙합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 신제품에 대한 솔직한 리뷰를 자주 올려 팔로워들에게 유익합니다.""",
    },
    {
        "query": "평균 좋아요 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 평균 좋아요 수가 높고, 콘텐츠의 질이 우수합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 평균적으로 높은 좋아요 수를 기록하며 인기가 많습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 제품 홍보에서 평균 좋아요 수가 높은 편입니다.""",
    },
    {
        "query": "겨울철 보습 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 겨울철 보습 제품을 잘 홍보하며, 사용 후기를 바탕으로 신뢰를 줍니다.
---
influencer_id: 8
name: 권지현
reason: 겨울철 필수 보습 제품을 잘 소개하고 효과를 설명합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 겨울철 피부 관리에 대한 조언을 잘 제공합니다.""",
    },
    {
        "query": "각종 이벤트에 참여하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 이벤트에 적극적으로 참여하며 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 관련 이벤트에 자주 참여하여 트렌드를 선도합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 각종 뷰티 및 패션 이벤트에 참여하여 활발한 활동을 보이고 있습니다.""",
    },
    {
        "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글 참여가 활발하여 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 댓글을 받고 있으며, 팔로워와의 관계를 중시합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 반응이 많아 활발한 소통을 이어가고 있습니다.""",
    },
    {
        "query": "소통이 활발한 여행 인플루언서를 추천해줘.",
        "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 다양한 여행 경험을 공유하며 팔로워와의 소통이 활발합니다.
---
influencer_id: 14
name: 예아린
reason: 여행지에서의 일상과 경험을 자주 공유하여 소통이 원활합니다.
---
influencer_id: 31
name: 지는빈
reason: 여행 관련 콘텐츠에서 팔로워와 소통하며 활발한 활동을 이어가고 있습니다.""",
    },
    {
        "query": "팔로워 수가 5000명 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 14011명의 팔로워를 보유하고 있어 영향력이 큽니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 약 10100명의 팔로워를 보유하고 있으며, 뷰티 관련 콘텐츠에서 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 높은 팔로워 수와 함께 뷰티 제품 리뷰에서 많은 신뢰를 얻고 있습니다.""",
    },
    {
        "query": "뷰티 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 3
name: 코덕 오드리
reason: 다양한 뷰티 제품에 대한 깊이 있는 리뷰를 제공하여 팔로워의 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 뷰티 제품 홍보에서 적극적으로 활동하며 사용자 경험을 공유합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 효과적인 뷰티 제품 리뷰로 많은 사랑을 받고 있습니다.""",
    },
    {
        "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 3
name: 코덕 오드리
reason: 스킨케어 제품에 대한 신뢰도 높은 리뷰를 제공하여 팔로워의 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 스킨케어 제품에 대한 솔직한 리뷰로 신뢰를 쌓고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 스킨케어 제품을 실용적으로 소개하여 신뢰를 얻고 있습니다.""",
    },
    {
        "query": "평균 댓글 수가 10개 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 평균 댓글 수가 높고, 다양한 반응을 이끌어내고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 댓글 참여가 활발하며, 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 제품 리뷰에서 항상 많은 댓글을 받습니다.""",
    },
    {
        "query": "가성비 좋은 패션 아이템을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 가성비 좋은 패션 아이템을 자주 소개하여 인기를 끌고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 저렴한 가격의 패션 아이템을 실용적으로 소개하여 많은 사랑을 받고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 아이템을 소개하며 가격 대비 좋은 제품을 추천합니다.""",
    },
    {
        "query": "각종 뷰티 이벤트에 참여하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 이벤트에 적극적으로 참여하여 인기를 끌고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 이벤트에 자주 참여하여 트렌드를 선도합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 각종 뷰티 및 패션 이벤트에 참여하여 활발한 활동을 보이고 있습니다.""",
    },
    {
        "query": "트렌디한 패션을 주로 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 트렌디한 패션 아이템을 자주 소개하며 최신 스타일을 반영합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 트렌디한 패션 아이템을 잘 소개하여 팔로워들에게 인기가 많습니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 트렌디한 패션을 잘 소개하며 팔로워의 관심을 끌고 있습니다.""",
    },
    {
        "query": "다양한 뷰티 브랜드와 협업 경험이 풍부한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 패션 브랜드와 협업을 진행하여 신뢰를 쌓고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 뷰티 브랜드와 협업 경험이 많아 효과적으로 홍보할 수 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 뷰티 브랜드와 협업하여 많은 사랑을 받고 있습니다.""",
    },
    {
        "query": "반응이 활발한 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 콘텐츠의 반응 지수가 높고 참여도가 우수합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 높은 반응 지수로 패션 트렌드를 잘 전달합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 패션 브랜드와의 협업을 통해 좋은 반응을 이끌어냅니다.""",
    },
    {
        "query": "가성비 좋은 뷰티 제품을 주로 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 가성비 좋은 뷰티 제품을 자주 리뷰하고 효과를 설명합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 다양한 저가형 뷰티 제품을 소개하여 소비자들에게 호평을 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 가성비 좋은 제품을 실용적으로 소개하여 인기를 끌고 있습니다.""",
    },
    {
        "query": "소통을 중시하는 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워와의 소통을 중요시하며 제품을 자연스럽게 소개합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 소통을 잘하며 팔로워와의 관계를 소중히 여깁니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 관계를 중시하며 소통을 자주 합니다.""",
    },
    {
        "query": "여행지에서 찍은 사진을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 여행지에서 찍은 사진을 공유하여 홍보에 적합합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여행 콘텐츠에서 패션 아이템을 잘 홍보합니다.
---
influencer_id: 14
name: 예아린
reason: 여행지에서의 일상과 경험을 자주 공유하여 소통이 원활합니다.""",
    },
    {
        "query": "겨울철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수품을 효과적으로 소개하며, 다양한 제품에 대한 정보를 공유합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 겨울철 필수 아이템을 자주 소개하고 신뢰도를높이고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 겨울철 필수품을 잘 홍보하며 사용 팁을 제공합니다.""",
    },
    {
        "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워와의 소통을 중요시하며 뷰티 제품을 자연스럽게 소개합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 팔로워와의 관계를 소중히 여기고 적극적으로 소통합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 관계를 중시하며 소통을 자주 합니다.""",
    },
    {
        "query": "팔로워 수가 많고 소통이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 14011명의 팔로워를 보유하고 있으며, 댓글 참여가 활발합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 약 10100명의 팔로워를 보유하고 있으며, 소통이 원활하여 인기가 많습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 높은 팔로워 수와 함께 댓글 반응이 많아 소통이 활발합니다.""",
    },
    {
        "query": "신제품 리뷰를 자주 올리는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 신제품에 대한 리뷰를 빠르게 진행하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 신제품 리뷰를 자주 올려 팔로워들에게 유익한 정보를 제공합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 신제품을 빠르게 리뷰하여 신뢰를 얻고 있습니다.""",
    },
    {
        "query": "패션 아이템을 주로 추천하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 아이템에 대한 깊은 이해를 바탕으로 다양한 스타일을 추천합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션 아이템을 자주 추천하며 최신 트렌드를 반영합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 패션 아이템에 대한 추천이 많고, 팔로워의 반응이 좋습니다.""",
    },
    {
        "query": "피부 진정 크림을 효과적으로 홍보할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 피부 진정 제품에 대한 경험을 공유하며 신뢰를 높입니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 피부 진정 크림을 효과적으로 사용하여 좋은 후기를 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 피부 진정 제품을 리뷰하여 효과를 설명합니다.""",
    },
    {
        "query": "학생층 팔로워가 많이 따르는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 스타일과 저렴한 가격의 제품을 자주 소개하여 학생들에게 인기가 많습니다.
---
influencer_id: 1
name: 코덕❤
reason: 학생들이 선호하는 뷰티 제품과 팁을 자주 공유하여 신뢰를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 학생층이 선호하는 다양한 제품 리뷰를 제공하여 많은 사랑을 받고 있습니다.""",
    },
    {
        "query": "여름철 필수 아이템을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 아이템을 자주 소개하고, 효과적인 팁을 제공합니다.
---
influencer_id: 8
name: 권지현
reason: 여름철 필수품을 잘 홍보하며 사용자 경험을 공유합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 여름철 필수 아이템을 효과적으로 소개하여 팔로워에게 유용한 정보를 제공합니다.""",
    },
    {
        "query": "신제품에 대한 리뷰가 빠른 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 신제품에 대한 리뷰를 빠르게 진행하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 신제품 리뷰를 자주 올려 팔로워들에게 유익한 정보를 제공합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 신제품을 빠르게 리뷰하여 신뢰를 얻고 있습니다.""",
    },
    {
        "query": "겨울철 필수품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 겨울철 필수품을 잘 홍보하며 사용 후기를 바탕으로 신뢰를 줍니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수 아이템을 자주 소개하고 효과를 설명합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 겨울철 피부 관리에 대한 조언을 잘 제공합니다.""",
    },
    {
        "query": "다양한 메이크업 스타일을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 다양한 메이크업 스타일을 자주 소개하며 많은 사랑을 받고 있습니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 메이크업 스타일과 팁을 공유하여 팔로워들에게 유익한 정보를 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 메이크업 제품을 소개하고 사용 후기를 공유합니다.""",
    },
    {
        "query": "남성 팔로워가 많이 따르는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 팔로워에게 많은 인기를 끌고 있는 패션 인플루언서입니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션에 대한 깊은 이해를 바탕으로 다양한 스타일을 소개합니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 다양한 남성 패션을 소개하며 팔로워들에게 인기를 얻고 있습니다.""",
    },
    {
        "query": "반응 지수가 높은 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 뷰티 카테고리에서 반응이 활발하며 많은 참여를 이끌어냅니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 뷰티 제품 홍보에서 반응이 좋고 소통이 활발합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 뷰티 제품에 대한 높은 반응을 이끌어내고 있습니다.""",
    },
    {
        "query": "일상 제품을 자주 리뷰하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 일상에서 사용한 제품을 자주 리뷰하여 팔로워에게 신뢰를 얻고 있습니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 일상 속의 제품을 자주 소개하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 31
name: 지는빈
reason: 자연스러운 일상 사진을 통해 다양한 제품을 홍보합니다.""",
    },
    {
        "query": "이벤트 참여가 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 이벤트에 적극적으로 참여하며 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 관련 이벤트에 자주 참여하여 트렌드를 선도합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 각종 뷰티 및 패션 이벤트에 참여하여 활발한 활동을 보이고 있습니다.""",
    },
    {
        "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글 참여가 활발하여 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 댓글을 받고 있으며, 팔로워와의 관계를 중시합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 반응이 많아 활발한 소통을 이어가고 있습니다.""",
    },
    {
        "query": "패션 아이템을 주로 추천하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 아이템에 대한 깊은 이해를 바탕으로 다양한 스타일을 추천합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션 아이템을 자주 추천하며 최신 트렌드를 반영합니다.
---
influencer_id: 6
name: 데일리룩 패션 / 한정우
reason: 패션 아이템에 대한 추천이 많고, 팔로워의 반응이 좋습니다.""",
    },
    {
        "query": "소통을 중시하는 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워와의 소통을 중요시하며 제품을 자연스럽게 소개합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 소통을 잘하며 팔로워와의 관계를 소중히 여깁니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 관계를 중시하며 소통을 자주 합니다.""",
    },
    {
        "query": "다양한 패션 스타일을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션 스타일을 자주 소개하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 스타일을 반영한 콘텐츠로 많은 사랑을 받고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 스타일에 대한 깊은 이해를 바탕으로 다양한 스타일을 소개합니다.""",
    },
    {
        "query": "팔로워 수가 많고 평균 좋아요 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 14011명의 팔로워를 보유하고 있으며, 평균 좋아요 수가 높습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 약 10100명의 팔로워를 보유하고 있으며, 높은 평균 좋아요 수를 기록합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 많은 댓글과 좋아요를 받아 반응이 좋은 인플루언서입니다.""",
    },
    {
        "query": "피드백 반영이 빠르고 신뢰도가 높은 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워의 피드백을 빠르게 반영하여 신뢰를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 피드백에 적극적으로 반응하여 팔로워와의 관계를 유지합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 사용자 피드백을 빠르게 반영하며 제품 리뷰에 신뢰도를 더합니다.""",
    },
    {
        "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글 참여가 활발하여 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 다양한 댓글을 받고 있으며, 팔로워와의 관계를 중시합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 반응이 많아 활발한 소통을 이어가고 있습니다.""",
    },
    {
        "query": "자연스러운 일상 사진으로 홍보를 잘하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 자연스러운 일상 사진으로 제품을 잘 홍보하며 신뢰를 얻고 있습니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 자연스러운 일상 속의 제품을 자주 소개하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 31
name: 지는빈
reason: 자연스러운 일상 사진을 통해 다양한 제품을 홍보합니다.""",
    },
    {
        "query": "여름철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수품을 효과적으로 소개하며, 다양한 제품에 대한 정보를 공유합니다.
---
influencer_id: 3
name: 코덕 오드리
reason: 여름철 필수 아이템을 자주 소개하고 신뢰도를 높이고 있습니다.
---
influencer_id: 8
name: 권지현
reason: 여름철 필수 아이템을 잘 홍보하여 신뢰를 얻고 있습니다.""",
    },
    {
        "query": "반응 지수가 높은 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 콘텐츠의 반응 지수가 높고 참여도가 우수합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 높은 반응 지수로 패션 트렌드를 잘 전달합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 패션 브랜드와의 협업을 통해 좋은 반응을 이끌어냅니다.""",
    }, {
        "query": "신제품 리뷰가 빠르고 반응이 좋은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 오드리
reason: 신제품 리뷰를 자주 올리며, 반응이 매우 좋습니다. 팔로워와의 소통도 활발하여 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 신제품에 대한 리뷰를 빠르게 올리며 반응이 좋습니다. 팔로워들의 반응도 긍정적입니다.
---
influencer_id: 12
name: 마르 Marr
reason: 신제품 리뷰가 빠르고 팔로워의 반응이 좋은 편입니다. 신뢰도를 높이고 있습니다.""",
    },
    {
        "query": "다양한 뷰티 브랜드와의 협업이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 오드리
reason: 여러 뷰티 브랜드와 협업을 통해 다양한 제품을 소개하며 인지도를 높이고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 브랜드와 협업하여 제품 리뷰를 진행하며 팔로워와의 소통도 활발합니다.
---
influencer_id: 34
name: Niya 김반야
reason: 여러 뷰티 브랜드와 협업을 통해 다양한 콘텐츠를 제공하며 반응이 좋습니다.""",
    },
    {
        "query": "팔로워와의 소통이 원활한 남성 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 팔로워와의 소통을 중시하며 다양한 패션 스타일을 소개합니다. 남성 팔로워와의 소통이 활발합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 피드백을 잘 반영하며 남성 패션 아이템에 대한 정보가 많습니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 소통이 원활하여 남성 팔로워와의 관계를 잘 유지하고 있습니다.""",
    },
    {
        "query": "트렌디한 아이템을 자주 소개하는 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 트렌디한 뷰티 아이템을 꾸준히 소개하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 최신 뷰티 트렌드를 반영하여 다양한 제품을 소개합니다. 팔로워와의 소통이 활발합니다.
---
influencer_id: 1
name: 코덕❤
reason: 트렌디한 뷰티 아이템을 자주 추천하여 팔로워들에게 인기가 많습니다.""",
    },
    {
        "query": "피부 진정 크림을 효과적으로 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 피부 진정 제품을 자주 소개하며 팔로워들에게 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 피부 진정 관련 제품에 대한 정보가 많고, 리뷰도 신뢰성이 높습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 피부 진정 크림에 대한 이해가 깊고, 실제 사용 사례를 잘 보여줍니다.""",
    },
  {
        "query": "남성 팔로워가 많은 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 팔로워를 대상으로 다양한 뷰티 제품을 소개합니다. 트렌디한 콘텐츠가 많습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션과 뷰티 제품을 자주 소개하여 남성 팔로워와의 소통이 활발합니다.
---
influencer_id: 36
name: 권지현
reason: 남성 팔로워들이 많이 따르는 뷰티 콘텐츠를 제작합니다.""",
    },
    {
        "query": "다양한 장소에서 찍은 일상 사진이 인상적인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 다양한 장소에서 찍은 일상 사진으로 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 장소에서의 패션을 자연스럽게 보여주며 일상 사진이 인상적입니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 장소에서의 일상 모습을 공유하여 팔로워와의 관계를 유지합니다.""",
    },
  {
        "query": "평균 좋아요가 300개 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 평균 좋아요 수가 300개 이상으로 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 많은 좋아요를 받으며 팔로워의 반응이 우수합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 평균 좋아요 수가 높아 제품 홍보에 효과적입니다.""",
    },
    {
        "query": "자연스러운 패션 스타일링을 자주 보여주는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 자연스러운 스타일링으로 패션 아이템을 잘 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 스타일을 자연스럽게 표현하여 팔로워의 흥미를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 자연스러운 패션 스타일링으로 많은 팔로워의 사랑을 받고 있습니다.""",
    },
 {
        "query": "좋아요 수가 많고 팔로워의 반응이 좋은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 좋아요 수와 댓글 반응이 모두 높은 인플루언서입니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 많은 좋아요를 받으며 팔로워와의 소통이 활발합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 반응이 좋고 다양한 피드백을 잘 반영합니다.""",
    },
    {
        "query": "패션 트렌드를 자주 소개하는 남성 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션 트렌드를 꾸준히 소개하며 많은 사랑을 받고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 트렌디한 남성 패션 아이템을 자주 소개하여 반응이 좋습니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 남성 트렌드를 자주 다룹니다.""",
    },
 {
        "query": "계절별 제품을 효과적으로 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 오드리
reason: 계절별로 적절한 제품을 소개하여 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 계절에 맞는 뷰티 제품을 잘 소개하여 반응이 좋습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 계절별로 트렌디한 제품을 자주 소개합니다.""",
    },
{
        "query": "팔로워 수가 많고 소통이 원활한 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 많은 팔로워와 활발한 소통을 유지하고 있습니다."""
},
 {
        "query": "팔로워 수가 많고 소통이 원활한 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 많은 팔로워와 활발한 소통을 유지하고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 팔로워와의 소통을 중요시하며 다양한 패션 아이템을 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 많은 팔로워와의 관계를 유지하며 패션 트렌드를 잘 반영합니다."""
    },
    {
        "query": "소통이 활발하고, 평균 댓글 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 평균 댓글 수가 높고, 팔로워와의 소통이 활발하여 신뢰를 얻고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글 참여율이 높아 소통이 활발합니다. 다양한 피드백을 반영합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 댓글 수가 많고 소통이 활발하여 반응이 좋습니다."""
    },
    {
        "query": "반응 지수가 높은 일상 카테고리 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 일상 카테고리에서 반응 지수가 높아 인기가 많습니다.
---
influencer_id: 31
name: 지는빈
reason: 일상 콘텐츠에 대한 반응이 좋고, 팔로워와의 소통이 활발합니다.
---
influencer_id: 33
name: 김윤지 (YUN JI)
reason: 다양한 일상 콘텐츠를 제공하여 많은 반응을 얻고 있습니다."""
    },
    {
        "query": "남성 패션 아이템을 자주 홍보하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션 아이템을 주로 소개하며 팔로워의 반응이 좋습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 패션을 효과적으로 홍보하여 많은 관심을 받고 있습니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 다양한 남성 패션 스타일을 소개하며 반응이 활발합니다."""
    },
    {
        "query": "소통이 활발한 여행 인플루언서를 추천해줘.",
        "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 여행 관련 콘텐츠에서 팔로워와의 소통이 활발합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여행지에서의 일상 콘텐츠를 공유하여 소통이 원활합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 여행과 관련된 리뷰를 통해 팔로워와 소통을 잘합니다."""
    },
    {
        "query": "비건 스킨케어 제품을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 오드리
reason: 비건 스킨케어 제품에 대한 리뷰를 자주 올리며 반응이 좋습니다.
---
influencer_id: 34
name: Niya 김반야
reason: 비건 뷰티 제품을 주로 사용하는 인플루언서로 신뢰도가 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 비건 스킨케어 제품에 대한 정보를 제공합니다."""
    },
    {
        "query": "남성 패션 브랜드와 협업 경험이 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 여러 남성 패션 브랜드와 협업을 통해 다양한 콘텐츠를 제공합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 패션 관련 협업을 진행하며 많은 피드백을 얻고 있습니다.
---
influencer_id: 39
name: 솔솔씨
reason: 다양한 남성 패션 브랜드와 협업하여 패션 아이템을 소개합니다."""
    },
    {
        "query": "뷰티 리뷰를 자주 작성하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 오드리
reason: 자주 뷰티 리뷰를 작성하며 신뢰성을 높이고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 제품에 대한 상세한 리뷰를 제공합니다.
---
influencer_id: 1
name: 코덕❤
reason: 뷰티 제품 리뷰가 많아 팔로워의 신뢰를 얻고 있습니다."""
    },
    {
        "query": "평균 좋아요가 50개 이상인 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 8
name: 권지현
reason: 평균 좋아요 수가 높아 제품 홍보에 효과적입니다.
---
influencer_id: 12
name: 마르 Marr
reason: 평균 좋아요가 높은 리뷰를 작성하여 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 많은 좋아요를 얻으며 팔로워와의 소통도 활발합니다."""
    },
    {
        "query": "학생층 팔로워를 타깃으로 하는 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 학생층에게 인기가 많은 패션 콘텐츠를 제공합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 다양한 학생층을 겨냥한 스타일링을 자주 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 학생들에게 적합한 패션을 자주 추천합니다."""
    },
    {
        "query": "댓글 참여율이 높고 소통이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 참여율이 높고 팔로워와의 소통이 매우 활발합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글과 좋아요 반응이 좋은 인플루언서입니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 소통이 활발하고 피드백을 잘 반영합니다."""
    },
    {
        "query": "댓글과 좋아요 반응이 좋은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 오드리
reason: 댓글과 좋아요 수가 모두 높은 편이며 반응이 좋습니다.
---
influencer_id: 8
name: 권지현
reason: 활발한 댓글과 좋아요로 팔로워의 반응이 우수합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 많은 좋아요와 댓글로 팔로워와의 소통이 활발합니다."""
    },
    {
        "query": "새로운 패션 브랜드와 자주 협업하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 다양한 새로운 패션 브랜드와 협업하며 많은 피드백을 얻고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여러 패션 브랜드와 협업하여 새로운 콘텐츠를 제작합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 새로운 브랜드와의 협업을 통해 트렌디한 콘텐츠를 제공합니다."""
    },
    {
        "query": "좋아요 수가 꾸준히 높은 남성 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션 아이템을 소개하며 평균 좋아요 수가 높은 편입니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 꾸준한 좋아요 수를 기록하고 있습니다."""
},{
        "query": "좋아요 수가 꾸준히 높은 남성 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션 아이템을 소개하며 평균 좋아요 수가 높은 편입니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 꾸준한 좋아요 수를 기록하고 있습니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 꾸준히 높은 반응을 얻으며 팔로워와의 소통이 활발합니다."""
    },
    {
        "query": "패션 잡지를 참고한 스타일을 자주 보여주는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 잡지를 참고하여 트렌디한 스타일을 자주 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 매거진에서 영감을 받아 스타일링을 공유합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 잡지를 통해 다양한 스타일을 자주 선보입니다."""
    },
    {
        "query": "평균 댓글 수가 7개 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 평균 댓글 수가 7개 이상으로 소통이 활발합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 댓글 참여율이 높고 팔로워의 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글 수가 많아 팔로워와의 소통이 활발합니다."""
    },
    {
        "query": "다양한 스킨케어 제품을 꾸준히 리뷰하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 오드리
reason: 다양한 스킨케어 제품에 대한 리뷰를 자주 올리며 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 스킨케어 제품 리뷰를 자주 하며 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 꾸준히 스킨케어 제품을 리뷰하여 많은 피드백을 받고 있습니다."""
    },
    {
        "query": "친환경 제품을 주로 사용하는 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 39
name: 솔솔씨
reason: 친환경 패션 아이템을 주로 사용하며 인기를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 친환경 브랜드와 협업하여 신뢰를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 친환경 뷰티 제품을 적극적으로 소개합니다."""
    },
    {
        "query": "팔로워 1만 명 이상이며 소통이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 팔로워 수가 많고 소통이 활발하여 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 많은 팔로워와의 소통을 중요시하며 다양한 콘텐츠를 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 소통이 원활하며 리뷰가 많이 이루어집니다."""
    },
    {
        "query": "피드백을 자주 반영하며 제품 설명이 상세한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피드백을 잘 반영하며 제품에 대한 설명이 상세합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 리뷰가 신뢰성이 높고 피드백을 잘 반영합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 상세한 제품 설명으로 팔로워의 신뢰를 얻고 있습니다."""
    },
    {
        "query": "계절별로 패션 스타일링을 제공하는 남성 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 계절에 맞는 남성 패션 아이템을 잘 소개하여 반응이 좋습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 계절별로 스타일링을 자주 제공하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 시즌에 맞는 패션을 자주 선보이며 인기를 얻고 있습니다."""
    },
    {
        "query": "최신 스킨케어 제품을 빠르게 리뷰하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 오드리
reason: 신제품에 대한 리뷰를 빠르게 올리며 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 새로운 스킨케어 제품을 자주 리뷰하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 최신 제품을 빠르게 리뷰하여 신뢰도를 높이고 있습니다."""
    },
    {
        "query": "친근한 소통을 중시하며 제품 리뷰가 자세한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 친근하게 소통하며 상세한 리뷰로 팔로워와의 관계를 유지하고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 제품에 대한 이해도가 높고 소통이 활발합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 리뷰가 자세하고 소통이 원활하여 인기가 많습니다."""
    },
    {
        "query": "팔로워 수가 많고 좋아요 반응이 꾸준히 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 팔로워 수가 많고, 평균 좋아요 수가 꾸준히 높습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 많은 팔로워와 높은 좋아요 수로 신뢰를 얻고 있습니다.
---
influencer_id: 8
name: 권지현
reason: 반응이 좋고 팔로워와의 소통이 활발합니다."""
    },
    {
        "query": "가성비 좋은 일상용 제품을 주로 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 가성비 좋은 일상용 제품을 자주 추천하며 반응이 좋습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 가성비 제품을 소개하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 가성비 좋은 뷰티 아이템에 대한 리뷰가 많아 인기가 높습니다."""
    },
    {
        "query": "학생들이 자주 참고하는 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 학생층에게 인기가 많은 뷰티 콘텐츠를 제공합니다.
---
influencer_id: 10
name: 코덕 오드리
reason: 학생들이 많이 찾는 뷰티 리뷰를 자주 게시합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 학생들에게 적합한 뷰티 정보를 많이 제공합니다."""
    },
    {
        "query": "여름철 필수 뷰티 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 오드리
reason: 여름철 뷰티 제품을 효과적으로 홍보하며 반응이 좋습니다."""
},
 {
        "query": "여름철 필수 뷰티 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 뷰티 제품에 대한 리뷰가 많아 팔로워들의 신뢰를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여름철 뷰티 제품을 효과적으로 홍보하며 활발한 소통이 가능합니다.
---
influencer_id: 8
name: 권지현
reason: 여름철 스킨케어 제품을 자주 소개하여 관심을 끌고 있습니다."""
    },
    {
        "query": "다양한 뷰티 브랜드와 협업 경험이 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여러 뷰티 브랜드와 협업하여 다양한 제품을 소개하고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 뷰티 브랜드와의 협업을 통해 팔로워들에게 인기가 많습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 뷰티 브랜드와 협업을 통해 신뢰를 얻고 있습니다."""
    },
    {
        "query": "학생층 팔로워를 타깃으로 하는 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 학생들에게 인기가 많고 그들의 관심을 끌 수 있는 콘텐츠를 제공합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 학생층을 겨냥한 뷰티 제품과 팁을 자주 소개합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 학생들이 선호하는 제품을 효과적으로 소개합니다."""
    },
    {
        "query": "비건 스킨케어 제품을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 비건 스킨케어 제품에 대한 리뷰를 자주 올리며 긍정적인 반응을 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 비건 제품을 주로 사용하여 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 비건 뷰티 제품을 소개하며 반응이 좋습니다."""
    },
    {
        "query": "신제품 리뷰가 빠르고 반응이 좋은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 신제품에 대한 리뷰를 자주 올리며 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 신제품에 대한 리뷰가 빠르고 팔로워의 반응도 긍정적입니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 신제품 리뷰를 통해 많은 팔로워와의 소통이 활발합니다."""
    },
    {
        "query": "여름철 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 스킨케어 루틴에 대한 설명이 상세하며 유용합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여름철 피부 관리에 대한 팁과 제품 추천이 유익합니다.
---
influencer_id: 8
name: 권지현
reason: 여름철 스킨케어 루틴을 잘 소개하여 많은 관심을 받고 있습니다."""
    },
    {
        "query": "여행을 자주 다니는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 여행지를 방문하며 관련 콘텐츠를 자주 올립니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 여행지에서의 일상 모습을 공유하며 반응이 좋습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 여행과 관련된 다양한 경험을 공유하여 팔로워와 소통합니다."""
    },
    {
        "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글과 DM을 통해 팔로워와의 소통이 활발합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 소통을 중요시하며 팔로워와의 관계를 잘 유지합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 활발한 소통을 통해 팔로워와의 관계를 강화하고 있습니다."""
    },
    {
        "query": "가성비 좋은 뷰티 아이템을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 가성비 좋은 뷰티 제품에 대한 정보를 자주 공유합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 가성비 좋은 제품을 중심으로 리뷰를 진행하여 많은 호응을 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 가성비 제품을 소개하여 많은 팔로워에게 인기를 끌고 있습니다."""
    },
    {
        "query": "여름철 패션 아이템을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름철 패션 아이템을 잘 소화하여 홍보 효과가 높습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름철 패션을 다양하게 소개하여 반응이 좋습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 여름철 필수 패션 아이템을 주로 소개하여 팔로워와의 소통이 활발합니다."""
    },
    {
        "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 참여율이 높아 팔로워와의 소통이 원활합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 댓글 반응이 좋고 활발한 소통을 유지합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글 참여가 높고 팔로워와의 관계가 좋습니다."""
    },
    {
        "query": "피드백을 자주 반영하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 팔로워의 피드백을 잘 반영하며 리뷰를 진행합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피드백을 잘 반영하여 팔로워와의 신뢰를 쌓고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워의 의견을 소중히 여기며 콘텐츠를 개선합니다."""
    },
    {
        "query": "겨울철 필수 뷰티 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수 뷰티 제품을 잘 홍보하여 팔로워의 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 겨울철 뷰티 제품에 대한 이해도가 높고 리뷰가 상세합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 겨울철 스킨케어 제품을 자주 소개하여 신뢰를 얻고 있습니다."""
    },
{
        "query": "소통이 활발한 일상 카테고리 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 일상 관련 콘텐츠를 자주 올리며 소통이 활발합니다.
---
influencer_id: 31
name: 지는빈
reason: 일상적인 이야기를 통해 팔로워와의 소통을 잘 이어갑니다.
---
influencer_id: 33
name: 김윤지 (YUN JI)
reason: 일상적인 모습과 피드백을 반영하여 많은 팔로워와 소통합니다."""
    },
    {
        "query": "여행용 화장품을 주로 홍보하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여행 중 사용하는 화장품을 자주 소개하여 인기를 끌고 있습니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 여행 관련 콘텐츠에서 화장품을 효과적으로 홍보합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여행용 화장품 리뷰를 통해 팔로워의 관심을 끌고 있습니다."""
    },
    {
        "query": "피드백 반영이 빠르고 친절한 설명을 제공하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 피드백을 빠르게 반영하며 제품에 대한 설명이 친절합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워의 피드백을 소중히 여기고 상세한 설명을 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 친절하게 소통하며 제품에 대한 이해도를 높이고 있습니다."""
    },
    {
        "query": "팔로워 수 대비 평균 좋아요 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 팔로워 수에 비해 평균 좋아요 수가 높은 편입니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 많은 팔로워와 높은 좋아요 수로 반응이 좋습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워 수에 비해 평균 좋아요 수가 높아 신뢰를 얻고 있습니다."""
    },
    {
        "query": "계절에 맞는 일상 제품을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 계절에 맞는 일상 제품을 자주 소개하여 관심을 끌고 있습니다.
---
influencer_id: 31
name: 지는빈
reason: 계절별 제품 추천을 통해 팔로워의 반응이 좋습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 계절에 적합한 다양한 일상 제품을 소개하여 인기가 많습니다."""
    },
    {
        "query": "다양한 브랜드와 협업 경험이 풍부한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여러 브랜드와 협업하여 다양한 제품을 소개하고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 브랜드 협업을 통해 신뢰성을 높이고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 브랜드와 협업하여 폭넓은 제품을 다루고 있습니다."""
    },
    {
        "query": "학생층 팔로워에게 인기가 많은 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 학생층에게 인기가 많은 패션 콘텐츠를 제공합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 다양한 학생층을 겨냥한 스타일링을 자주 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 학생들에게 적합한 패션을 자주 추천하여 많은 사랑을 받고 있습니다."""
    },
    {
        "query": "평소 이벤트 참여가 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 다양한 이벤트에 적극적으로 참여하여 팔로워와의 소통을 강화하고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 이벤트에 자주 참여하여 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 이벤트 참여를 통해 팔로워와의 관계를 깊게 하고 있습니다."""
    },
    {
        "query": "트렌디한 일상 제품을 꾸준히 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 트렌디한 일상 제품을 자주 소개하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 31
name: 지는빈
reason: 트렌디한 제품을 지속적으로 소개하여 반응이 좋습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 트렌디한 제품을 자주 소개하여 팔로워의 반응이 좋습니다."""
    },
    {
        "query": "평균 댓글 수가 8개 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 평균 댓글 수가 8개 이상으로 팔로워와의 소통이 활발합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 댓글 참여율이 높아 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글 수가 많아 팔로워와의 관계가 좋습니다."""
    },
    {
        "query": "소통이 활발하고 팔로워의 피드백을 잘 반영하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 팔로워의 피드백을 잘 반영하며 소통이 활발합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 소통이 활발하여 피드백을 잘 반영합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 소통을 중요시하며 피드백을 반영하는 콘텐츠를 제공합니다."""
    },
    {
        "query": "남성 스킨케어 제품을 자주 리뷰하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 스킨케어 제품을 자주 리뷰하여 남성 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 스킨케어 제품에 대한 이해도가 높고 자주 리뷰를 진행합니다.
---
influencer_id: 36
name: 권지현
reason: 남성 스킨케어 제품 관련 콘텐츠를 소개하여 반응이 좋습니다."""
    },
    {
        "query": "여름 패션 브랜드와 협업한 경험이 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 여름 패션 브랜드와 협업을 통해 다양한 콘텐츠를 제공합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름 패션 브랜드와의 협업 경험이 많습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름 패션과 관련된 협업을 통해 인기를 끌고 있습니다."""
    },
    {
        "query": "겨울철 필수 뷰티 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수 뷰티 제품을 잘 홍보하여 팔로워의 반응이 좋습니다."""
},
 {
        "query": "겨울철 필수 뷰티 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수 뷰티 제품을 잘 홍보하여 팔로워의 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 겨울철 피부 관리에 대한 이해도가 높고 제품 추천이 상세합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 겨울철 스킨케어 제품을 자주 소개하여 신뢰를 얻고 있습니다."""
    },
    {
        "query": "가성비 좋은 패션 제품을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 가성비 좋은 패션 아이템을 자주 추천하여 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 가성비 좋은 패션 제품에 대한 정보도 자주 공유합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 다양한 가성비 패션 아이템을 소개하여 많은 사랑을 받고 있습니다."""
    },
    {
        "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 참여율이 높아 팔로워와의 소통이 원활합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 댓글 반응이 좋고 활발한 소통을 유지합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글 수가 많아 팔로워와의 관계가 좋습니다."""
    },
    {
        "query": "비건 스킨케어 제품을 자주 리뷰하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 비건 스킨케어 제품에 대한 리뷰를 자주 올리며 긍정적인 반응을 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 비건 제품을 주로 사용하여 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 비건 뷰티 제품을 소개하며 반응이 좋습니다."""
    },
    {
        "query": "자연스러운 일상 제품 리뷰가 인상적인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 자연스러운 일상 제품을 자주 리뷰하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 31
name: 지는빈
reason: 일상적인 제품을 자연스럽게 소개하여 반응이 좋습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 자연스러운 리뷰로 팔로워들에게 인기를 끌고 있습니다."""
    },
    {
        "query": "다양한 장소에서 찍은 일상 사진이 인상적인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 다양한 장소에서 찍은 사진으로 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여러 장소에서의 패션을 자연스럽게 보여주며 일상 사진이 인상적입니다.
---
influencer_id: 36
name: 권지현
reason: 다양한 장소에서 찍은 일상 사진으로 팔로워와 소통합니다."""
    },
    {
        "query": "겨울철 패션 아이템을 효과적으로 홍보할 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 겨울철 필수 패션 아이템을 잘 소화하여 홍보 효과가 높습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 겨울철 패션 아이템에 대한 정보가 많고 홍보가 효과적입니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 겨울철 패션을 다양하게 소개하여 반응이 좋습니다."""
    },
    {
        "query": "비건 및 자연 유래 제품을 사용하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 비건 및 자연 유래 제품을 사용하여 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 비건 화장품에 대한 정보가 많고 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 자연 유래 제품을 자주 리뷰하며 팔로워와의 신뢰를 쌓고 있습니다."""
    },
    {
        "query": "자연스럽게 패션 아이템을 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 자연스러운 스타일링으로 패션 아이템을 잘 소개합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 자연스럽게 패션 아이템을 보여주며 팔로워의 반응이 좋습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 자연스러운 패션 스타일을 자주 선보이며 인기를 끌고 있습니다."""
    },
    {
        "query": "여름철 필수 아이템을 잘 홍보하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 아이템을 효과적으로 홍보하여 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여름철 필수 아이템에 대한 정보를 자주 공유합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름철 패션과 뷰티 아이템을 다양하게 소개하여 팔로워의 반응이 좋습니다."""
    },
    {
        "query": "댓글과 좋아요 반응이 좋은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글과 좋아요 수가 모두 높은 편이며 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 많은 좋아요를 받으며 팔로워와의 소통이 활발합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글과 좋아요 반응이 모두 긍정적입니다."""
    },
    {
        "query": "소통이 활발한 일상 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 일상 관련 콘텐츠를 자주 올리며 소통이 활발합니다.
---
influencer_id: 31
name: 지는빈
reason: 일상적인 이야기를 통해 팔로워와의 소통을 잘 이어갑니다.
---
influencer_id: 33
name: 김윤지 (YUN JI)
reason: 다양한 일상 콘텐츠를 제공하여 많은 반응을 얻고 있습니다."""
    },
    {
        "query": "평균 댓글이 많고 반응이 좋은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 평균 댓글 수가 많고 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글 반응이 좋고 소통이 활발하여 인기가 많습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 댓글 수와 반응이 모두 긍정적입니다."""
    },


 {
        "query": "겨울철 패션 아이템을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 겨울철 패션 아이템을 잘 소개하여 팔로워의 반응이 좋습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 겨울철 패션 관련 정보가 많고 홍보가 효과적입니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 겨울철 스타일링을 다양하게 소개하여 많은 사랑을 받고 있습니다."""
    },
    {
        "query": "여름철 필수 뷰티 아이템을 효과적으로 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 뷰티 아이템에 대한 리뷰가 많아 팔로워들의 신뢰를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여름철 뷰티 제품을 효과적으로 홍보하며 활발한 소통이 가능합니다.
---
influencer_id: 8
name: 권지현
reason: 여름철 스킨케어 제품을 자주 소개하여 관심을 끌고 있습니다."""
    },
    {
        "query": "다양한 브랜드와 협업 경험이 풍부한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여러 브랜드와 협업하여 다양한 제품을 소개하고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 브랜드 협업을 통해 신뢰성을 높이고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 브랜드와 협업하여 폭넓은 제품을 다루고 있습니다."""
    },
    {
        "query": "신제품 반응이 좋은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 신제품에 대한 긍정적인 반응을 얻고 있으며 리뷰가 신뢰를 쌓고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 신제품을 빠르게 리뷰하여 많은 피드백을 받고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 신제품 리뷰가 빠르고 반응이 좋습니다."""
    },
    {
        "query": "평균 댓글 수가 10개 이상인 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 평균 댓글 수가 10개 이상으로 소통이 활발합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 댓글 참여율이 높아 반응이 좋습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 많은 댓글과 소통으로 팔로워와의 관계가 좋습니다."""
    },
    {
        "query": "겨울철 필수 뷰티 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수 뷰티 제품을 효과적으로 홍보하여 팔로워의 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 겨울철 스킨케어 제품에 대한 이해도가 높고, 리뷰가 상세합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 겨울철 스킨케어 제품을 자주 소개하여 신뢰를 얻고 있습니다."""
    },
    {
        "query": "댓글과 좋아요 반응이 좋은 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글과 좋아요 수가 모두 높은 편이며 반응이 좋습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 많은 좋아요를 받으며 팔로워와의 소통이 활발합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 댓글과 좋아요 반응이 모두 긍정적입니다."""
    },
    {
        "query": "소통이 활발한 여행 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여행 관련 콘텐츠에서 팔로워와의 소통이 활발합니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 여행지에서의 일상 모습을 공유하며 반응이 좋습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 여행과 관련된 다양한 경험을 공유하여 팔로워와 소통합니다."""
    },
    {
        "query": "팔로워와 일상 속 소통이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 일상적인 콘텐츠를 통해 팔로워와 소통이 활발합니다.
---
influencer_id: 31
name: 지는빈
reason: 일상적인 이야기를 통해 팔로워와의 소통을 잘 이어갑니다.
---
influencer_id: 33
name: 김윤지 (YUN JI)
reason: 다양한 일상 콘텐츠를 제공하여 많은 반응을 얻고 있습니다."""
    },
    {
        "query": "소통이 활발한 일상 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 일상 관련 콘텐츠를 자주 올리며 소통이 활발합니다.
---
influencer_id: 31
name: 지는빈
reason: 일상적인 이야기를 통해 팔로워와의 소통을 잘 이어갑니다.
---
influencer_id: 33
name: 김윤지 (YUN JI)
reason: 다양한 일상 콘텐츠를 제공하여 많은 반응을 얻고 있습니다."""
    },
 {
        "query": "겨울철 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 스킨케어 루틴에 대한 다양한 팁을 제공하여 많은 신뢰를 받고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 겨울철 피부 관리를 위한 효과적인 루틴을 자주 공유하고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 겨울철 스킨케어 팁을 쉽게 설명하여 많은 사람들에게 도움이 됩니다."""
    },
    {
        "query": "피부 개선에 좋은 뷰티 제품을 리뷰하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 피부 개선을 위한 다양한 뷰티 제품을 상세히 리뷰합니다.
---
influencer_id: 8
name: 권지현
reason: 피부 개선에 도움이 되는 제품을 자주 소개하여 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 효과적인 피부 개선 제품에 대한 리뷰가 많아 유용합니다."""
    },
    {
        "query": "가성비 높은 뷰티 제품을 자주 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 가성비 좋은 뷰티 제품을 자주 리뷰하여 많은 사람들에게 인기가 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 가성비 높은 스킨케어 제품을 잘 홍보하고 있습니다.
---
influencer_id: 14
name: 예아린
reason: 저렴하면서도 효과적인 제품을 많이 소개합니다."""
    },
    {
        "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 전문적인 스킨케어 리뷰로 많은 팔로워들에게 신뢰를 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 제품에 대한 객관적인 리뷰를 통해 신뢰도를 높이고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 제품에 대한 솔직한 리뷰를 제공합니다."""
    },
    {
        "query": "팔로워 수가 10000명 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워 수가 많아 신뢰성이 높습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 뷰티 관련 콘텐츠로 많은 팔로워를 확보하고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 많은 팔로워 수를 자랑하며 인기가 많습니다."""
    },
    {
        "query": "비건 및 친환경 스킨케어 제품을 사용하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 12
name: 마르 Marr
reason: 비건 및 친환경 제품을 주로 사용하며 그에 대한 정보도 많이 제공합니다.
---
influencer_id: 1
name: 코덕❤
reason: 비건 뷰티 제품을 자주 소개하여 많은 주목을 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 친환경 스킨케어 제품에 대한 리뷰가 많이 올라와 있습니다."""
    },
    {
        "query": "신제품 리뷰가 빠르고 반응이 좋은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 신제품 리뷰를 빠르게 진행하며 팔로워의 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 새로운 제품에 대한 리뷰가 많고 반응이 활발합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 신제품 리뷰가 신속하게 이루어지며 많은 피드백을 받습니다."""
    },
    {
        "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 댓글 참여율이 높아 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글이 활발히 달리며 인기도가 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 참여율이 높아 팔로워와의 관계가 좋습니다."""
    },
    {
        "query": "가성비 좋은 스킨케어 제품을 자주 리뷰하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 가성비 높은 스킨케어 제품에 대한 리뷰가 많이 올라옵니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 가성비 좋은 제품을 소개하여 많은 팔로워의 사랑을 받고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 저렴한 스킨케어 제품을 중심으로 리뷰를 진행합니다."""
    },
    {
        "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 댓글 참여율이 높아 팔로워와의 소통이 잘 이루어집니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글이 활발히 달리며 인기도가 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 참여율이 높아 팔로워와의 관계가 좋습니다."""
    },
    {
        "query": "패션 트렌드를 자주 소개하는 남성 인플루언서를 추천해줘.",
        "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 최신 패션 트렌드를 잘 반영하여 다양한 스타일을 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 패션 트렌드를 주로 다루며 팔로워의 관심을 받고 있습니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 남성 패션을 주제로 한 콘텐츠로 많은 피드백을 얻고 있습니다."""
    },
    {
        "query": "팔로워와 소통이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워와의 소통이 활발하여 피드백이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와 친밀하게 소통하여 신뢰를 쌓고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 댓글과 피드백이 활발하여 소통이 잘 이루어집니다."""
    },
 {
        "query": "남성 팔로워가 많은 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 뷰티 제품을 자주 소개하여 남성 팔로워들이 많이 따릅니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션과 뷰티를 다루며 남성 팔로워의 반응이 좋습니다.
---
influencer_id: 1
name: 코덕❤
reason: 남성 팔로워와의 소통도 활발하여 다양한 피드백을 얻고 있습니다."""
    },
    {
        "query": "여름철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수품을 다양하게 소개하여 인기가 높습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름 패션 아이템을 자주 리뷰하여 많은 팔로워들에게 사랑받고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 필수 뷰티 아이템을 잘 소개하여 많은 반응을 얻고 있습니다."""
    },
    {
        "query": "피드백이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피드백을 자주 반영하여 팔로워와의 관계가 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워의 피드백에 귀 기울이며 소통이 활발합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 댓글 반응이 좋고, 팔로워의 피드백을 잘 반영합니다."""
    },
    {
        "query": "자연스러운 일상 사진으로 홍보를 잘하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 자연스러운 일상 사진으로 제품을 잘 홍보하며 친근감을 줍니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 장소에서 찍은 자연스러운 사진으로 반응이 좋습니다.
---
influencer_id: 31
name: 지는빈
reason: 자연스러운 일상 사진과 함께 제품을 홍보하여 신뢰를 얻고 있습니다."""
    },
    {
        "query": "가을 패션 아이템을 잘 홍보하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 가을 패션 아이템을 자주 소개하여 많은 인기를 끌고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 계절별 패션 아이템을 잘 소화하여 반응이 좋습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 가을 스타일링에 적합한 아이템을 자주 소개합니다."""
    },
    {
        "query": "트렌디한 패션 아이템을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 트렌드를 반영한 패션 아이템을 자주 소개하여 많은 주목을 받고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 트렌디한 스타일링으로 다양한 아이템을 잘 소개합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 최신 패션 트렌드를 반영하여 팔로워의 반응이 좋습니다."""
    },
    {
        "query": "평균 댓글 수가 10개 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 댓글이 활발히 달려 평균 댓글 수가 높은 편입니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워와의 소통이 잘 이루어져 평균 댓글 수가 많습니다.
---
influencer_id: 1
name: 코덕❤
reason: 활발한 댓글 참여로 평균 댓글 수가 높습니다."""
    },
    {
        "query": "가성비 높은 뷰티 제품을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 가성비 좋은 제품을 잘 소개하여 많은 팔로워의 사랑을 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 저렴하면서도 효과적인 제품에 대한 리뷰가 많습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 가성비 좋은 뷰티 아이템을 자주 소개하여 인기를 끌고 있습니다."""
    },
    {
        "query": "피부 진정 크림을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 피부 진정 제품을 리뷰하며 깊이 있는 정보를 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 피부 진정 크림의 효능을 잘 설명하여 많은 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피부 진정 관련 제품 리뷰가 많아 신뢰를 얻고 있습니다."""
    },
    {
        "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워와의 소통이 활발하여 피드백이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 소통을 중요시하여 많은 팔로워와 신뢰를 쌓고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워와의 대화를 통해 신뢰도를 높이고 있습니다."""
    },

 {
        "query": "팔로워 수가 많고 평균 댓글 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 높은 팔로워 수를 바탕으로 평균 댓글 수 또한 높은 편입니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 많은 팔로워와 활발한 댓글 참여로 인기를 끌고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워가 많고, 댓글 참여율이 높아 소통이 활발합니다."""
    },
    {
        "query": "반응 지수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글과 좋아요 수가 높은 반응 지수를 자랑합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 반응 지수가 높아 팔로워의 신뢰를 얻고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 평균 반응 지수가 높아 많은 인기를 끌고 있습니다."""
    },
    {
        "query": "겨울철 보습 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수 보습 제품을 자주 소개하여 많은 반응을 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 겨울철 스킨케어 루틴을 잘 설명하며 보습 제품을 추천합니다.
---
influencer_id: 1
name: 코덕❤
reason: 피부 보습에 대한 정보가 풍부하여 보습 제품 홍보에 적합합니다."""
    },
    {
        "query": "비건 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 비건 화장품을 주로 사용하며 신뢰성이 높습니다.
---
influencer_id: 36
name: 권지현
reason: 비건 제품 리뷰를 통해 많은 관심을 받고 있습니다.
---
influencer_id: 34
name: Niya 김반야
reason: 비건 및 친환경 제품을 자주 소개하여 호평을 받고 있습니다."""
    },
    {
        "query": "여행용 화장품을 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 여행지에서 화장품을 사용하며 실제 리뷰를 제공합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여행 중 필수 아이템으로 화장품을 추천하여 반응이 좋습니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 여행과 관련된 뷰티 제품을 잘 홍보하여 많은 사랑을 받고 있습니다."""
    },
    {
        "query": "패션 브랜드와의 협업 경험이 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 패션 브랜드와 협업하여 인지도를 높이고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 다양한 패션 브랜드와의 협업 경험으로 신뢰성을 얻고 있습니다.
---
influencer_id: 30
name: 수슬리 soosyl
reason: 패션 브랜드와의 협업을 통해 팔로워의 관심을 끌고 있습니다."""
    },
    {
        "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 실제 사용 후기를 통해 신뢰성 높은 스킨케어 리뷰를 제공합니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 스킨케어 제품에 대한 리뷰가 인상적이며 신뢰를 쌓고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 스킨케어 제품의 깊이 있는 리뷰로 많은 팔로워의 신뢰를 얻고 있습니다."""
    },
    {
        "query": "광고 게시물의 참여도가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 광고 게시물에 대한 높은 참여도로 인기 있는 인플루언서입니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 광고 게시물의 반응이 좋아 소통이 활발합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 광고 게시물에서 높은 참여율을 기록하여 효과적인 홍보가 가능합니다."""
    },
 {
        "query": "트렌디한 스킨케어 제품을 잘 홍보하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 최신 트렌드를 반영한 스킨케어 제품을 자주 소개하여 많은 반응을 얻습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 트렌디한 스킨케어 제품 리뷰가 많아 인기가 높습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 스킨케어 제품에 대한 트렌디한 접근으로 팔로워의 호응을 얻고 있습니다."""
    },
    {
        "query": "가을 패션을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 가을 패션 아이템을 자주 소개하여 많은 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 계절에 맞는 패션을 잘 소화하여 인기를 얻고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 가을 패션에 적합한 스타일링을 자주 보여줍니다."""
    },
    {
        "query": "여행지에서 찍은 사진을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여행 중 찍은 다양한 사진으로 제품을 잘 홍보합니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 여행지에서 자연스럽게 제품을 소개하여 많은 사랑을 받고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여행 사진을 통해 패션 아이템을 자연스럽게 홍보합니다."""
    },
 {
        "query": "팔로워 수가 10000명 이상인 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 10,000명이 넘는 팔로워를 보유하고 있으며, 소통이 활발합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 팔로워 수가 많고, 다양한 패션 콘텐츠를 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워가 많아 인플루언서로서 영향력이 큽니다."""
    },
    {
        "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 참여율이 높아 활발한 소통이 이루어집니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 콘텐츠로 댓글 참여를 유도하여 인기가 높습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글 참여율이 높고 소통이 원활합니다."""
    },
    {
        "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워와의 소통이 활발하며 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 친근한 소통으로 많은 팔로워와 유대감을 형성하고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 소통이 원활하여 팔로워와의 관계가 좋습니다."""
    },
    {
        "query": "피부 타입별 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 피부 타입에 맞는 스킨케어 루틴을 잘 설명합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피부 타입별로 적절한 제품을 추천하여 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 각 피부 타입에 맞는 루틴을 잘 설명하며 많은 호응을 얻고 있습니다."""
    },
    {
        "query": "평균 좋아요 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 평균 좋아요 수가 높아 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여러 콘텐츠에서 평균 좋아요 수가 높은 편입니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 인기 있는 콘텐츠로 평균 좋아요 수가 높습니다."""
    },
    {
        "query": "여름철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수품을 잘 소개하여 팔로워의 반응을 이끌어냅니다.
---
influencer_id: 1
name: 코덕❤
reason: 여름철 스킨케어 제품을 자주 추천하여 신뢰를 얻고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름 패션 아이템을 잘 홍보하여 팔로워의 관심을 끌고 있습니다."""
    },
    {
        "query": "남성 패션을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 패션 아이템을 다양하게 소개하여 많은 반응을 얻고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 트렌디한 남성 패션을 잘 소화하며 팔로워와 소통이 활발합니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 다양한 남성 패션 스타일을 자주 보여주어 인기가 높습니다."""
    },
    {
        "query": "여행 인플루언서를 추천해줘.",
        "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 여행지에서 찍은 사진으로 많은 인기를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여행 중 다양한 콘텐츠로 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여행 관련 패션 아이템을 소개하여 팔로워와 소통이 원활합니다."""
    },
    {
        "query": "반응 지수가 높은 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 높은 반응을 얻고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 아이템에 대한 높은 관심으로 반응이 좋습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 관련 콘텐츠에서 반응 지수가 높아 많은 팔로워의 신뢰를 얻고 있습니다."""
    },
{
        "query": "겨울철 보습 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 겨울철 보습 제품에 대한 다양한 추천을 통해 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 스킨케어 제품을 잘 소개하여 많은 호응을 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 보습 제품 관련 정보를 쉽게 설명하여 팔로워의 반응이 좋습니다."""
    },
    {
        "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 스킨케어 제품 리뷰로 팔로워에게 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 신뢰성 있는 리뷰로 팔로워에게 꾸준한 인기를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 세밀한 제품 설명으로 많은 호응을 얻고 있습니다."""
    },
    {
        "query": "제품 홍보 경험이 많은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 브랜드와 협업 경험이 많아 홍보에 능숙합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 제품 홍보 경험을 통해 많은 신뢰를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다수의 뷰티 제품을 소개하며 홍보 경험이 풍부합니다."""
    },
    {
        "query": "트렌디한 패션 아이템을 잘 소개하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드를 반영한 아이템을 자주 소개합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패셔너블한 스타일링으로 많은 관심을 끌고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 트렌디한 패션 아이템을 잘 소화하여 인기가 높습니다."""
    },
    {
        "query": "피부 타입에 맞는 제품 추천이 잘 이루어지는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 각 피부 타입에 맞는 제품을 추천하여 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 피부 타입에 따른 제품 추천이 가능합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 피부 타입별로 적절한 제품을 잘 설명합니다."""
    },
    {
        "query": "신제품을 자주 리뷰하는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 신제품 리뷰를 통해 항상 새로운 정보를 제공합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 새로운 뷰티 아이템을 꾸준히 리뷰하여 반응이 좋습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 신제품에 대한 상세한 리뷰를 자주 올립니다."""
    },
    {
        "query": "소통이 활발한 인플루언서를 추천해줘.",
        "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 소통이 활발하여 인기가 높습니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워와의 활발한 소통을 통해 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 소통을 중요시하며 팔로워와 유대감을 형성하고 있습니다."""
    },
    {
        "query": "팔로워가 많은 패션 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 많은 팔로워를 보유하고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션 아이템을 소개하며 많은 관심을 받고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 관련 콘텐츠에서 높은 팔로워 수를 기록하고 있습니다."""
    },
    {
        "query": "다양한 화장품 브랜드와의 협업이 많은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 1
name: 코덕❤
reason: 여러 브랜드와의 협업을 통해 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 브랜드와 협업한 경험이 풍부합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여러 브랜드와의 협업으로 팔로워의 신뢰를 얻고 있습니다."""
    },
    {
        "query": "패션 브랜드와의 협업 경험이 있는 인플루언서를 추천해줘.",
        "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 브랜드와 협업하여 인기를 얻고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 브랜드와의 협업 경험이 많아 인지도가 높습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 협업한 브랜드가 많아 팔로워에게 신뢰를 얻고 있습니다."""
    },
    {
        "query": "평균 댓글 수가 높은 인플루언서를 추천해줘.",
        "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 수가 많아 팔로워와의 소통이 활발합니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 콘텐츠로 평균 댓글 수가 높습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 평균 댓글 수가 높습니다."""
    },
{
    "query": "겨울철 보습 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 겨울철 보습 제품에 대한 다양한 추천을 통해 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 스킨케어 제품을 잘 소개하여 많은 호응을 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 보습 제품 관련 정보를 쉽게 설명하여 팔로워의 반응이 좋습니다."""
},
{
    "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 스킨케어 제품 리뷰로 팔로워에게 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 신뢰성 있는 리뷰로 팔로워에게 꾸준한 인기를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 세밀한 제품 설명으로 많은 호응을 얻고 있습니다."""
},
{
    "query": "제품 홍보 경험이 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 브랜드와 협업 경험이 많아 홍보에 능숙합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 제품 홍보 경험을 통해 많은 신뢰를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다수의 뷰티 제품을 소개하며 홍보 경험이 풍부합니다."""
},
{
    "query": "트렌디한 패션 아이템을 잘 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드를 반영한 아이템을 자주 소개합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패셔너블한 스타일링으로 많은 관심을 끌고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 트렌디한 패션 아이템을 잘 소화하여 인기가 높습니다."""
},
{
    "query": "피부 타입에 맞는 제품 추천이 잘 이루어지는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 각 피부 타입에 맞는 제품을 추천하여 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 피부 타입에 따른 제품 추천이 가능합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 피부 타입별로 적절한 제품을 잘 설명합니다."""
},
{
    "query": "신제품을 자주 리뷰하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 신제품 리뷰를 통해 항상 새로운 정보를 제공합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 새로운 뷰티 아이템을 꾸준히 리뷰하여 반응이 좋습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 신제품에 대한 상세한 리뷰를 자주 올립니다."""
},
{
    "query": "소통이 활발한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 소통이 활발하여 인기가 높습니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워와의 활발한 소통을 통해 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 소통을 중요시하며 팔로워와 유대감을 형성하고 있습니다."""
},
{
    "query": "팔로워가 많은 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 많은 팔로워를 보유하고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션 아이템을 소개하며 많은 관심을 받고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 관련 콘텐츠에서 높은 팔로워 수를 기록하고 있습니다."""
},
{
    "query": "다양한 화장품 브랜드와의 협업이 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 여러 브랜드와의 협업을 통해 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 브랜드와 협업한 경험이 풍부합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여러 브랜드와의 협업으로 팔로워의 신뢰를 얻고 있습니다."""
},
{
    "query": "패션 브랜드와의 협업 경험이 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 브랜드와 협업하여 인기를 얻고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 브랜드와의 협업 경험이 많아 인지도가 높습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 협업한 브랜드가 많아 팔로워에게 신뢰를 얻고 있습니다."""
},
{
    "query": "평균 댓글 수가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 수가 많아 팔로워와의 소통이 활발합니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 콘텐츠로 평균 댓글 수가 높습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 평균 댓글 수가 높습니다."""
}
,{
    "query": "좋아요 수가 많은 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 뷰티 제품 관련 콘텐츠로 높은 좋아요 수를 기록하고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 다양한 뷰티 아이템을 소개하며 많은 호응을 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 화장품 리뷰에서 좋아요 수가 높아 많은 인기를 끌고 있습니다."""
},
{
    "query": "팔로워가 10000명 이상인 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 높은 팔로워 수를 자랑하며 패션 콘텐츠에서 인기를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 뷰티 분야에서 큰 영향력을 발휘하고 있는 인플루언서입니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 많은 팔로워를 보유하고 있으며, 다양한 제품을 소개합니다."""
},
{
    "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 소통이 활발하여 신뢰를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 질문에 빠르게 답변하며 팔로워와 유대감을 형성하고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 소통을 중요시하며 팔로워의 의견을 잘 반영합니다."""
},
{
    "query": "겨울철 패션 아이템을 잘 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 겨울철 패션 아이템을 잘 소화하며 스타일링을 제안합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 다양한 겨울철 스타일을 선보이며 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 겨울철 아이템을 자주 소개하여 팔로워의 호응을 얻고 있습니다."""
},
{
    "query": "반응 지수가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 높은 좋아요와 댓글 수로 인해 반응 지수가 높습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 화장품 리뷰에서 반응이 좋고 팔로워의 참여가 활발합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 제품 소개 시 반응 지수가 뛰어나 많은 관심을 받고 있습니다."""
},
{
    "query": "뷰티 관련 제품을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 뷰티 제품을 소개하며 많은 팔로워의 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 화장품 관련 콘텐츠에서 유익한 정보를 제공하고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 뷰티 제품에 대한 깊이 있는 설명으로 팔로워의 관심을 끌고 있습니다."""
},
{
    "query": "패션 아이템을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 아이템을 소개하며 팔로워의 호응을 얻고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 트렌드를 반영한 아이템을 자주 소개하여 인기가 높습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 관련 콘텐츠에서 많은 팔로워를 보유하고 있습니다."""
},
{
    "query": "여름철 필수품을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 아이템을 효과적으로 홍보하며 많은 호응을 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 여름철 스킨케어와 뷰티 아이템을 잘 소화합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 필수 뷰티 제품을 잘 소개하여 반응이 좋습니다."""
},
{
    "query": "겨울철 보습 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 겨울철 보습 제품에 대한 다양한 추천을 통해 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 스킨케어 제품을 잘 소개하여 많은 호응을 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 보습 제품 관련 정보를 쉽게 설명하여 팔로워의 반응이 좋습니다."""
},
{
    "query": "트렌디한 메이크업을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 최신 메이크업 트렌드를 자주 반영하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 메이크업 팁과 제품을 소개하여 많은 인기를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 유행하는 메이크업 스타일을 자주 소개하며 팔로워의 반응이 좋습니다."""
}
,{
    "query": "가성비 좋은 뷰티 제품을 소개할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 가성비 뷰티 제품을 추천하여 많은 신뢰를 얻고 있습니다.
---
influencer_id: 2
name: 코덕 쩨로
reason: 합리적인 가격의 제품을 잘 소개하며 인기가 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 가성비 좋은 뷰티 제품 리뷰로 팔로워의 많은 호응을 받고 있습니다."""
},
{
    "query": "소통이 활발한 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 팔로워와의 소통이 활발하여 많은 피드백을 받고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 아이템에 대해 자주 소통하며 신뢰를 쌓고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 팔로워와의 소통을 중요시하며 반응이 좋습니다."""
},
{
    "query": "반응이 활발한 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 뷰티 관련 콘텐츠에서 높은 반응을 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 제품 리뷰에서 많은 좋아요와 댓글을 기록하고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 소통이 활발하여 반응이 좋고 신뢰를 얻고 있습니다."""
},
{
    "query": "최신 패션 트렌드를 반영하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드를 적극적으로 반영하여 스타일링을 제안합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 트렌드를 자주 업데이트하며 팔로워의 호응을 얻고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 최신 패션 아이템을 소개하며 많은 반응을 얻고 있습니다."""
},
{
    "query": "여행용 화장품을 잘 홍보할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여행 관련 뷰티 제품을 잘 소개하여 인기가 많습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여행 중 유용한 화장품을 잘 추천하여 팔로워의 호응을 얻고 있습니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 다양한 여행지에서 화장품을 소개하며 효과적인 홍보를 하고 있습니다."""
},
{
    "query": "겨울철 필수 뷰티 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 겨울철 보습 제품에 대한 리뷰에서 많은 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수 뷰티 아이템을 자주 소개하여 많은 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 겨울철 피부 관리에 적합한 제품을 잘 홍보하고 있습니다."""
},
{
    "query": "남성 화장품을 자주 사용하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 화장품 관련 콘텐츠에서 많은 팔로워를 보유하고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 화장품에 대한 리뷰를 자주 올리며 신뢰를 얻고 있습니다.
---
influencer_id: 39
name: 솔솔씨
reason: 남성 화장품을 다루며 다양한 정보를 제공하고 있습니다."""
},
{
    "query": "피부 타입별 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 피부 타입을 고려한 스킨케어 팁을 제공하여 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 피부 타입별 맞춤형 스킨케어 루틴을 자주 소개합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 피부 타입에 맞는 제품 추천이 효과적이며 반응이 좋습니다."""
},
{
    "query": "겨울철 보습 제품을 잘 홍보할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 겨울철 보습 제품 리뷰에서 높은 호응을 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수 보습 제품을 잘 소개하여 많은 반응을 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 겨울철 피부 관리 제품에 대한 정보 제공이 효과적입니다."""
},
{
    "query": "다양한 장소에서 제품을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 여행지에서 제품을 자연스럽게 소개하여 많은 호응을 얻고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 장소에서 패션 아이템을 소개하며 큰 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 장소에서 촬영한 패션 콘텐츠가 주목받고 있습니다."""
}
,{
    "query": "가성비 좋은 패션 아이템을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 합리적인 가격의 패션 아이템을 잘 소개하여 인기를 얻고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 가격대의 패션 아이템을 추천하여 많은 신뢰를 받고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 가성비 높은 패션 아이템에 대한 리뷰가 효과적입니다."""
},
{
    "query": "화장품을 자주 리뷰하는 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 화장품 리뷰를 통해 많은 반응을 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 화장품에 대한 자세한 리뷰를 자주 올려 팔로워의 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 자주 화장품 리뷰를 올리며 팔로워의 피드백이 좋습니다."""
},
{
    "query": "여행 중 필수 아이템을 잘 소개할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여행 필수 아이템을 자주 소개하여 많은 반응을 얻고 있습니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 여행 중 필요한 아이템을 효과적으로 추천합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 여행 관련 아이템을 자연스럽게 홍보하고 있습니다."""
},
{
    "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워와의 소통을 중요시하며 많은 피드백을 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 뷰티 제품에 대한 질문에 친절하게 답변하여 소통이 활발합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워와의 소통을 중요시하며 반응이 좋습니다."""
},
{
    "query": "남성 스킨케어 제품을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 스킨케어 제품에 대한 정보 제공이 효과적입니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 화장품을 자주 리뷰하여 신뢰를 얻고 있습니다.
---
influencer_id: 39
name: 솔솔씨
reason: 남성 스킨케어 제품 관련 콘텐츠에서 반응이 좋습니다."""
},
{
    "query": "여름철 필수 스킨케어 제품을 추천할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 여름철 피부 관리에 필수적인 제품을 잘 소개합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여름철 보습 및 자외선 차단 제품에 대한 리뷰가 효과적입니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 필수 아이템을 자주 추천하여 신뢰를 얻고 있습니다."""
},
{
    "query": "패션 잡지와 협업 경험이 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 잡지와의 협업 경험이 풍부하여 많은 반응을 얻고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 다양한 패션 잡지와의 협업으로 트렌디한 아이템을 소개합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 관련 잡지와의 협업 경험이 많아 신뢰를 얻고 있습니다."""
},
{
    "query": "여름철 여행 아이템을 잘 소개할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 여행 필수 아이템을 자주 소개하여 많은 호응을 얻고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여행 관련 아이템을 자연스럽게 홍보하여 인기를 끌고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름 여행지에서 필요한 패션 아이템을 잘 추천합니다."""
},
{
    "query": "소통이 활발한 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 팔로워와의 소통이 활발하며 패션에 대한 정보 제공이 효과적입니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 질문에 적극적으로 답변하며 신뢰를 얻고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 소통을 중시하며 팔로워의 피드백을 잘 반영합니다."""
}
,{
    "query": "스킨케어 루틴을 잘 설명할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 스킨케어 루틴에 대한 상세한 설명과 제품 추천이 효과적입니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 피부 타입에 맞는 스킨케어 루틴을 잘 소개합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 자신의 루틴을 공유하며 팔로워와 소통이 활발합니다."""
},
{
    "query": "트렌디한 패션 아이템을 잘 소개할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 트렌드를 반영한 패션 아이템을 잘 추천하여 많은 호응을 얻고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 시즌별 트렌디한 패션 아이템을 자연스럽게 소개합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 관련 최신 트렌드를 자주 다루어 팔로워의 신뢰를 얻고 있습니다."""
},
{
    "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 스킨케어 제품에 대한 진솔한 리뷰로 많은 신뢰를 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 스킨케어 제품을 공정하게 리뷰하여 신뢰를 쌓고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 객관적인 리뷰로 팔로워의 신뢰를 얻고 있습니다."""
},
{
    "query": "팔로워 수가 많은 여행 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 여행 관련 콘텐츠에서 팔로워와의 소통이 활발하며 많은 인기를 얻고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 여행지를 소개하며 팔로워 수가 많습니다.
---
influencer_id: 8
name: 권지현
reason: 여행지에서의 활동과 콘텐츠가 많은 호응을 얻고 있습니다."""
},
{
    "query": "남성 화장품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 화장품에 대한 정보 제공이 효과적입니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 화장품에 대한 리뷰와 홍보가 신뢰를 얻고 있습니다.
---
influencer_id: 39
name: 솔솔씨
reason: 남성 화장품을 자연스럽게 소개하여 많은 호응을 받고 있습니다."""
},
{
    "query": "여름철 필수 뷰티 제품을 추천할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 여름철 필수 뷰티 제품을 잘 소개하여 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여름철 제품 리뷰에 강점을 지니며 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 필수 아이템을 자주 추천하여 많은 반응을 얻고 있습니다."""
},
{
    "query": "여행지에서 찍은 사진을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여행지에서의 사진과 콘텐츠가 매우 매력적입니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 여행지를 잘 소개하며 시각적으로 매력적인 사진을 공유합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여행지에서의 패션과 관련된 사진이 돋보입니다."""
},
{
    "query": "소통이 활발한 일상 인플루언서를 추천해줘.",
    "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 팔로워와의 소통이 활발하며 일상 콘텐츠에 대한 반응이 좋습니다.
---
influencer_id: 31
name: 지는빈
reason: 친근한 소통으로 팔로워와의 관계가 깊습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 일상 콘텐츠에서 팔로워와의 소통이 두드러집니다."""
}
,{
    "query": "광고 게시물의 참여도가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 광고 게시물에 대한 높은 참여율을 기록하고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 광고 관련 게시물에서 팔로워의 반응이 활발합니다.
---
influencer_id: 8
name: 권지현
reason: 광고 포스팅에서 높은 댓글과 좋아요 수를 자랑합니다."""
},
{
    "query": "가성비 좋은 뷰티 제품을 소개할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 가성비 좋은 뷰티 제품을 꾸준히 소개하여 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 실용적인 제품을 추천하여 많은 인기를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 가성비 제품을 효과적으로 홍보하고 있습니다."""
},
{
    "query": "피부 타입별 스킨케어 제품을 추천할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 피부 타입에 맞는 다양한 제품을 소개하여 신뢰를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 각 피부 타입에 맞춘 스킨케어 제품을 효과적으로 추천합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피부 유형에 따라 추천 제품을 세분화하여 공유합니다."""
},
{
    "query": "여름철 보습 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 여름철 보습에 대한 전문적인 지식을 바탕으로 제품을 추천합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여름철 보습 제품을 자주 리뷰하여 신뢰를 쌓고 있습니다.
---
influencer_id: 8
name: 권지현
reason: 다양한 여름 보습 제품에 대한 실질적인 리뷰를 제공합니다."""
},
{
    "query": "학생들이 많이 팔로우하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 학생층의 공감을 불러일으키는 콘텐츠로 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션과 일상 콘텐츠로 학생 팔로워를 많이 보유하고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 친근한 소통으로 학생들에게 높은 인기를 얻고 있습니다."""
},
{
    "query": "가성비 좋은 패션 아이템을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 30
name: 수슬리 soosyl
reason: 실용적인 패션 아이템을 자주 추천하여 많은 호응을 얻고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 트렌디한 아이템을 가성비 좋게 소개하는 데 능합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 아이템의 가격 대비 효용을 강조하여 추천합니다."""
},
{
    "query": "반응 지수가 높은 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 관련 게시물에서 높은 반응 지수를 기록하고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 아이템을 효과적으로 홍보하여 반응이 좋습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 많은 팔로워와 소통하며 높은 반응을 얻고 있습니다."""
},
{
    "query": "평균 댓글 수가 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 주제로 활발한 소통을 이어가고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워들과의 소통이 활발하여 댓글 수가 많습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워와의 친밀한 소통으로 댓글 수가 높습니다."""
},
{
    "query": "여름철 필수 스킨케어 제품을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 여름철 스킨케어 제품을 잘 설명하여 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 여름 스킨케어 제품에 대한 정보를 제공합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 필수 아이템을 자주 추천하여 많은 반응을 얻고 있습니다."""
},
{
    "query": "제품 리뷰 경험이 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 뷰티 제품에 대한 리뷰 경험이 많아 신뢰를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 많은 스킨케어 제품을 리뷰하여 팔로워의 신뢰를 받습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 여러 제품에 대한 리뷰 경험이 많아 신뢰도가 높습니다."""
},
{
    "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워들과의 소통이 활발하여 많은 호응을 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 친구 같은 친근한 소통으로 인기가 많습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 소통 방식으로 팔로워들과 관계를 깊게 유지합니다."""
}
,{
    "query": "소통이 활발한 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 팔로워들과의 소통이 활발하여 패션 관련 피드백이 많습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 게시물에 대한 소통이 활발하여 인기가 높습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 팔로워들과의 소통을 중요시하여 반응이 좋습니다."""
},
{
    "query": "광고 게시물 참여율이 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 광고 관련 게시물에서 매우 높은 참여율을 기록하고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 광고에 대한 반응이 좋고 참여도가 높습니다.
---
influencer_id: 8
name: 권지현
reason: 다양한 광고 게시물에서 팔로워의 참여가 활발합니다."""
},
{
    "query": "패션 관련 브랜드와 협업 경험이 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 브랜드와 협업하여 신뢰도를 쌓고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여러 브랜드와의 협업을 통해 스타일링을 선보이고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 브랜드와의 협업 경험이 많아 많은 팔로워를 보유하고 있습니다."""
},
{
    "query": "여행 관련 제품을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 다양한 여행지를 소개하며 관련 제품을 잘 홍보합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여행 관련 제품을 자주 리뷰하여 많은 호응을 얻고 있습니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 여행과 일상을 결합하여 제품을 자연스럽게 소개합니다."""
},
{
    "query": "평균 좋아요 수가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 게시물당 평균 좋아요 수가 매우 높아 인기를 끌고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 게시물에서 높은 좋아요 수를 기록하고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 제품을 소개하며 평균 좋아요 수가 높습니다."""
},
{
    "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 스킨케어 제품에 대한 신뢰할 수 있는 리뷰로 팔로워의 지지를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 제품에 대한 솔직한 리뷰로 팔로워들의 신뢰를 받고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 신뢰도 높은 스킨케어 리뷰로 많은 팔로워들에게 인기가 있습니다."""
},
{
    "query": "여름철 스킨케어 루틴을 잘 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 여름철 피부 관리에 대한 다양한 루틴을 소개하고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 스킨케어 제품과 루틴을 꾸준히 공유합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 스킨케어 팁을 자주 올려 인기가 높습니다."""
},
{
    "query": "여행지에서 찍은 사진을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 다양한 여행지에서 촬영한 멋진 사진을 공유하며 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여행 중 찍은 사진으로 화려한 스타일링을 선보입니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 여행지를 배경으로 한 다양한 사진을 잘 홍보합니다."""
},
{
    "query": "여름철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 여름철 필수품을 효과적으로 소개하여 팔로워의 반응을 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여름 필수 아이템을 꾸준히 리뷰하고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 여름 필수 제품에 대한 리뷰로 많은 인기를 끌고 있습니다."""
}
,
{
    "query": "반응 지수가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 반응 지수가 매우 높아 팔로워들의 참여가 활발합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 제품에 대한 반응이 좋고 높은 참여율을 자랑합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 높은 반응 지수로 팔로워와의 소통이 활발합니다."""
},
{
    "query": "트렌디한 패션 아이템을 잘 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드를 반영한 스타일링으로 많은 호응을 얻고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 트렌디한 패션 아이템을 소개하며 팔로워들에게 인기가 높습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 트렌디한 패션 아이템을 자주 추천하여 인기를 끌고 있습니다."""
},
{
    "query": "피부 진정 크림을 효과적으로 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 피부 진정 효과가 있는 제품을 잘 홍보하여 인기가 높습니다.
---
influencer_id: 1
name: 코덕❤
reason: 스킨케어 관련 콘텐츠로 피부 진정 크림을 효과적으로 소개할 수 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피부 진정과 관련된 제품에 대한 신뢰도 높은 리뷰로 팔로워의 반응을 얻고 있습니다."""
},
{
    "query": "남성 팔로워가 많은 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 팔로워를 대상으로 한 뷰티 제품을 잘 소개하여 인기를 끌고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 팔로워들에게 적합한 뷰티 제품을 리뷰하며 신뢰를 얻고 있습니다.
---
influencer_id: 36
name: 권지현
reason: 남성 팔로워를 위한 다양한 뷰티 제품을 소개하여 반응이 좋습니다."""
},
{
    "query": "여름 패션 아이템을 효과적으로 홍보할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름 패션 아이템을 자주 소개하며 스타일링을 잘 선보입니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름철 패션 아이템을 효과적으로 홍보하며 많은 호응을 얻고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 여름철 필수 아이템에 대한 리뷰로 인기를 끌고 있습니다."""
},
{
    "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 댓글 참여율이 높아 팔로워들과의 소통이 활발합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글을 통한 소통이 원활하여 반응이 좋습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 참여가 활발하여 팔로워들과의 관계를 잘 유지합니다."""
},
{
    "query": "평균 댓글 수가 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 평균 댓글 수가 높아 팔로워들의 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 게시물마다 댓글 수가 많아 반응이 활발합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 게시물에서 평균 댓글 수가 높습니다."""
},
{
    "query": "저가형 스킨케어 제품을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 저가형 스킨케어 제품을 자주 리뷰하여 많은 관심을 받고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 가성비 좋은 스킨케어 제품을 효과적으로 소개합니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 저가형 스킨케어 제품을 리뷰하며 팔로워의 호응을 얻고 있습니다."""
},
{
    "query": "인테리어와 관련된 제품을 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 일상과 인테리어를 잘 결합하여 다양한 제품을 소개합니다. 참고: 질문에 대한 관련 카테고리가 부족해 다른 기준으로 추천하였습니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 여행과 일상을 통해 인테리어 소품을 자연스럽게 홍보합니다. 참고: 질문에 대한 관련 카테고리가 부족해 다른 기준으로 추천하였습니다.
---
influencer_id: 1
name: 코덕❤
reason: 인테리어와 관련된 제품을 소개하는 콘텐츠로 관심을 받고 있습니다. 참고: 질문에 대한 관련 카테고리가 부족해 다른 기준으로 추천하였습니다."""
}
,{
    "query": "팔로워가 10000명 이상인 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워 수가 10000명을 초과하여 신뢰도가 높습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 10000명 이상의 팔로워로 높은 참여율을 자랑합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 10000명 이상의 팔로워를 보유하여 영향력이 큽니다."""
},
{
    "query": "여름철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름철 필수 아이템을 잘 홍보하여 팔로워들의 관심을 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름 시즌에 적합한 다양한 필수품을 소개합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수품에 대한 리뷰가 많아 신뢰를 얻고 있습니다."""
},
{
    "query": "반응이 활발한 뷰티 카테고리 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 뷰티 관련 콘텐츠로 반응이 활발하여 인기가 높습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 뷰티 제품에 대한 반응이 좋고 소통이 활발합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워들과의 소통이 원활하고 반응이 좋습니다."""
},
{
    "query": "간편한 다이어트 제품을 잘 소개할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다이어트 관련 제품을 자주 리뷰하며 많은 관심을 받고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 다이어트 제품에 대한 리뷰가 많아 신뢰를 얻고 있습니다.
---
influencer_id: 34
name: Niya 김반야
reason: 다양한 다이어트 제품을 자연스럽게 소개하여 인기가 높습니다."""
},
{
    "query": "다양한 장소에서 찍은 여행 사진을 잘 홍보하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 다양한 여행지를 소개하며 풍부한 콘텐츠로 팔로워들의 관심을 끌고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여행 사진을 자주 올려 팔로워들에게 높은 반응을 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 여행지에서 찍은 사진으로 팔로워와의 소통이 활발합니다."""
},
{
    "query": "겨울철 보습 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 보습에 적합한 제품을 자주 소개하며 인기를 끌고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 겨울철 필수 보습 제품을 리뷰하여 신뢰도가 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 보습 제품에 대한 세심한 리뷰로 많은 팔로워의 관심을 얻고 있습니다."""
},
{
    "query": "새로운 패션 스타일을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 새로운 패션 트렌드를 잘 반영하여 다양한 스타일을 소개합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 유행하는 패션 스타일을 자주 업데이트하여 팔로워들에게 인기가 많습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 다양한 스타일을 제안하여 팔로워의 관심을 끌고 있습니다."""
},
{
    "query": "남성 팔로워가 많은 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 팔로워를 대상으로 한 다양한 패션 아이템을 소개하고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션 아이템을 자주 리뷰하여 남성 팔로워들에게 인기가 많습니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 남성 패션에 대한 다양한 콘텐츠를 제공하여 많은 호응을 얻고 있습니다."""
},
{
    "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 신뢰할 수 있는 스킨케어 리뷰로 팔로워의 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 스킨케어 제품에 대한 세심한 리뷰로 인기가 높습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 효과적인 스킨케어 제품을 소개하여 많은 팔로워의 신뢰를 얻고 있습니다."""
},
{
    "query": "피부 타입별 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 피부 타입에 맞는 스킨케어 루틴을 잘 설명합니다.
---
influencer_id: 1
name: 코덕❤
reason: 피부 타입에 따른 적절한 제품을 추천하여 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 세심한 설명으로 피부 타입별 루틴을 소개하여 많은 호응을 얻고 있습니다."""
}
,{
    "query": "제품에 대한 세세한 리뷰를 남기는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 제품에 대한 상세한 리뷰로 많은 신뢰를 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 제품에 대한 깊이 있는 분석을 제공하여 호응이 좋습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 제품 설명이 세밀하여 많은 팔로워의 관심을 끌고 있습니다."""
},
{
    "query": "여름철 선크림을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 아이템인 선크림을 효과적으로 소개합니다.
---
influencer_id: 1
name: 코덕❤
reason: 피부 보호를 강조하며 선크림 제품을 잘 홍보합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여름철에 적합한 선크림 제품에 대한 리뷰가 많습니다."""
},
{
    "query": "계절에 맞는 패션 아이템을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 계절별 패션 아이템을 잘 소개하여 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 시즌별 패션 트렌드를 잘 반영하여 인기가 높습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 계절에 맞는 다양한 스타일을 제안합니다."""
},
{
    "query": "팔로워 수 대비 반응도가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 높은 팔로워 수에도 불구하고 반응이 활발하여 신뢰받고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워 수에 비해 높은 참여율을 보이고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워 수에 비례하여 반응이 좋고 소통이 활발합니다."""
},
{
    "query": "주로 소통을 활발히 하며 제품을 자연스럽게 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워들과의 소통이 활발하며 자연스럽게 제품을 소개합니다.
---
influencer_id: 1
name: 코덕❤
reason: 소통을 중시하여 팔로워들의 반응이 좋습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 활발한 소통으로 제품을 자연스럽게 홍보하는 데 능숙합니다."""
},
{
    "query": "트렌디한 패션 아이템을 잘 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드를 잘 반영하여 인기가 높습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 트렌디한 스타일을 자주 소개하여 많은 팔로워를 끌어모으고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 다양한 패션 아이템을 소개하여 트렌드에 민감한 팔로워들에게 인기입니다."""
},
{
    "query": "피부 개선을 위한 뷰티 제품을 잘 홍보하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 피부 개선과 관련된 다양한 제품을 효과적으로 소개합니다.
---
influencer_id: 1
name: 코덕❤
reason: 피부 개선 효과가 있는 제품에 대한 리뷰가 많아 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피부 개선을 강조한 제품을 자주 추천하여 많은 관심을 받고 있습니다."""
},
{
    "query": "자연스러운 일상 사진으로 홍보를 잘하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 자연스러운 일상 사진을 자주 올리며 신뢰를 쌓고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 일상 속 자연스러운 콘텐츠로 많은 팔로워의 관심을 끌고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 자연스러운 일상 사진으로 팔로워와 소통하며 홍보합니다."""
},
{
    "query": "다이어트 식품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다이어트 관련 콘텐츠를 자주 올려 팔로워들에게 인기가 많습니다.
---
influencer_id: 34
name: Niya 김반야
reason: 다양한 다이어트 제품을 소개하여 많은 호응을 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다이어트 제품에 대한 리뷰가 많아 신뢰를 쌓고 있습니다."""
},
{
    "query": "스킨케어 제품의 신뢰도가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 스킨케어 제품에 대한 신뢰할 수 있는 리뷰를 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 스킨케어 제품에 대한 리뷰로 많은 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 효과적인 스킨케어 제품을 추천하여 팔로워의 신뢰를 받고 있습니다."""
}
,{
    "query": "친환경 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 친환경 제품을 주로 사용하는 인플루언서로 인식되고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 친환경 뷰티 제품에 대한 소개가 많아 신뢰를 받고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 환경을 고려한 제품을 자주 추천하여 호응이 좋습니다."""
},
{
    "query": "가성비 좋은 뷰티 제품을 소개할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 가성비가 뛰어난 뷰티 제품을 자주 소개하여 많은 팔로워를 끌어모으고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 합리적인 가격의 제품을 강조하며 팔로워의 신뢰를 얻고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 저렴하면서 효과적인 제품 리뷰로 인기 있는 인플루언서입니다."""
},
{
    "query": "소통을 중요시하는 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 팔로워들과의 소통이 활발하여 친밀한 관계를 유지합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 소통을 중시하며 자주 피드백을 반영합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 소통이 활발하여 팔로워와의 관계를 잘 유지합니다."""
},
{
    "query": "저자극 제품을 주로 사용하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 저자극 스킨케어 제품을 자주 사용하는 인플루언서입니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 피부에 자극이 적은 제품을 주로 소개하여 호응이 좋습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 저자극 제품에 대한 리뷰가 많아 신뢰를 얻고 있습니다."""
},
{
    "query": "팔로워 수가 많고 평균 댓글이 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워 수가 많고 댓글 참여율이 높은 인플루언서입니다.
---
influencer_id: 1
name: 코덕❤
reason: 많은 팔로워와 함께 높은 댓글 수를 자랑합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워 수가 많고 반응이 활발하여 소통이 좋습니다."""
},
{
    "query": "피드백이 활발한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 피드백이 활발하여 신뢰를 쌓고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 피드백을 자주 반영하여 팔로워와의 관계가 좋습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 활발한 소통으로 피드백을 잘 반영합니다."""
},
{
    "query": "패션 브랜드와의 협업 경험이 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 브랜드와의 협업 경험이 풍부합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여러 브랜드와의 협업을 통해 인지도가 높습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 브랜드와의 다양한 협업을 진행하고 있습니다."""
},
{
    "query": "계절별 피부 관리 제품을 잘 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 계절별로 적합한 스킨케어 제품을 잘 소개합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 계절에 맞는 피부 관리 방법을 자주 공유합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 각 계절별로 추천하는 제품이 다양합니다."""
},
{
    "query": "팔로워 수가 많고 반응이 활발한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 많은 팔로워를 보유하고 있으며 반응이 매우 활발합니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워 수가 많고 소통도 원활하여 인기가 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워가 많고 활발한 댓글 반응을 얻고 있습니다."""
}
,{
    "query": "다양한 메이크업 제품을 잘 홍보하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 메이크업 제품을 소개하며 사용법도 상세히 설명합니다.
---
influencer_id: 1
name: 코덕❤
reason: 메이크업 제품에 대한 리뷰와 사용기를 자주 게시합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 메이크업 관련 제품을 다채롭게 소개하는 인플루언서입니다."""
},
{
    "query": "최신 뷰티 트렌드를 반영하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 뷰티 트렌드를 빠르게 반영하여 신뢰를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 최신 뷰티 트렌드에 맞는 제품을 추천하여 많은 관심을 받고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 트렌디한 뷰티 아이템을 주로 소개하는 인플루언서입니다."""
},
{
    "query": "팔로워 수가 2000명 이하이면서 소통이 활발한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 팔로워 수는 적지만 소통이 활발하여 신뢰를 얻고 있습니다.
---
influencer_id: 31
name: 지는빈
reason: 작은 커뮤니티에서 소통이 원활하고 피드백이 좋습니다.
---
influencer_id: 36
name: 권지현
reason: 적은 팔로워 수에도 불구하고 활발한 댓글 소통이 특징입니다."""
},
{
    "query": "비건 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 비건 제품을 자주 소개하며 신뢰를 받고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 비건 화장품에 대한 리뷰가 많아 관심을 끌고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 비건 뷰티 제품에 대한 인식이 높아져 인기를 끌고 있습니다."""
},
{
    "query": "여름철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 아이템을 잘 소개하며 실용적인 조언을 제공합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름철 패션 아이템을 효과적으로 소개하는 인플루언서입니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름 시즌에 적합한 제품을 자주 추천하여 많은 호응을 얻고 있습니다."""
},
{
    "query": "트렌디한 패션 아이템을 잘 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드에 맞는 아이템을 자주 소개하여 인기가 많습니다.
---
influencer_id: 30
name: 수슬리 soosyl
reason: 패션 트렌드를 반영한 스타일을 잘 보여줍니다.
---
influencer_id: 35
name: 옷미새 이수 eesoo
reason: 다양한 트렌디 아이템을 소개하며 팔로워와 소통합니다."""
},
{
    "query": "피부 진정 크림을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 피부 진정에 효과적인 제품을 자주 추천합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 피부 진정에 관한 콘텐츠를 많이 다루어 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 피부 트러블 완화와 진정 효과에 대한 정보를 자주 공유합니다."""
},
{
    "query": "여행용 화장품을 홍보할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여행 시 필요한 화장품을 자주 소개하여 유용합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여행지에서 사용할 수 있는 제품에 대한 리뷰가 많습니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 다양한 여행지에서 화장품 사용법을 소개하여 도움이 됩니다."""
}
,{
    "query": "여행지에서 찍은 사진을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 다양한 여행지에서의 사진을 자주 공유하며, 촬영 기법이 뛰어납니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여행 스타일을 잘 소화하며, 힙한 감각으로 사진을 올립니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여러 장소에서 촬영한 멋진 사진을 자주 올리며, 팔로워들에게 큰 호응을 얻고 있습니다."""
},
{
    "query": "반응 지수가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워들과의 소통이 활발하여 반응 지수가 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 콘텐츠에 대한 반응이 좋고, 댓글 참여율이 높습니다.
---
influencer_id: 1
name: 코덕❤
reason: 꾸준한 피드백과 높은 참여율로 반응 지수가 우수합니다."""
},
{
    "query": "팔로워가 10000명이상인 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워 수가 많고, 다양한 콘텐츠를 꾸준히 올리며 인기가 높습니다.
---
influencer_id: 1
name: 코덕❤
reason: 뷰티 관련 콘텐츠로 팔로워 수가 빠르게 증가하고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 제품 리뷰와 팁을 통해 많은 팔로워를 보유하고 있습니다."""
},
{
    "query": "팔로워 수 대비 반응도가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워 수에 비해 댓글과 좋아요 수가 높은 반응도를 보입니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 적은 팔로워 수에도 불구하고 활발한 소통으로 반응도가 높습니다.
---
influencer_id: 31
name: 지는빈
reason: 팔로워 수는 적지만 댓글과 좋아요 수가 높은 인플루언서입니다."""
},
{
    "query": "가을철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 가을철 패션 아이템을 효과적으로 소개하며, 스타일링 팁도 제공합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 가을에 적합한 패션 아이템을 잘 소화하여 많은 사랑을 받고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 가을철에 어울리는 다양한 뷰티 제품을 소개합니다."""
},
{
    "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 신뢰도 높은 리뷰와 상세한 설명으로 많은 팔로워들에게 신뢰를 받고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 제품 사용 후기와 효과를 명확하게 전달하여 신뢰를 쌓고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 스킨케어 제품에 대한 전문가적인 리뷰로 많은 팔로워의 호평을 받고 있습니다."""
},
{
    "query": "저가형 스킨케어 제품을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 가성비 좋은 제품을 자주 추천하며, 실용적인 리뷰를 제공합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 저가형 제품을 소개하여 많은 관심을 받고 있습니다.
---
influencer_id: 36
name: 권지현
reason: 저렴하면서도 효과적인 스킨케어 제품에 대한 리뷰가 많습니다."""
},
{
    "query": "계절별 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 계절별로 변화하는 피부 관리법을 상세하게 설명합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 계절에 따라 적합한 스킨케어 제품을 잘 소개하여 많은 도움이 됩니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 계절별 제품 추천과 사용법을 잘 설명합니다."""
},
{
    "query": "여름철 패션 아이템을 효과적으로 홍보할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름에 어울리는 다양한 패션 아이템을 소개합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 아이템에 대한 리뷰가 많아 신뢰를 받고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름 시즌에 적합한 스타일링 팁과 패션 아이템을 잘 홍보합니다."""
},
{
    "query": "다양한 여행지를 소개하며 필수 아이템을 홍보하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여러 여행지에서 촬영한 사진과 필수 아이템을 잘 소개합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여행 중 유용한 아이템과 스타일을 소개하여 많은 사랑을 받고 있습니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 다양한 장소에서의 사진과 함께 필수 아이템을 추천합니다."""
}
,{
    "query": "팔로워와 친근한 소통이 가능한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 소통이 활발하여 신뢰도를 높이고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 자주 팔로워들과 소통하며 피드백을 적극 반영합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 친근한 소통으로 많은 팔로워들과의 유대감을 형성하고 있습니다."""
},
{
    "query": "광고 게시물의 참여도가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 광고 게시물에 대한 반응이 좋고, 많은 댓글과 좋아요를 받습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 광고 게시물에서 높은 참여율을 보이며, 팔로워들의 반응이 활발합니다.
---
influencer_id: 1
name: 코덕❤
reason: 광고 콘텐츠에 대한 피드백이 많아 참여도가 높습니다."""
},
{
    "query": "평균 댓글 수가 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 포스팅에 대한 댓글 수가 평균적으로 많아 소통이 활발합니다.
---
influencer_id: 1
name: 코덕❤
reason: 여러 게시물에서 높은 댓글 수를 기록하며 참여율이 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 게시물에 대한 댓글이 많아 반응이 뛰어납니다."""
},
{
    "query": "피드백이 활발한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 피드백에 대한 반응이 빠르며, 댓글을 통해 소통이 잘 이루어집니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워의 의견을 자주 반영하여 피드백이 활발합니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워들과의 소통을 중요시하며, 피드백에 민감하게 반응합니다."""
},
{
    "query": "겨울철 보습 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 겨울철 보습 제품에 대한 리뷰가 많아 신뢰도를 높이고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 스킨케어 루틴을 잘 설명하며, 보습 제품을 자주 홍보합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 보습 제품에 대한 전문적인 지식을 바탕으로 신뢰를 얻고 있습니다."""
},
{
    "query": "비건 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 비건 제품에 대한 리뷰가 많아 비건 팔로워들의 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 비건 화장품과 스킨케어 제품에 대한 설명이 자세하고 효과적입니다.
---
influencer_id: 34
name: Niya 김반야
reason: 비건 제품에 대한 경험과 사용기를 자주 공유하여 많은 관심을 받고 있습니다."""
},
{
    "query": "학생층 팔로워를 타깃으로 한 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 학생들에게 인기가 높은 뷰티 제품과 트렌드를 잘 소개합니다.
---
influencer_id: 1
name: 코덕❤
reason: 학생들이 선호하는 가성비 좋은 뷰티 제품을 자주 리뷰합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 학생들이 참고할 만한 스킨케어 루틴과 제품을 추천합니다."""
},
{
    "query": "친환경 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 친환경 뷰티 제품에 대한 콘텐츠가 많아 신뢰를 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 지속 가능한 제품을 강조하며 친환경성을 잘 홍보합니다.
---
influencer_id: 34
name: Niya 김반야
reason: 다양한 친환경 브랜드와 협업하여 제품을 소개하고 있습니다."""
},
{
    "query": "다양한 스킨케어 제품을 자주 리뷰하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 다양한 브랜드의 스킨케어 제품을 리뷰하며 많은 사랑을 받고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 스킨케어 제품에 대한 자세한 리뷰를 자주 올려 팔로워들에게 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여러 브랜드의 제품을 비교하며 리뷰를 제공하여 많은 인기를 끌고 있습니다."""
}
,{
    "query": "소통이 활발하고 팔로워의 피드백을 잘 반영하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 댓글과 DM을 통해 팔로워와 소통이 활발하며, 피드백을 적극 반영합니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워의 의견을 수렴하여 콘텐츠에 반영하는 모습을 보여줍니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워와의 소통이 원활하며, 피드백을 즉각적으로 반영합니다."""
},
{
    "query": "팔로워 수 대비 댓글 참여율이 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워 수에 비해 댓글 참여율이 높아, 활발한 소통을 보여줍니다.
---
influencer_id: 1
name: 코덕❤
reason: 많은 팔로워를 보유하면서도 댓글 수가 높아 반응이 좋습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 참여율이 높아 팔로워들과의 유대감을 잘 형성하고 있습니다."""
},
{
    "query": "겨울철 필수 스킨케어 제품을 잘 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 겨울철 보습 제품을 효과적으로 리뷰하며, 사용법을 잘 설명합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 스킨케어 루틴을 통해 필수 제품을 소개합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 겨울철 피부 관리 팁과 제품을 자주 포스팅하여 많은 인기를 끌고 있습니다."""
},
{
    "query": "패션 트렌드를 잘 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드를 반영한 스타일링을 자주 소개합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션 아이템을 활용해 트렌디한 룩을 잘 보여줍니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 트렌드에 대한 감각이 뛰어나고, 팔로워들과의 소통이 활발합니다."""
},
{
    "query": "여름철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수품을 다양하게 소개하며, 많은 팁을 제공합니다.
---
influencer_id: 1
name: 코덕❤
reason: 여름철 스킨케어와 관련된 필수 아이템을 자주 포스팅합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 피부 관리에 필수적인 제품을 소개하여 많은 인기를 끌고 있습니다."""
},
{
    "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 게시물에 대한 댓글이 많고, 댓글을 통해 소통이 활발합니다.
---
influencer_id: 1
name: 코덕❤
reason: 댓글 참여가 높아 활발한 소통이 이루어집니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글로 팔로워와의 소통이 활발하여 참여율이 높습니다."""
},
{
    "query": "겨울철 필수 아이템을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 겨울철 스킨케어와 관련된 필수 아이템을 잘 홍보합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수 아이템에 대한 유용한 정보를 자주 포스팅합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 겨울철 아이템에 대한 전문적인 설명으로 팔로워의 신뢰를 얻고 있습니다."""
},
{
    "query": "다양한 패션 아이템을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 아이템을 활용한 스타일링을 자주 보여줍니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션 아이템을 조합하여 독창적인 룩을 소개합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 트렌디한 패션 아이템을 자주 소개하여 많은 사랑을 받고 있습니다."""
}
,{
    "query": "가성비 좋은 뷰티 제품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 가성비 좋은 뷰티 제품을 적극적으로 추천하며, 리뷰가 신뢰성이 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 저렴한 뷰티 제품을 소개하며 팔로워들에게 인기를 끌고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 가성비 높은 뷰티 제품을 잘 홍보하여 많은 팔로워의 관심을 받고 있습니다."""
},
{
    "query": "신제품에 대한 호응이 좋은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 신제품 리뷰에 빠르게 반응하며, 피드백이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 신제품에 대한 리뷰가 활발하고, 반응이 좋습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 신제품을 적극적으로 소개하며, 팔로워의 반응이 좋습니다."""
},
{
    "query": "남성 스킨케어 제품을 주로 사용하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 스킨케어 제품을 자주 리뷰하며, 실용적인 팁을 제공합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 스킨케어 제품에 대한 정보와 사용법을 잘 설명합니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 남성 스킨케어 제품에 대한 리뷰를 통해 신뢰를 얻고 있습니다."""
},
{
    "query": "친환경 제품을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 16
name: 민들레
reason: 친환경 제품을 적극적으로 추천하며, 자연을 중요시하는 메시지를 전합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 친환경 뷰티 제품을 자주 소개하며 신뢰도를 높이고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 친환경 화장품과 관련된 제품을 소개하여 많은 관심을 받고 있습니다."""
},
{
    "query": "소통이 활발하고 팔로워의 피드백을 잘 반영하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 댓글과 DM을 통해 팔로워와 소통이 활발하며, 피드백을 적극 반영합니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워의 의견을 수렴하여 콘텐츠에 반영하는 모습을 보여줍니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워와의 소통이 원활하며, 피드백을 즉각적으로 반영합니다."""
},
{
    "query": "비건 화장품을 자주 사용하는 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 비건 화장품에 대한 리뷰를 자주 하며, 관심이 높습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 비건 화장품을 주로 사용하고 그에 대한 리뷰를 많이 합니다.
---
influencer_id: 34
name: Niya 김반야
reason: 비건 화장품에 대한 다양한 정보와 사용기를 공유하고 있습니다."""
},
{
    "query": "여름철 필수 아이템을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수품을 다양하게 소개하며, 많은 팁을 제공합니다.
---
influencer_id: 1
name: 코덕❤
reason: 여름철 스킨케어와 관련된 필수 아이템을 자주 포스팅합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 피부 관리에 필수적인 제품을 소개하여 많은 인기를 끌고 있습니다."""
},
{
    "query": "이벤트 참여가 활발하며 피드백 반응이 좋은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 이벤트에 자주 참여하며 팔로워의 피드백에 적극 반영합니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 이벤트에 참여하고 팔로워와의 소통이 활발합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 이벤트 참여와 피드백을 통해 팔로워들과의 유대감을 높이고 있습니다."""
},
{
    "query": "평균 좋아요 수가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 평균적으로 높은 좋아요 수를 기록하여 인기를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 포스팅마다 높은 좋아요 수를 기록하여 많은 사랑을 받고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 꾸준히 높은 좋아요 수를 기록하며 팔로워와의 소통이 활발합니다."""
},
{
    "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 댓글 소통이 활발하며, 자주 피드백을 반영합니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워와의 소통이 원활하여 많은 피드백을 받습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 팔로워와 자주 소통하며 피드백을 잘 반영합니다."""
}
,{
    "query": "여행지에서 찍은 사진을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여행지에서 다양한 스타일의 사진을 잘 찍으며, 여행 필수 아이템을 소개합니다.
---
influencer_id: 37
name: 민주(정문츄)
reason: 여행 중 촬영한 일상적인 모습들을 잘 표현하여 여행 아이템을 자연스럽게 홍보합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여러 여행지를 배경으로 한 패션 스타일링이 뛰어나 여행 사진이 인상적입니다."""
},
{
    "query": "피부 개선에 좋은 뷰티 제품을 리뷰하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 피부 개선을 위한 다양한 뷰티 제품을 자주 리뷰하여 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피부 개선 효과가 뛰어난 제품에 대한 리뷰가 많아 많은 이들에게 추천받고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 피부 개선을 위한 전문적인 조언과 함께 제품을 소개하여 신뢰감을 줍니다."""
},
{
    "query": "남성 패션을 다루는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션에 대한 다양한 스타일을 자주 선보이며 많은 인기를 얻고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 패션 트렌드에 대한 정보를 자주 포스팅하여 많은 팔로워들에게 사랑받고 있습니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 남성 패션 스타일링을 잘 소개하여 신뢰를 받고 있습니다."""
},
{
    "query": "다양한 뷰티 브랜드와의 협업이 활발한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여러 뷰티 브랜드와의 협업을 통해 다양한 제품을 소개하며 많은 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 뷰티 브랜드와의 협업을 통해 제품을 자연스럽게 홍보합니다.
---
influencer_id: 1
name: 코덕❤
reason: 협업을 통해 신뢰성 높은 뷰티 제품을 자주 소개하여 많은 관심을 받고 있습니다."""
},
{
    "query": "가성비 좋은 스킨케어 제품을 잘 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 가성비 좋은 스킨케어 제품에 대한 정보를 많이 공유하며 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 저렴하면서 효과적인 스킨케어 제품을 추천하여 팔로워들에게 많은 사랑을 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 가성비 스킨케어 제품을 리뷰하며 많은 정보를 제공합니다."""
},
{
    "query": "여름철 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 여름철 피부 관리 팁을 자주 공유하여 많은 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름 스킨케어 루틴을 잘 설명하며, 팔로워들에게 유용한 정보를 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여름철 스킨케어 제품과 루틴을 소개하여 많은 도움이 됩니다."""
},
{
    "query": "소통이 활발한 일상 카테고리 인플루언서를 추천해줘.",
    "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 팔로워와의 댓글 소통이 활발하며, 다양한 일상 콘텐츠를 공유합니다.
---
influencer_id: 31
name: 지는빈
reason: 팔로워와의 소통을 중요시하며, 일상적인 이야기로 친근감을 줍니다.
---
influencer_id: 17
name: 봄웜라이트 코덕 셀레나
reason: 일상적인 내용을 공유하며 팔로워들과 활발하게 소통합니다."""
},
{
    "query": "겨울철 보습 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 겨울철 필수 보습 제품을 적극적으로 소개하여 인기를 끌고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 겨울철 보습 제품에 대한 정보와 리뷰를 많이 공유합니다.
---
influencer_id: 12
name: 마르 Marr
reason: 겨울철 피부 관리에 적합한 보습 제품을 잘 추천합니다."""
},
{
    "query": "저자극 스킨케어 제품을 주로 사용하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 저자극 제품에 대한 정보와 리뷰를 자주 올리며 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피부에 자극이 적은 스킨케어 제품을 주로 소개합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 저자극 스킨케어 제품을 많이 사용하여 많은 팔로워에게 추천합니다."""
}
,{
    "query": "피부 진정 크림을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 피부 진정에 효과적인 제품을 자주 리뷰하며 신뢰를 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피부 진정을 위해 사용하는 다양한 제품을 소개하여 많은 인기를 끌고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 피부 진정 크림과 관련된 유용한 정보를 공유하여 팔로워들에게 도움을 줍니다."""
},
{
    "query": "반응 지수가 높은 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 콘텐츠에 대한 반응이 활발하며, 다양한 스타일을 자주 공유합니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 관련 콘텐츠에 높은 반응을 얻어 많은 팔로워에게 사랑받고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 트렌드에 대한 정보를 제공하여 많은 팔로워의 반응을 얻고 있습니다."""
},
{
    "query": "겨울철 패션 아이템을 효과적으로 홍보할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 겨울철 필수 패션 아이템을 자주 소개하여 인기를 끌고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 겨울철 스타일링에 적합한 패션 아이템을 자연스럽게 홍보합니다.
---
influencer_id: 39
name: 솔솔씨
reason: 겨울 패션에 대한 다양한 아이템을 소개하여 많은 인기를 얻고 있습니다."""
},
{
    "query": "팔로워 수가 많고 평균 댓글 수가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 많은 팔로워를 보유하며 댓글 참여도도 활발하여 인기 있는 인플루언서입니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 평균 댓글 수가 높아 팔로워와의 소통이 활발합니다.
---
influencer_id: 1
name: 코덕❤
reason: 많은 팔로워와 활발한 댓글 소통으로 인기를 끌고 있습니다."""
},
{
    "query": "신뢰할 수 있는 스킨케어 리뷰를 제공하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 스킨케어 제품에 대한 신뢰할 수 있는 리뷰를 자주 제공합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 피부 관리에 대한 전문적인 리뷰로 많은 신뢰를 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 스킨케어 제품에 대한 정보와 리뷰를 통해 신뢰성을 높이고 있습니다."""
},
{
    "query": "트렌디한 패션 아이템을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드를 반영한 아이템을 자주 소개하여 많은 인기를 얻고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 아이템에 대한 트렌드 정보를 적극적으로 공유합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 트렌디한 패션 아이템을 소개하여 팔로워들에게 인기를 끌고 있습니다."""
},
{
    "query": "여름철 필수품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수품을 자주 리뷰하여 많은 관심을 받고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 여름철 필수 아이템에 대한 정보와 팁을 제공합니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 필수품을 잘 소개하며, 많은 이들의 관심을 끌고 있습니다."""
},
{
    "query": "가성비 좋은 뷰티 제품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 가성비 뷰티 제품을 자주 소개하여 많은 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 저렴한 가격에 좋은 효과를 가진 제품을 많이 추천합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 가성비 뷰티 제품을 리뷰하며 많은 도움을 주고 있습니다."""
},
{
    "query": "팔로워가 10000명이상인 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 많은 팔로워를 보유하여 높은 인지도와 신뢰도를 자랑합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워 수가 많아 많은 이들에게 영향을 미치고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워 수가 많고 다양한 정보를 공유하여 신뢰를 얻고 있습니다."""
},
{
    "query": "피부 타입별 스킨케어 루틴을 잘 설명하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 피부 타입에 맞는 스킨케어 루틴을 자주 소개하여 많은 도움을 줍니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 피부 타입에 맞춘 스킨케어 팁을 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 피부 타입별 관리법에 대한 유용한 정보를 공유합니다."""
}
,{
    "query": "팔로워 수 대비 평균 댓글 수가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 팔로워 수에 비해 평균 댓글 수가 높은 편으로, 팔로워들과의 소통이 활발합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 트렌디한 패션을 소개하며, 댓글 참여율이 높은 편입니다. 참고: 질문에 대한 관련 카테고리가 부족해 다른 기준으로 추천하였습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 뷰티 콘텐츠를 통해 댓글 참여가 활발한 인플루언서입니다."""
},

{
    "query": "계절에 따라 트렌디한 패션을 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 계절별 패션 스타일링을 잘 보여주며, 트렌디한 아이템을 소개합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 계절별 패션을 자연스럽게 홍보하고 소통하는 인플루언서입니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션을 주로 다루며 계절에 맞는 스타일을 소개합니다."""
},

{
    "query": "평균 댓글 수가 15개 이상인 인플루언서를 추천해줘.",
    "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 댓글 참여율이 높아, 평균 댓글 수가 15개 이상입니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 콘텐츠를 통해 평균 댓글 수가 높은 편입니다. 참고: 질문에 대한 관련 카테고리가 부족해 다른 기준으로 추천하였습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 평균 댓글 수가 높은 인플루언서입니다."""
},

{
    "query": "일상에서 사용하는 생활용품을 잘 홍보하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 일상적인 제품을 자연스럽게 소개하며 소통하는 인플루언서입니다.
---
influencer_id: 31
name: 지는빈
reason: 다양한 생활용품을 리뷰하며 팔로워와의 소통이 활발합니다.
---
influencer_id: 8
name: 권지현
reason: 일상 속에서 사용하는 제품을 자주 리뷰하고 있습니다."""
},

{
    "query": "가성비 좋은 뷰티 제품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 가성비 뷰티 제품을 자주 소개하여 많은 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 저렴한 가격에 좋은 효과를 가진 제품을 많이 추천합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 가성비 뷰티 제품을 리뷰하며 많은 도움을 주고 있습니다."""
}
,{
    "query": "댓글 참여율이 높고 소통이 활발한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 댓글 참여율이 높고 팔로워들과의 소통이 활발하여 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글과 소통이 활발해 많은 팔로워들이 활발히 반응합니다. 참고: 질문에 대한 관련 카테고리가 부족해 다른 기준으로 추천하였습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 팔로워들과 소통이 원활하며, 댓글 참여가 높은 인플루언서입니다."""
},

{
    "query": "반응 지수가 높아 뷰티 제품 홍보에 적합한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 높은 반응 지수를 기반으로 다양한 뷰티 제품을 효과적으로 홍보합니다.
---
influencer_id: 1
name: 코덕❤
reason: 뷰티 제품 리뷰에서 반응 지수가 높아 신뢰를 얻고 있습니다.
---
influencer_id: 8
name: 권지현
reason: 반응이 활발하여 뷰티 제품을 자연스럽게 홍보하는 데 적합합니다."""
},

{
    "query": "다양한 패션 브랜드와 자주 협업하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 여러 패션 브랜드와의 협업을 통해 다양한 콘텐츠를 만들어내고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 패션 브랜드와의 협업 경험이 많아 신뢰도가 높은 인플루언서입니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 브랜드와 협업하며 패션 아이템을 효과적으로 홍보합니다."""
},

{
    "query": "여름철 여행지에서 사용하기 좋은 제품을 홍보하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 여행 관련 콘텐츠를 통해 여름철 필수 아이템을 소개합니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 여름철 여행지에서 사용할 수 있는 제품을 자연스럽게 홍보합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름 여행에 적합한 패션 아이템을 많이 소개합니다."""
},

{
    "query": "팔로워 수 대비 평균 좋아요가 높은 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 팔로워 수에 비해 평균 좋아요 수가 높고, 콘텐츠가 반응이 좋습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 아이템을 소개하며 평균 좋아요 수가 높은 편입니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 평균 좋아요 수가 높은 인플루언서입니다."""
},

{
    "query": "최신 트렌드를 자주 다루며 신제품 반응이 좋은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 최신 뷰티 트렌드를 반영하며 신제품 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 새로운 트렌드와 신제품을 다루며 팔로워 반응이 높은 인플루언서입니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 패션 트렌드를 잘 반영하여 신제품을 홍보합니다."""
},

{
    "query": "가성비 좋은 뷰티 제품을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 가성비 뷰티 제품을 자주 소개하여 많은 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 저렴한 가격에 좋은 효과를 가진 제품을 많이 추천합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 가성비 뷰티 제품을 리뷰하며 많은 도움을 주고 있습니다."""
},

{
    "query": "친환경 제품 리뷰 경험이 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 친환경 제품에 대한 리뷰를 자주 작성하며 신뢰도가 높습니다.
---
influencer_id: 16
name: 민들레
reason: 자연친화적인 제품을 소개하며 팔로워들의 반응이 좋습니다.
---
influencer_id: 8
name: 권지현
reason: 친환경 제품을 적극적으로 소개하고 소통하는 인플루언서입니다."""
},

{
    "query": "평균 댓글 수가 20개 이상인 인플루언서를 추천해줘.",
    "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 댓글 참여율이 높아, 평균 댓글 수가 20개 이상입니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 콘텐츠를 통해 평균 댓글 수가 높은 편입니다. 참고: 질문에 대한 관련 카테고리가 부족해 다른 기준으로 추천하였습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 평균 댓글 수가 높은 인플루언서입니다."""
},

{
    "query": "다양한 장소에서 제품을 자연스럽게 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 여행 관련 콘텐츠를 통해 다양한 장소에서 제품을 자연스럽게 소개합니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 일상적인 장소에서 제품을 자연스럽게 소개하며 소통합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 아이템을 다양한 장소에서 자연스럽게 홍보하는 인플루언서입니다."""
}
,{
    "query": "학생층 팔로워가 많은 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 학생들에게 인기가 많고 가성비 좋은 뷰티 제품을 자주 소개합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 많은 학생 팔로워와 소통하며 다양한 뷰티 제품을 추천합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 학생층에게 큰 인기를 끌며, 소통이 활발한 인플루언서입니다."""
},

{
    "query": "남성 팔로워와의 소통이 활발한 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션에 대한 소통이 활발하며 많은 팔로워가 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 팔로워와의 소통을 중요시하며 다양한 패션을 소개합니다.
---
influencer_id: 39
name: 솔솔씨
reason: 남성 팔로워들과의 소통이 활발하여 인기를 끌고 있습니다."""
},

{
    "query": "평균 좋아요 수가 높아 가성비 제품 홍보에 적합한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 가성비 좋은 제품을 홍보하며 평균 좋아요 수가 높습니다.
---
influencer_id: 1
name: 코덕❤
reason: 가성비 제품을 소개하면서 많은 좋아요를 받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 가성비 뷰티 제품을 소개하며 반응이 좋습니다."""
},

{
    "query": "반응 지수가 높고 팔로워 수가 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 높은 팔로워 수와 함께 반응 지수가 높아 신뢰를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 많은 팔로워를 보유하고 있으며, 반응이 좋은 콘텐츠를 제공합니다.
---
influencer_id: 8
name: 권지현
reason: 팔로워 수가 많고, 다양한 콘텐츠에서 반응이 좋습니다."""
},

{
    "query": "친환경 패션 아이템을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 친환경 패션 아이템에 대한 소개가 많고 소통이 활발합니다.
---
influencer_id: 16
name: 민들레
reason: 지속 가능한 패션을 자주 소개하며, 많은 인기를 끌고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 친환경적인 패션 브랜드와의 협업을 통해 지속 가능한 스타일을 보여줍니다."""
},

{
    "query": "여행용 가방을 홍보하기에 적합한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 여행 콘텐츠를 자주 다루며 가방을 효과적으로 홍보합니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 여행 관련 제품을 소개하며 가방 홍보에 적합합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여행 스타일을 잘 살려 가방을 자연스럽게 소개합니다."""
},

{
    "query": "최신 스킨케어 트렌드를 자주 반영하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 최신 트렌드를 잘 반영하여 스킨케어 제품을 소개합니다.
---
influencer_id: 1
name: 코덕❤
reason: 최신 스킨케어 제품과 트렌드를 자주 다루며 반응이 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 스킨케어 제품을 소개하며 최신 트렌드를 반영합니다."""
},

{
    "query": "계절별 화장품을 추천할 수 있는 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 계절에 맞는 화장품 추천을 잘 하며, 팔로워들에게 인기가 많습니다.
---
influencer_id: 1
name: 코덕❤
reason: 계절별 스킨케어 및 메이크업 제품을 소개하여 많은 호응을 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 계절별 뷰티 제품을 소개하여 많은 도움을 주고 있습니다."""
},

{
    "query": "평균 댓글이 10개 이상이며 팔로워 반응이 좋은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 댓글 참여율이 높고, 팔로워 반응이 매우 좋습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 콘텐츠로 평균 댓글 수가 10개 이상이며 반응이 활발합니다. 참고: 질문에 대한 관련 카테고리가 부족해 다른 기준으로 추천하였습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 콘텐츠에서 평균 댓글 수가 높아 소통이 잘 이루어집니다."""
},{
    "query": "일상에서 자주 사용하는 저렴한 제품을 리뷰하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 저렴한 생활용품을 자주 리뷰하며 많은 팔로워에게 인기가 많습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 일상적인 제품들을 저렴하게 리뷰하여 많은 도움을 줍니다.
---
influencer_id: 1
name: 코덕❤
reason: 저렴하고 효과적인 제품 리뷰로 학생층에게 인기가 많습니다."""
},

{
    "query": "여름철 야외 활동에 적합한 제품을 잘 홍보할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 여름철 야외 활동과 관련된 제품을 잘 홍보합니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 여름철 액티비티에 적합한 제품을 효과적으로 소개합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 야외 활동에 적합한 뷰티 및 패션 제품을 자주 추천합니다."""
},

{
    "query": "팔로워와의 친밀한 소통이 활발한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워들과의 소통이 활발하여 친근한 이미지가 많습니다.
---
influencer_id: 1
name: 코덕❤
reason: 팔로워와의 소통을 중요시하며 친근하게 다가갑니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 다양한 소통 방식으로 팔로워들과의 관계를 잘 유지합니다."""
},

{
    "query": "피드백 반응이 빠르며 신뢰도가 높은 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 팔로워의 피드백을 빠르게 반영하며 신뢰도가 높습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 신뢰도가 높고, 패션 피드백에 빠르게 반응합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 고객 피드백을 잘 반영하여 신뢰를 얻고 있습니다."""
},

{
    "query": "뷰티 제품 중에서도 피부 타입별 추천을 잘하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 피부 타입에 맞는 제품을 잘 추천하여 많은 팔로워의 신뢰를 얻고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 피부 타입별 맞춤형 스킨케어 추천으로 팔로워들의 많은 호응을 얻습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 피부 타입별로 상세한 리뷰를 제공하여 도움이 됩니다."""
},

{
    "query": "남성 패션 아이템을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 다양한 남성 패션 아이템을 자주 소개하여 팔로워와의 소통이 활발합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 패션 아이템에 대한 소통이 활발하며 인기가 많습니다.
---
influencer_id: 39
name: 솔솔씨
reason: 다양한 남성 패션 아이템을 추천하며 트렌디한 스타일을 제공합니다."""
},

{
    "query": "반응 지수가 높아 광고주 신뢰도가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 광고주와의 협업 경험이 많고, 반응 지수가 높아 신뢰도가 높습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 광고주와의 신뢰를 바탕으로 다양한 협업을 진행하고 있습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 높은 반응 지수로 광고주 신뢰도가 매우 높은 인플루언서입니다."""
},

{
    "query": "평균 좋아요 수가 높은 여행 카테고리 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 여행 관련 콘텐츠에서 평균 좋아요 수가 높습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여행 사진에서 많은 좋아요를 받으며 인기가 높습니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 여행 콘텐츠에서 반응이 뛰어나 평균 좋아요 수가 많습니다."""
},

{
    "query": "자연스러운 일상 제품 리뷰가 인상적인 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 자연스러운 리뷰 스타일로 일상 제품을 잘 소개합니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 일상 제품을 자연스럽게 리뷰하여 많은 호응을 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 일상적인 제품을 자연스럽게 리뷰하여 신뢰를 쌓고 있습니다."""
},

{
    "query": "댓글과 좋아요 수가 높아 반응이 좋은 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 댓글과 좋아요 수가 많아 반응이 뛰어난 인플루언서입니다.
---
influencer_id: 1
name: 코덕❤
reason: 높은 반응 지수로 댓글과 좋아요 수가 많습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 다양한 뷰티 제품을 소개하며 반응이 좋습니다."""
}
,
{
    "query": "학생층을 타깃으로 한 뷰티 제품 홍보에 적합한 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 학생들에게 인기가 높은 뷰티 제품을 많이 소개합니다.
---
influencer_id: 1
name: 코덕❤
reason: 학생들을 대상으로 한 뷰티 제품을 자주 추천하여 호응을 얻고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 저렴하면서도 효과적인 뷰티 제품을 리뷰하여 학생층에게 인기가 많습니다."""
},

{
    "query": "다양한 메이크업 스타일을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 다양한 메이크업 스타일을 자주 소개하여 팔로워의 호응을 얻고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여러 가지 메이크업 룩을 선보이며 인기 있는 인플루언서입니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 트렌디한 메이크업 스타일을 자주 소개하여 많은 관심을 끌고 있습니다."""
},

{
    "query": "가성비 좋은 여름철 필수 패션 아이템을 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 여름철 필수 아이템을 가성비 좋게 소개하여 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름철 필수 패션 아이템을 저렴하게 소개하여 많은 호응을 얻고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름철 패션 아이템에 대한 리뷰가 많아 가성비가 좋습니다."""
},

{
    "query": "남성 팔로워 비율이 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 남성 패션 아이템을 자주 소개하여 남성 팔로워 비율이 높습니다.
---
influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 남성 패션을 주로 다루어 남성 팔로워가 많습니다.
---
influencer_id: 39
name: 솔솔씨
reason: 남성 팔로워들에게 많은 사랑을 받고 있는 인플루언서입니다."""
},

{
    "query": "댓글 참여율이 높고 반응이 좋은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 댓글 참여율이 높아 팔로워와의 소통이 활발합니다.
---
influencer_id: 1
name: 코덕❤
reason: 댓글 반응이 뛰어나 많은 소통을 이루고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 다양한 콘텐츠로 댓글 참여를 유도하여 반응이 좋습니다."""
},

{
    "query": "평균 좋아요가 200개 이상인 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 평균 좋아요 수가 높아 많은 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 콘텐츠에서 평균 좋아요가 200개 이상으로 반응이 좋습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 관련 포스팅에서 높은 평균 좋아요 수를 기록하고 있습니다."""
},

{
    "query": "비건 스킨케어 제품을 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 비건 및 자연 유래 제품을 자주 소개하여 인기가 많습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 비건 스킨케어 제품을 잘 홍보하여 많은 신뢰를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 비건 제품에 대한 관심이 높아 관련 콘텐츠가 많습니다."""
},

{
    "query": "다양한 장소에서 제품을 자주 소개하는 여행 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 다양한 여행지를 배경으로 제품을 잘 소개하여 팔로워의 호응을 얻고 있습니다.
---
influencer_id: 13
name: 조화 ZOHWA
reason: 여러 여행지에서 촬영한 사진과 제품 소개로 인기를 끌고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 장소에서 찍은 사진으로 제품을 자연스럽게 홍보합니다."""
},

{
    "query": "팔로워와의 소통이 활발하며 신뢰도가 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 소통이 활발하고 신뢰도가 높아 많은 팔로워에게 사랑받고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 친밀한 소통이 잘 이루어져 인기가 많습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 팔로워와의 신뢰 관계를 중요시하여 많은 인기를 끌고 있습니다."""
},

{
    "query": "비건 및 친환경 화장품을 사용하는 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 비건 및 친환경 화장품에 대한 관심이 높아 관련 콘텐츠가 많습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 비건 화장품을 잘 홍보하여 팔로워들의 신뢰를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 비건 및 친환경 제품에 대한 리뷰가 다양하게 이루어집니다."""
},{
    "query": "여름철 스킨케어 제품을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 여름철 스킨케어 제품에 대한 다양한 리뷰를 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여름철에 적합한 스킨케어 제품을 자주 소개하여 인기를 끌고 있습니다."""
},

{
    "query": "소통이 활발하고 팔로워의 피드백을 잘 반영하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 소통이 활발하여 피드백을 잘 반영합니다.
---
influencer_id: 1
name: 코덕❤
reason: 댓글과 소통을 통해 피드백을 적극적으로 반영하는 인플루언서입니다."""
},

{
    "query": "피부 타입별 스킨케어 제품을 잘 추천하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 다양한 피부 타입에 맞는 스킨케어 제품을 추천하는 데 특화되어 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 피부 타입에 따른 스킨케어 팁을 자주 공유하여 많은 도움을 주고 있습니다."""
},

{
    "query": "여름철 필수 뷰티 아이템을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 여름철 뷰티 아이템에 대한 리뷰가 많아 홍보에 적합합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여름 필수 뷰티 제품을 효과적으로 소개하여 반응이 좋습니다."""
},

{
    "query": "겨울철 필수 스킨케어 제품을 추천할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 겨울철 필수 스킨케어 제품에 대한 정보를 자주 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 겨울철에 필요한 스킨케어 제품을 많이 추천하여 신뢰를 얻고 있습니다."""
},

{
    "query": "일상에서 사용하는 생활용품을 잘 홍보하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 다양한 생활용품을 소개하여 일상에서 유용하게 활용할 수 있도록 합니다.
---
influencer_id: 1
name: 코덕❤
reason: 생활용품을 리뷰하며 많은 팔로워의 공감을 얻고 있습니다."""
},

{
    "query": "신제품에 대한 호응이 좋은 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 신제품 패션 아이템에 대한 반응이 좋아 인기가 높습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 신제품 패션에 대한 리뷰가 많은 팔로워의 호응을 얻고 있습니다."""
},

{
    "query": "자연스럽게 제품을 리뷰하며 가성비가 좋은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 가성비 좋은 제품에 대한 자연스러운 리뷰로 많은 인기를 끌고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 가성비 제품을 자연스럽게 소개하여 많은 호응을 얻고 있습니다."""
},

{
    "query": "가성비 좋은 스킨케어 제품을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 가성비 좋은 스킨케어 제품을 자주 소개하여 많은 관심을 받고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 다양한 가성비 스킨케어 제품을 리뷰하여 호응을 얻고 있습니다."""
}
,
{
    "query": "비건 스킨케어 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 비건 스킨케어 제품에 대한 깊이 있는 리뷰를 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 비건 제품을 주제로 한 다양한 콘텐츠로 신뢰를 얻고 있습니다."""
},

{
    "query": "피드백이 잘 반영되는 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 팔로워의 피드백을 적극적으로 반영하며 소통이 활발합니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 댓글을 통해 받은 피드백을 제품 리뷰에 잘 반영합니다."""
},

{
    "query": "신제품 리뷰가 빠르고 반응이 좋은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 신제품을 신속하게 리뷰하며 팔로워의 높은 반응을 얻고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 최신 신제품에 대한 리뷰가 빨라 많은 인기를 끌고 있습니다."""
},

{
    "query": "트렌디한 패션 아이템을 자주 소개하는 남성 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 최신 패션 트렌드를 반영한 아이템을 자주 소개하여 인기를 끌고 있습니다.
---
influencer_id: 32
name: 장홍석 (홍또기)
reason: 힙한 스타일의 패션 아이템을 많이 소개하여 남성 팔로워에게 인기가 많습니다."""
},

{
    "query": "반응 지수가 높고 팔로워 수가 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 활발한 소통으로 반응 지수가 높고 팔로워 수가 많습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 콘텐츠로 반응 지수를 높이며 많은 팔로워를 보유하고 있습니다."""
},

{
    "query": "여름철 필수 뷰티 아이템을 효과적으로 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여름철 뷰티 아이템에 대한 리뷰가 많아 효과적인 홍보가 가능합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 여름철 필수 뷰티 제품을 자주 소개하여 신뢰를 얻고 있습니다."""
},

{
    "query": "학생층 팔로워를 타깃으로 한 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 31
name: 지는빈
reason: 학생들이 선호하는 스타일을 많이 소개하여 인기가 높습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 트렌디한 패션 아이템을 소개하여 학생층에게 많은 인기를 얻고 있습니다."""
},

{
    "query": "여름철 필수 패션 아이템을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름 패션 아이템을 자주 소개하여 많은 관심을 받고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름철 필수 패션 아이템에 대한 리뷰가 많아 효과적으로 홍보할 수 있습니다."""
},

{
    "query": "일상에서 사용하는 제품을 자주 리뷰하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 일상에서 사용하기 좋은 다양한 제품을 자주 리뷰합니다.
---
influencer_id: 31
name: 지는빈
reason: 일상 속에서 사용하는 제품을 꾸준히 소개하여 많은 공감을 얻고 있습니다."""
}
,{
    "query": "가성비 좋은 뷰티 제품을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 가성비 뷰티 제품을 자주 소개하여 많은 인기를 끌고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 저렴한 가격에 좋은 효과를 가진 제품을 많이 추천합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 가성비 뷰티 제품을 리뷰하며 많은 도움을 주고 있습니다."""
},

{
    "query": "여름철 필수 스킨케어 제품을 잘 홍보할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 여름철 스킨케어 제품을 효과적으로 홍보하며 실용적인 정보를 제공합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 여름철 스킨케어 팁과 제품을 소개하여 신뢰를 얻고 있습니다."""
},

{
    "query": "학생층 팔로워에게 인기 있는 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 학생들에게 인기 있는 뷰티 제품을 자주 소개합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 젊은층을 겨냥한 다양한 뷰티 팁과 제품 리뷰로 인기를 끌고 있습니다."""
},

{
    "query": "여름철 필수 패션 아이템을 소개할 수 있는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 9
name: 옷미새 이수 eesoo
reason: 여름 패션 아이템에 대한 다양한 콘텐츠를 제공합니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여름 패션 아이템을 트렌디하게 소개하여 관심을 끌고 있습니다."""
},

{
    "query": "일상에서 사용하는 생활용품을 잘 홍보하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 13
name: 조화 ZOHWA
reason: 일상에서 사용하는 다양한 생활용품을 자주 리뷰합니다.
---
influencer_id: 31
name: 지는빈
reason: 실용적인 생활용품 리뷰로 많은 팔로워의 공감을 얻고 있습니다."""
},

{
    "query": "트렌디한 패션 아이템을 자주 소개하는 여성 인플루언서를 추천해줘.",
    "answer": """influencer_id: 8
name: 권지현
reason: 최신 트렌드의 패션 아이템을 자주 소개하여 많은 관심을 받고 있습니다.
---
influencer_id: 35
name: 옷미새 이수 eesoo
reason: 트렌디한 패션 스타일링으로 여성 팔로워들에게 인기가 많습니다."""
},

{
    "query": "소통이 활발한 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 팔로워와의 활발한 소통으로 인기를 끌고 있습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 댓글을 통해 소통하며 팔로워의 피드백을 잘 반영합니다."""
},

{
    "query": "학생층 팔로워가 많은 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 트렌디한 패션 아이템으로 학생들에게 큰 인기를 얻고 있습니다.
---
influencer_id: 31
name: 지는빈
reason: 학생들이 선호하는 스타일을 자주 소개하여 인기가 많습니다."""
},

{
    "query": "계절에 맞는 패션 아이템을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 계절별 트렌디한 패션 아이템을 소개하여 많은 사랑을 받고 있습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 계절별 패션 아이템을 자연스럽게 소개하여 팔로워의 반응이 좋습니다."""
},

{
    "query": "반응 지수가 높고 소통이 잘 되는 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 활발한 소통으로 반응 지수가 높아 많은 신뢰를 얻고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 뷰티 제품 리뷰로 소통이 활발하며 반응이 좋습니다."""
}
,{
    "query": "비건 화장품을 자주 사용하는 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 36
name: 권지현
reason: 비건 화장품에 대한 다양한 정보를 제공하여 관심을 끌고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 비건 및 자연 유래 제품을 자주 사용하는 뷰티 인플루언서로 신뢰를 얻고 있습니다."""
},

{
    "query": "평균 댓글 수가 높은 패션 인플루언서를 추천해줘.",
    "answer": """influencer_id: 32
name: 장홍석 (홍또기)
reason: 패션에 대한 다양한 콘텐츠로 평균 댓글 수가 높습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 스타일리시한 패션 아이템을 소개하며 댓글 참여가 활발합니다."""
},

{
    "query": "가성비 높은 스킨케어 제품을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 가성비 좋은 스킨케어 제품을 자주 리뷰하여 많은 관심을 받고 있습니다.
---
influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 저렴한 스킨케어 제품을 소개하여 팔로워들에게 인기가 높습니다."""
},

{
    "query": "여름철 필수 패션 아이템을 효과적으로 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 38
name: 데일리룩 패션 / 한정우
reason: 여름철 패션 아이템에 대한 트렌디한 정보를 제공합니다.
---
influencer_id: 8
name: 권지현
reason: 여름 패션 아이템을 자주 소개하며 신뢰를 얻고 있습니다."""
},

{
    "query": "신제품 리뷰가 빠르고 반응이 좋은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 12
name: 마르 Marr
reason: 신제품에 대한 리뷰를 빠르게 진행하여 인기를 끌고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 다양한 신제품 리뷰로 빠른 반응을 얻고 있습니다."""
},

{
    "query": "소통이 활발한 여행 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 여행 관련 콘텐츠를 통해 팔로워와 활발한 소통을 이어가고 있습니다.
---
influencer_id: 31
name: 지는빈
reason: 다양한 여행지를 소개하며 댓글 소통이 활발합니다."""
},

{
    "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 아이템으로 댓글 참여율이 높은 인플루언서입니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 댓글 참여가 활발하여 많은 반응을 얻고 있습니다."""
},

{
    "query": "신뢰도가 높은 화장품 리뷰를 제공하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 1
name: 코덕❤
reason: 화장품 리뷰에 대한 신뢰도가 높아 많은 팔로워의 사랑을 받고 있습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 자세한 리뷰로 신뢰성을 높이고 있습니다."""
},

{
    "query": "패션 잡지를 자주 다루는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 패션 잡지 콘텐츠를 자주 다루며 트렌드를 소개합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 잡지와 연계한 스타일링 팁을 제공합니다."""
}
,{
    "query": "피드백 반영이 빠르고 친절한 설명을 제공하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 36
name: 권지현
reason: 피드백에 대한 반응이 빠르고 친절한 소통으로 신뢰를 얻고 있습니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글에 대한 세심한 답변과 친절한 설명으로 호평을 받고 있습니다."""
},

{
    "query": "여름철 필수 뷰티 제품을 잘 홍보할 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 여름철 뷰티 제품을 효과적으로 소개하여 인기가 높습니다.
---
influencer_id: 10
name: 코덕 여쿨라🎀
reason: 여름철 뷰티 필수품을 자주 홍보하여 관심을 끌고 있습니다."""
},

{
    "query": "여름철 스킨케어 제품을 자주 소개하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 11
name: 🌸소플라🌸봄웜
reason: 여름철 스킨케어 제품에 대한 정보를 자주 제공하고 있습니다.
---
influencer_id: 1
name: 코덕❤
reason: 다양한 여름철 스킨케어 팁과 제품을 소개하고 있습니다."""
},

{
    "query": "여행용 화장품을 주로 홍보하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 37
name: 민주(정문츄)
reason: 여행 관련 화장품에 대한 정보를 자주 공유하고 있습니다.
---
influencer_id: 4
name: 장홍석 (홍또기)
reason: 여행지에서 사용할 수 있는 화장품을 소개하며 반응이 좋습니다."""
},

{
    "query": "학생층 팔로워를 타깃으로 한 뷰티 인플루언서를 추천해줘.",
    "answer": """influencer_id: 5
name: 민주(정문츄)
reason: 학생층을 대상으로 한 뷰티 제품 리뷰가 많습니다.
---
influencer_id: 1
name: 코덕❤
reason: 학생들이 선호하는 가성비 좋은 제품을 소개하여 인기를 끌고 있습니다."""
},

{
    "query": "패션 관련 제품을 자주 홍보하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 4
name: 장홍석 (홍또기)
reason: 다양한 패션 아이템을 자주 소개하며 트렌디한 정보를 제공합니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 패션 아이템을 다양하게 홍보하여 팔로워의 관심을 끌고 있습니다."""
},

{
    "query": "피드백을 잘 반영하는 인플루언서를 추천해줘.",
    "answer": """influencer_id: 36
name: 권지현
reason: 피드백을 빠르게 반영하며 팔로워와의 소통이 활발합니다.
---
influencer_id: 5
name: 민주(정문츄)
reason: 댓글 피드백에 신속하게 반응하여 신뢰를 얻고 있습니다."""
},

{
    "query": "댓글 참여율이 높은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 32
name: 장홍석 (홍또기)
reason: 댓글 참여율이 높은 패션 콘텐츠로 인기가 많습니다.
---
influencer_id: 9
name: 옷미새 이수 eesoo
reason: 다양한 패션 아이템을 소개하며 댓글 참여가 활발합니다."""
},

{
    "query": "반응이 활발하며 댓글 수가 많은 인플루언서를 추천해줘.",
    "answer": """influencer_id: 36
name: 권지현
reason: 다양한 콘텐츠로 반응이 활발하고 댓글이 많습니다.
---
influencer_id: 12
name: 마르 Marr
reason: 댓글 수가 많고 팔로워와의 소통이 활발하여 인기를 끌고 있습니다."""
}


    
]




# Define output path automatically using OS path join
output_path = os.path.join(os.path.expanduser("~"), "Documents", "qa_vector_db2.csv")

# Write to CSV with UTF-8 BOM
with open(output_path, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=["query", "answer"])
    writer.writeheader()
    for row in qa_data:
        writer.writerow(row)

print(f"CSV file saved to {output_path}")
