import numpy as np
import cv2
import matplotlib.pyplot as plt

# img1 = cv2.imread('../data/chanel/sample1/original.jpg', 0)
# img2 = cv2.imread('../data/chanel/sample1/fake1.jpg', 0)
#img2 = cv2.imread('../data/chanel/sample1/fake2.jpg', 0)
#img2 = cv2.imread('../data/chanel/sample1/keypoints/logo.jpg', 0)
#img2 = cv2.imread('../data/cr7/photo1.jpg', 0)

###############################################################################

# # Initiate ORB detector
# orb = cv2.ORB_create()
#
# # find the keypoints and descriptors with ORB
# kp1, des1 = orb.detectAndCompute(img1, None)
# kp2, des2 = orb.detectAndCompute(img2, None)
#
# # create BFMatcher object
# bf = cv2.BFMatcher(cv2.NORM_HAMMING2, crossCheck=True)
#
# # Match descriptors.
# matches = bf.match(des1, des2)
#
# # Sort them in the order of their distance.
# matches = sorted(matches, key=lambda x:x.distance)
#
# print(len(matches))
#
# # Draw first 10 matches.
# img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:300], outImg=2)
# plt.imshow(img3), plt.show()

###############################################################################

# # Initiate SIFT detector
# sift = cv2.xfeatures2d.SIFT_create()
# # find the keypoints and descriptors with SIFT
# kp1, des1 = sift.detectAndCompute(img1, None)
# kp2, des2 = sift.detectAndCompute(img2, None)
# # BFMatcher with default params
# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1, des2, k=2)
# print(len(matches))
# # Apply ratio test
# good = []
# for m, n in matches:
#     if m.distance < 0.75*n.distance:
#         good.append([m])
#
# print(len(good))
# # cv2.drawMatchesKnn expects list of lists as matches.
# img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, outImg=2)
# plt.imshow(img3), plt.show()

###############################################################################

# # Initiate SIFT detector
# sift = cv2.xfeatures2d.SIFT_create()
# # find the keypoints and descriptors with SIFT
# kp1, des1 = sift.detectAndCompute(img1, None)
# kp2, des2 = sift.detectAndCompute(img2, None)
# # FLANN parameters
# FLANN_INDEX_KDTREE = 1
# index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=50)
# search_params = dict(checks=50)   # or pass empty dictionary
# flann = cv2.FlannBasedMatcher(index_params, search_params)
# matches = flann.knnMatch(des1, des2, k=2)
# print(len(matches))
# # Need to draw only good matches, so create a mask
# matchesMask = [[0, 0] for i in range(len(matches))]
# # ratio test as per Lowe's paper
# for i, (m, n) in enumerate(matches):
#     if m.distance < 0.7*n.distance:
#         matchesMask[i] = [1, 0]
# draw_params = dict(matchColor=(0, 255, 0),
#                    singlePointColor=(255, 0, 0),
#                    matchesMask=matchesMask,
#                    flags=0)
# print(len(matchesMask))
# print(len(draw_params))
# img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
# plt.imshow(img3,), plt.show()

###############################################################################

img1 = cv2.imread('../data/test/box_in_scene.png', 0)
#img2 = cv2.imread('../data/chanel/sample1/fake1.jpg', 0)
img2 = cv2.imread('../data/test/box.png', 0)
#img2 = cv2.imread('../data/cr7/photo1.jpg', 0)

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1, des2, k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0, 0] for i in range(len(matches))]

matchesCount = 0
# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.70*n.distance:
        matchesMask[i] = [1, 0]
        matchesCount = matchesCount+1

draw_params = dict(matchColor=(0, 255, 0),
                   singlePointColor=(255, 0, 0),
                   matchesMask=matchesMask,
                   flags=0)

print(len(matchesMask))
print(matchesCount)

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

plt.imshow(img3), plt.show()
