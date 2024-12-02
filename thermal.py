import numpy as np
from PIL import Image

# 텍스트 파일에서 숫자 데이터 불러오기
file_path = r'C:/파일/unlv/test.txt'  # 역슬래시 대신 슬래시 사용 또는 r'문자열'로 처리

# 텍스트 파일에서 숫자를 읽어 1차원 배열로 변환
with open(file_path, 'r') as file:
    data = file.read().replace(',', '').split()  # 쉼표 제거 후 공백으로 분리

# 숫자 문자열을 정수로 변환
data = list(map(int, data))

# 320 x 256 배열로 변환 (사이즈가 정확히 맞아야 함)
data = np.array(data).reshape((256, 320)).astype(np.uint8)

# 배열을 이미지로 변환
image = Image.fromarray(data)

# 이미지 저장 (PNG 형식으로 저장)
image.save('generated_image.png')

# 이미지 보기
image.show()
