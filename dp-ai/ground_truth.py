import csv

def directed_to_ground_truth(directed_file, ground_truth_file, weight_threshold=0.05):
    with open(directed_file, 'r') as infile, open(ground_truth_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=' ')
        writer = csv.writer(outfile)
        writer.writerow(['data'])
        
        for row in reader:
            weight = float(row[2])
            if weight >= weight_threshold:
                writer.writerow([' '.join(row)])

# 파일 경로 설정
directed_file = 'directed.csv'
ground_truth_file = 'ground_truth.csv'

# 변환 함수 호출
directed_to_ground_truth(directed_file, ground_truth_file)
print(f"Data has been successfully converted from {directed_file} to {ground_truth_file}")
