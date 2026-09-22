import pymupdf
import os

pdf_file_path = r"C:\Users\Administer\Desktop\llm-programming-main\pdf\opensource_llm.pdf"

doc = pymupdf.open(pdf_file_path)

# 모든 페이지의 텍스트를 저장할 변수
full_text = ""

# PDF의 각 페이지에서 텍스트 추출
for page in doc:
    text = page.get_text()
    full_text += text

print(full_text)

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0] # 확장자 제거

os.makedirs("output", exist_ok=True)
txt_file_path = f"output/{pdf_file_name}.txt"

# 추출한 전체 텍스트를 UTF-8 형식의 파일로 저장
with open(txt_file_path, "w", encoding="utf-8") as f:
    f.write(full_text)