#!/usr/bin/env python
#-*-coding=utf-8-*-

'''To add a number at the corner of an image'''

from PIL import Image, ImageDraw, ImageFont

class ImageNumber(object):
    '''To add a number 
    __init__:
        initialize the class;
    add_number:
        add number
    '''

    def __init__(self, scale=(0.5, 0.5), path='./img.png'):
        '''Init'''
        self.path = path

    def add_number(self, num):
        img = Image.open(self.path)
        width, height = img.size
        draw = ImageDraw.Draw(img)
        font_size = min(width, height) // 5 
        font = ImageFont.truetype('./Novecentowide-Bold-webfont.woff', font_size);
        draw.text([width*0.2, height*0.3], num, fill=(77, 77, 77), font=font)
        font_size2 = font_size/4;
        font2 = ImageFont.truetype('Blokletters-Potlood-webfont.woff', font_size2) 
        draw.text([width*0.4, height*0.7], 'BY ZHANG QIONGYU', fill=(48, 48,48), font=font2)
        del draw
        img.show()
        img.save('page1.jpg', 'jpeg')

if __name__ == '__main__':
    img = ImageNumber(path='./page.jpg')
    img.add_number(r'WEB & BACKEND')
