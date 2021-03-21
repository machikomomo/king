# requirements.txt 用添加依赖，优点类似于pom.xml
import os

import cv2

# 待处理的角色列表
heros = ['diaochan','shangguan','zhouyu']

if __name__ == '__main__':
    for hero in heros:
        # 待处理图片的路径
        path = '/Users/momochan/pythonProject/honor-of-king/images/' + hero + '/'
        path2 = path.replace(hero, hero + '_2')
        if not os.path.exists(path2):
            os.mkdir(path2)
        for key in range(100, 200):
            file = '0' + str(key) + '.jpg'
            if os.path.isfile(path + file):
                # path是目录名，file是文件名，如果path+file存在
                img = cv2.imread(path + file, 0)
                # cv2在读取图片时就可以将它转为黑白了
                if img.size !=921600:
                    img = cv2.resize(img,(1280,720))
                #如果图片大小不符合预期，就按照上面这句调整大小
                crop_img = img[447:550, 970:1085]
                #裁剪，分别是主对角线上的两个坐标,裁剪完就变成/赋值给crop_img
                cv2.imwrite(path2 +file,crop_img)