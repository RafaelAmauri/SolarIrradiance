import numpy as np 
import cv2

###########################
# Variables
K = 2
ATTEMPTS = 10
CRITERIA = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

#################################

# convert to LAB colorspace
def rgb_convert_lab(img):
    height, width, channel = img.shape
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    return img_lab


# convert image from LAB to RGB
def lab_convert_rgb(processed_img):
    res2 = cv2.cvtColor(processed_img, cv2.COLOR_LAB2BGR)

    return res2


# flatten the image and convert it to float32 so it can be used in k-means
def kmeans_flatten_img(img, is_lab):
    img2 = img.reshape((-1, 3))
    img2 = np.float32(img2)

    return img2


# run kmeans
def kmeans(flattened_img, original_img_shape, n_clusters):
    ret, label, center= cv2.kmeans(flattened_img, n_clusters, None, CRITERIA, ATTEMPTS, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res  = center[label.flatten()]
    res2 = res.reshape((original_img_shape))

    return res2


def save_img(name, img):
    cv2.imwrite(name, img)


def main():

    # Read IMG
    img = cv2.imread('database/inpe.png')

    # KMEANS IN RGB
    flattened_img = kmeans_flatten_img(img, False)
    processed_img = kmeans(flattened_img, img.shape, K)
    print("Printing img in RGB colorspace")
    save_img("kmeans_rgb.png", processed_img)

    # KMEANS IN LAB
    lab_img = rgb_convert_lab(img)
    flattened_img = kmeans_flatten_img(lab_img, True)
    processed_img = kmeans(flattened_img, img.shape, K)
    rgb_img = lab_convert_rgb(processed_img)
    
    print("Printing img in LAB colorspace")
    save_img("kmeans_lab.png", rgb_img)

if __name__ == '__main__':
    main()
