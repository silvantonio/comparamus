from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

#Get the 'Mean Squared Error'
def mse(imageA, imageB):

    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

# Compare images according to SSIM and MSE
def compare_images(imageA, imageB, title):

    # mean squared error
    m = mse(imageA, imageB)
    # structural similarity
    s = ssim(imageA, imageB)

    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")

    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")

    # show the images
    plt.show()


# load the images
original = cv2.imread("../data/chanel/sample1/original_resized.jpg")
fake = cv2.imread("../data/chanel/sample1/fake1.jpg")

# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
fake = cv2.cvtColor(fake, cv2.COLOR_BGR2GRAY)

# resize images
original = cv2.resize(original, (2000, 2000))
fake = cv2.resize(fake, (2000, 2000))

# initialize the figure
fig = plt.figure("Images")
images = ("Original", original), ("Fake", fake)

# loop over the images
for (i, (name, image)) in enumerate(images):
    # show the image
    ax = fig.add_subplot(1, 2, i + 1)
    ax.set_title(name)
    plt.imshow(image, cmap=plt.cm.gray)
    plt.axis("off")

# show the figure
plt.show()
# compare the images
compare_images(original, original, "Original vs. Original")
compare_images(original, fake, "Original vs. Fake")
