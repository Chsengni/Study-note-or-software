<p align="center" style="font-size:25px;color:blue;">matlab初级教程</p>

----------

2018/10/30 9:25:03 
### 1.图像的读入和显示：

（1）图像读入：
	A=imread('文件名',文件格式) 

	[X,map]=imread('文件名') 

 X代表索引图像矩阵，map为颜色映射表 

（2）图像显示：
	image(A); 
	imshow(A);

### 2. 图像写回 
	A=imwrite('文件名',文件格式) 
	[X,map]=imwrite('文件名')
	
  注意，当只写文件名时，它应带有扩展名 

### 3.获取图像信息 
	info=imfinfo('文件名')

### 4.标准图像显示技术 
	imshow(I,n)
 显示灰度图像，n为灰度级数 

	imshow(I,[low,high])
 [low,high]为图像数据的值域（可为空[ ]）
 
	imshow(BW)
 显示二值图像 

	imshow(X,map)
 显示索引色图像
### 5.图像的运算

（1）Z=imadd(X,Y)

	图像的加运算，X,Y是输入的两幅图像，其中一个可以是常数
（2）Z=imsubtract(X,Y)

	图像的减运算，Y可以是常数
（3）Z=immiltiply(X,y)
	
	图像的乘运算，Y也可以是常数

（4）Z=imdivide(X,y)

	图像的除运算，Y也可以是常数

6.图像的类型转换

（1）RGB=ind2rgb(X,map)

	索引图转换为真彩色图
（2）I=mat2gray(A)

	将一个数据矩阵转换为灰度图
（3）I=rgb2gray(RGB)

	将一副灰度图转换为真彩色图
（4）[X,map]=rgb2ind(RGB,n)

	将RGB图转换为索引色图
（5）BW=im2bw(I,level)

	将真彩色图或灰度图转换为二值图，level为阈值
  BW=im2bw(X,map,level)

	将索引色图转换为二值图

（6）I=ind2gray(X,map)

	将索引色图转换为灰度图

### 7.傅里叶变换

（1）Y=fft2(x,m,n)

	二维离散傅里叶快速变换，x为要进行傅里叶变换的矩阵，m、n是返回的变换矩阵Y的行数和列数。 
（2）Y=ifft2(x,m,n)

	二维离散傅里叶反变换 
（3）Y1=fftshift(Y)

	把傅里叶变换操作得到的结果中零频率成分移到矩阵中心，这样利于观察频谱。
### 8.离散余弦变换

（1）D=dct2(A,m,n)

	二维离散余弦变换，A是输入图像，B是返回的DCT变换系数，m、n为D的行数和列数 
（2）D=idct(A,m,n)

	e二维离散余弦逆变换。 
（3）D=dctmtx(n)

	返回DCT变换矩阵

### 9.Radon变换

[R,xp]=radon(I,theta)

	I为图像矩阵，theta为角度

I=iradon(R,thrta)

	逆Radon变换

### 10.图像的增强（1）

（1）imhist(I)

	显示一副图像的直方图
（2）J=histeq(I)

	直方图均衡化
（3）J=imadjust(I,[low_in;high_in],[low_out;high_out],gamma)

	调整图像灰度值
（4）J=adapthisteq(I)

	有限对比自适应直方图均衡化

（5）S=decorrestretch(I)

	去相关色度拉伸

### 11.图像的增强（2）
    B=imfilter(A,H,option1,option2,...)

A是输入图像，H是卷积核或相关核，option是一些可选参数。
注：权重矩阵称为卷积核，也称为滤波器。卷积核是相关核旋转180度得到的,可选参数参看help

其中H也用H=fspecial(type,parameters)可自定义

### 12.中值滤波器
	B=medfilt2(A,[m,n])

A是输入的图像，[m,n]是邻域的大小

### 13.自适应滤波器

	B=wiener2(A,[m,n])

14.图像的分析 
	P=impixel(I)

交互式获取图像像素值 

	P=impixel(I,c,r)

指定点坐标像素值，c、r为行坐标和列坐标 
C=improfile(I,xi,yi,n,method)%创建图像强度曲线，n规定了计算图像强度点的个数，xi、yi规定了空间直线端点坐标，method是插值方法（nearest,bilinrar,bicubic） 

	imcontour(I,n,linespec)

显示图像数据的等值线图

### 15.图像的统计信息
	B=mean(A)
计算A的均值

	b=std2（A）
计算A的标准差

	r=corr2(A,B)
A,B为输入二维矩阵，r是返回的协方差系数
