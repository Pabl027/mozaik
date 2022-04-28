from comparison import comparison1, comparison11
from PIL import Image, ImageDraw
import random
import os


fl = True
protect = []

save_i = 0
save_j = 0


image = Image.open("1.jpg")
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.

first_size = True
path = "image"
filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        name = os.path.splitext(file)[1]
        if name == ".jpg":
            test = Image.open(os.path.join(root, file))
            if first_size:
                size0 = test.size[0]
                size1 = test.size[1]
                first_size = False
            if test.size[0] != size0 or test.size[1] != size1:
                print(os.path.join(root, file))
            else:
                filelist.append(os.path.join(root, file))
width0 = size0  # Определяем ширину.
height0 = size1

for uu in range(round(width/size0)):
    protect.append([])

for uu2 in range(round(width/size0)):
    for uu1 in range(round(height/size1)):
        protect[uu2].append(0)

while fl:
    if len(filelist) < 2:
        for root, dirs, files in os.walk(path):
            for file in files:
                name = os.path.splitext(file)[1]
                if name == ".jpg":
                    test = Image.open(os.path.join(root, file))
                    if first_size:
                        size0 = test.size[0]
                        size1 = test.size[1]
                        first_size = False
                    if test.size[0] != size0 or test.size[1] != size1:
                        print(os.path.join(root, file))
                    else:
                        filelist.append(os.path.join(root, file))
    lst_pict = 0
    for lst11 in protect:
        for lst110 in lst11:
            if lst110 == 0:
                lst_pict += 1
                if lst_pict > 1:
                    break
        if lst_pict == 1:
            fl = False
    rnd_index = random.randint(0, len(filelist)-1)
    first_comp = True
    mirror_comp = []
    image = Image.open("1.jpg")
    image0 = Image.open(filelist[rnd_index])
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
    pix = image0.load()
    i = 0
    while i <= width - width0:
        j = 0
        while j <= height - height0:
            if protect[int(i/size0)][int(j/size1)] != 1:
                if first_comp:
                    max_comp = comparison1(image, image0, i, j)
                    now_comp = max_comp + 1
                    first_comp = False
                else:
                    now_comp = comparison11(image, image0, i, j, max_comp, size0, size1)
                if now_comp < max_comp:
                    save_i = i
                    save_j = j
                    max_comp = now_comp
                    mirror_comp = []
                elif now_comp == max_comp:
                    if len(mirror_comp) == 0:
                        mirror_comp.append([save_i, save_j])
                    mirror_comp.append([i, j])
            j += size1
        i += size0
    if len(mirror_comp) != 0:
        k = random.choice(mirror_comp)
        save_i = k[0]
        save_j = k[1]
    protect[int(save_i/size0)][int(save_j/size1)] = 1
    for ii in range(width0):
        for jj in range(height0):
            a = pix[ii, jj][0]
            b = pix[ii, jj][1]
            c = pix[ii, jj][2]
            draw.point((ii + save_i, jj + save_j), (a, b, c))

    image.save("1.jpg", "JPEG")

    del filelist[rnd_index]

lst_pict = random.randint(0, len(filelist))
image0 = Image.open(filelist[rnd_index])
pix = image0.load()
for ii in range(width0):
    for jj in range(height0):
        a = pix[ii, jj][0]
        b = pix[ii, jj][1]
        c = pix[ii, jj][2]
        draw.point((ii, jj), (a, b, c))
image.save("1.jpg", "JPEG")
