# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random
# # 打开一个png图像文件
# im = Image.open('test.png')

# # 获得图像尺寸
# w, h = im.size
# print('原始图像大小: %s x %s' % (w, h))

# # 缩放到50%
# im.thumbnail((w / 2, h / 2))

# # 保存缩放后的图像
# im.save('thumbnail.jpg', 'jpeg')


# # 打开一个jpg图像文件
# im = Image.open('test.png')

# # 对图片进行模糊处理
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.png', 'png')


# 随机字母
def rmdChar():
    return chr(random.randint(65, 90))


# 随机颜色1
def rmdColor():
    return (random.randint(64, 255),
            random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def rmdColor2():
    return(random.randint(32, 127), random.randint(32, 127),
           random.randint(32, 127))


# 240 x 60
width = 60 * 4
height = 40
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建font对象
font = ImageFont.truetype('DejaVuSans-Bold.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rmdColor())

# 输出文字
for t in range(4):
    ch = rmdChar()
    print('char = %s', ch)
    draw.text((60 * t + 10, 0), ch, font=font, fill=rmdColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
