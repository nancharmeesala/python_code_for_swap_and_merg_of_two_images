import cv2

# Load an image from file
image = cv2.imread("C:\\Users\\nanch\\Downloads\\tiger2.jpeg")

# Check if the image was loaded successfully
if image is not None:
    # Display the image in a window
    cv2.imshow('Loaded Image', image)

    # Wait for a key press and close the window when a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Failed to load the image.')
