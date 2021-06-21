from os import path, walk
from PIL import Image, ImageOps

COLORS = 255
W_SIZE = 500
H_SIZE = 500


def resize_image(img_path):
    im = None
    try:
        # Load image
        im = Image.open(img_path)
        im = im.quantize(
            colors=256,
            method=1
        ).resize(
            (W_SIZE, H_SIZE)
        )
        im = ImageOps.grayscale(im)
        im.save(f"{img_path}_result.jpg")
    except Exception as err:
        print(err)
    return im


def get_rgb_image_matrix(im):
    mtx = [[] for x in range(H_SIZE)]
    for h_px in range(H_SIZE):
        for w_px in range(W_SIZE):
            la= im.getpixel((w_px, h_px))
            mtx[h_px].append((la))
    return mtx


def found_similars(im, img_folder):
    main_mtx = get_rgb_image_matrix(im)
    img_f = []
    img_f_result = []
    for (dirpath, dirnames, filenames) in walk(img_folder):
        img_f.extend(filenames)
        break
    for img in img_f:
        pil_img = resize_image(path.join(img_folder, img))
        img_mtx = get_rgb_image_matrix(pil_img)
        total_coincidence = 0
        for h_px in range(H_SIZE):
            for w_px in range(W_SIZE):
                lao = main_mtx[h_px][w_px]
                la = img_mtx[h_px][w_px]
                la_result = False
                # R
                if lao > la - 10 and lao < la + 10:
                    la_result = True
                if la_result:
                    total_coincidence += 1
        percent = (total_coincidence * 100) / (W_SIZE * H_SIZE)
        img_f_result.append(f"{img} => {percent}")
    print(img_f_result)


if __name__ == "__main__":
    image_name = "004.jpg"
    base_folder = path.realpath(path.dirname(__file__))
    img_folder = path.join(base_folder, 'imgs')
    img_path = path.join(img_folder, image_name)
    print(base_folder)
    print(img_folder)
    print(img_path)

    # Get image
    im = resize_image(img_path)
    found_similars(im, img_folder)
