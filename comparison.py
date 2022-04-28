def comparison1(x, y, ii, jj):
    comp = 0  # чем ближе эта переменная к 0, тем более схоже изображения
    image_x = x
    image_y = y
    pix_x = image_x.load()
    width_y = image_y.size[0]  # Определяем ширину.
    height_y = image_y.size[1]  # Определяем высоту.
    pix_y = image_y.load()
    i0 = ii
    j0 = jj
    while ii < width_y:
        while jj < height_y:
            comp += abs(pix_x[ii, jj][0] - pix_y[ii - i0, jj - j0][0])
            comp += abs(pix_x[ii, jj][1] - pix_y[ii - i0, jj - j0][1])
            comp += abs(pix_x[ii, jj][2] - pix_y[ii - i0, jj - j0][2])
            jj += 1
        ii += 1
    return comp


def comparison11(x, y, ii, jj, max_comp, size0, size1):
    comp = 0  # чем ближе эта переменная к 0, тем более схоже изображения
    image_x = x
    image_y = y
    pix_x = image_x.load()
    pix_y = image_y.load()
    i0 = ii
    j0 = jj
    while ii < i0 + size0:
        while jj < j0 + size1:
            comp += abs(pix_x[ii, jj][0] - pix_y[ii - i0, jj - j0][0])
            comp += abs(pix_x[ii, jj][1] - pix_y[ii - i0, jj - j0][1])
            comp += abs(pix_x[ii, jj][2] - pix_y[ii - i0, jj - j0][2])
            if comp > max_comp:
                return comp
            jj += 1
        ii += 1
    return comp
