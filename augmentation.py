import cv2
import numpy as np
import os
import shutil



images_folder = 'C:/Users/PC/Desktop/projedeneme/image'
label_folder = 'C:/Users/PC/Desktop/projedeneme/label'

def add_noise(image):
    row, col, ch = image.shape
    noise_lvl = 0.5
    noise = np.random.randn(row, col, ch) * 50
    img_noise = image + noise_lvl * noise
    img_noise = np.clip(img_noise, 0, 255)
    return img_noise

def add_sharpening(image):
    kernel_array = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])
    img_sharpened = cv2.filter2D(image, -1, kernel_array)
    return img_sharpened

def add_blur(image):
    ksize = (7, 7)
    img_blur = cv2.blur(image, ksize)
    return img_blur

image_files = os.listdir(images_folder)

for image_file in image_files:
    img_name, img_uzanti = os.path.splitext(image_file)
    img_path = os.path.join(images_folder, image_file)

    img = cv2.imread(img_path)

    noised_image = add_noise(img)
    sharpened_image = add_sharpening(img)
    blur_image = add_blur(img)
    noised_image_path = os.path.join(images_folder, f'{img_name}_noised{img_uzanti}')
    sharpened_image_path = os.path.join(images_folder, f'{img_name}_sharpened{img_uzanti}')
    blur_image_path = os.path.join(images_folder, f'{img_name}_blur{img_uzanti}')

    cv2.imwrite(noised_image_path, noised_image)
    cv2.imwrite(sharpened_image_path, sharpened_image)
    cv2.imwrite(blur_image_path, blur_image)

    #etiketleri kopyala ve cogalt
    label_file = f'{img_name}.txt'
    label_copy_path = os.path.join(label_folder, label_file)
    noised_img_label_path = os.path.join(label_folder, f'{img_name}_noised.txt')
    sharpened_img_label_path = os.path.join(label_folder, f'{img_name}_sharpened.txt')
    blur_img_label_path = os.path.join(label_folder, f'{img_name}_blur.txt')

    shutil.copy(label_copy_path, noised_img_label_path)
    shutil.copy(label_copy_path, sharpened_img_label_path)
    shutil.copy(label_copy_path, blur_img_label_path)
    pl.show(img)
