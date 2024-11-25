import json
import os

def split_json_by_influencer_id(input_file, output_dir):
    # JSON 파일 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 출력 폴더가 존재하지 않으면 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 각 인플루언서 정보를 개별 JSON 파일로 저장
    for influencer in data:
        influencer_id = influencer.get("influencer_id")
        if influencer_id is not None:
            output_file = os.path.join(output_dir, f"influencer_{influencer_id}.json")
            with open(output_file, 'w', encoding='utf-8') as f_out:
                json.dump(influencer, f_out, ensure_ascii=False, indent=4)
            print(f"Saved {output_file}")
        else:
            print("No influencer_id found for an entry, skipping.")

# 사용 예시
input_file = 'D:/대학 관련/4-2/종합설계2/v2.json'  # 분할할 원본 JSON 파일 경로
output_dir = 'D:/대학 관련/4-2/종합설계2/influencer_csv'  # 분할된 JSON 파일을 저장할 폴더 경로
split_json_by_influencer_id(input_file, output_dir)
