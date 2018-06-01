#-*-coding:utf-8-*-

from PIL import Image, ImageFilter
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
#获取图片大小
w,h = im.size
print('Original image size : width:%d height: %d' %(w,h))

#图片缩放
im.thumbnail((w//3, h//3))

print('Resize image to: %dx%d' % (w//3, h//3))
# 把缩放后的图像用jpeg格式保存:
im.save('test2.jpg', 'jpeg')


# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 应用模糊滤镜:

#变得模糊不清
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

#轮廓;外形;周线,围线
im2 = im.filter(ImageFilter.CONTOUR)
im2.save('contour.jpg','jpeg')

#细部； 细目，琐碎； 各种细节
im2 = im.filter(ImageFilter.DETAIL)
im2.save('detall.jpg','jpeg')

#在(表面)上浮雕图案
im2 = im.filter(ImageFilter.EMBOSS)
im2.save('emboss.jpg','jpeg')

#边界加强
im2 = im.filter(ImageFilter.EDGE_ENHANCE)
im2.save('edge_enhance.jpg','jpeg')

# 边界加强(阀值更大)
im2 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
im2.save('edge_enhance_more.jpg','jpeg')

# 边界滤镜
im2 = im.filter(ImageFilter.FIND_EDGES)
im2.save('find_edges.jpg','jpeg')

#平滑滤镜
im2 = im.filter(ImageFilter.SMOOTH)
im2.save('smooth.jpg','jpeg')

#平滑滤镜(阀值更大)
im2 = im.filter(ImageFilter.SMOOTH_MORE)
im2.save('smooth_more.jpg','jpeg')

#锐化滤镜
im2 = im.filter(ImageFilter.SHARPEN)
im2.save('sharpen.jpg','jpeg')
