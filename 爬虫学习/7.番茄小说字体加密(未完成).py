# import requests
#
#
# url = "https://fanqienovel.com/api/author/library/book_list/v0/?page_count=18&page_index=0&gender=-1&category_id=-1&creation_status=-1&word_count=-1&book_type=-1&sort=0&msToken=uYjpjQVfg9Yrdbty-Aa1DhrMd8bQow23UIksilrPEpoLnb_Z753EbVxvUYoqx4D_0LM3QzM3FnPmjJrTC3Hil9WGwo4ab1w0Bbd0IsUXIGUgx2zRldxQ&a_bogus=D7UOvcg8Msm18jfPYwkz9bwm%2FLm0YWRogZEz1Tz1XzLL"
#
# res = requests.get(url=url)
#
# datas = res.json()["data"]["book_list"]
# for data in datas:
#     print(data["book_name"])


# from paddleocr import PaddleOCR, draw_ocr
# # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
# ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
# img_path = '../RESULT/Encrypted_Font/58347.png'
# result = ocr.ocr(img_path, cls=True)
# for idx in range(len(result)):
#     res = result[idx]
#     for line in res:
#         print(line, "*********************")



from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
img_path = '../RESULT/Encrypted_Font/58347.png'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# 显示结果
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
