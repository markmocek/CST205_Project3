import cv2

# Camera port 0 is the laptop webcam
camera_port = 0

# Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

# Index to a camera port.
camera = cv2.VideoCapture(camera_port)

# Captures image from the camera and returns it in PIL format
def get_image():
    # read to get a full image out of a VideoCapture object
    retval, im = camera.read()
    return im

# Ramp the camera - these frames will be discarded
for i in xrange(ramp_frames):
    temp = get_image()

print("Taking image...")

# Take the actual image we want to keep
camera_capture = get_image()\

file = "test_image.jpg"

# correct format based on the file extension you provide
cv2.imwrite(file, camera_capture)

# Release the camera
del(camera)
