from PIL import Image
import os
 
def nameSort(x):
    # print(x)
    temp = 0
    if len(x.split(".")[0]) == 2:
        # print(x)
        temp = int(x[:2])
    else:
        temp = int(x[:1])
    # print(temp)
    return temp

def rea(path, pdf_name):
    
    file_list = os.listdir(path)
    
    pic_name = []
    im_list = []
    for x in file_list:
        if "jpg" in x or 'png' in x or 'jpeg' in x:
            pic_name.append(x)

    # pic_name.sort()
    # int(re.split('Mframes|_EPI|.png',x)[1]),int(re.split('Mframes|_EPI|.png',x)[2]))
    # file_list.sort(key=lambda x: int(x[4:])) 
    pic_name.sort(key=nameSort) 
    print(pic_name)
 
    # for x in pic_name:
    #     if "jpg" in x:
    #         new_pic.append(x)
 
    # for x in pic_name:
    #     if "png" in x:
    #         new_pic.append(x)
 
    # print("hec", new_pic)
 
    im1 = Image.open(os.path.join(path, pic_name[0])).rotate(90)  
    pic_name.pop(0)
    for i in pic_name:
        img = Image.open(os.path.join(path, i)).rotate(90)  
        # im_list.append(Image.open(i))
        if img.mode == "RGBA":
            img = img.convert('RGB')
            im_list.append(img)
        else:
            im_list.append(img)
    im1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)
    print("输出文件名称：", pdf_name)
 
 
if __name__ == '__main__':
 
    pdf_name = '静态部分'
    mypath=r"/media/wy/B2CD-0088/Download/静态部分"
    # if ".pdf" in pdf_name:
    #     rea(mypath, pdf_name=pdf_name)
    # else:
    rea(mypath, pdf_name="{}.pdf".format(pdf_name))