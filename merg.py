import cv2

# Load the two images
image1 = cv2.imread("C:\\Users\\nanch\\Downloads\\tiger2.jpeg")
image2 = cv2.imread("C:\\Users\\nanch\\Downloads\\flower.jpeg")

# Get the dimensions of the first image
height, width, _ = image1.shape

# Combine the two images horizontally
combined_image = cv2.hconcat([image1, image2])

# Save the combined image
cv2.imwrite('combined_image.jpg', combined_image)

# Display the combined image
cv2.imshow('Combined Image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()