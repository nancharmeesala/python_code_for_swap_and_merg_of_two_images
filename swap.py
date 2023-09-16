import cv2

# Load the two images
image1 = cv2.imread("C:\\Users\\nanch\\Downloads\\tiger2.jpeg")
image2 = cv2.imread("C:\\Users\\nanch\\Downloads\\flower.jpeg")

# Crop a part from each image (specify the cropping coordinates and dimensions)
crop1 = image1[100:100, 100:100]
crop2 = image2[100:100, 100:100]

# Ensure that the cropped regions have the same dimensions
if crop1.shape == crop2.shape:
    # Swap the cropped parts
    image1[100:100, 100:100] = crop2
    image2[100:100, 100:100] = crop1

    # Save the modified images
    cv2.imwrite('image1_modified.jpg', image1)
    cv2.imwrite('image2_modified.jpg', image2)

    # Display the modified images
    cv2.imshow('Modified Image 1', image1)
    cv2.imshow('Modified Image 2', image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Cropped regions have different dimensions. Make sure they match for swapping.')