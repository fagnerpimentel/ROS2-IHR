# Fonte: https://ai.google.dev/edge/mediapipe/solutions/vision/face_landmarker?hl=pt-br

# pip install mediapipe
# wget -O tasks/face_landmarker.task -q https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task
# wget -q -O input_images/input_face.png https://storage.googleapis.com/mediapipe-assets/business-person.png

# STEP 1: Import the necessary modules.
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from utils.utils_face import draw_landmarks_on_image

# STEP 2: Create an FaceLandmarker object.
base_options = python.BaseOptions(model_asset_path='tasks/face_landmarker.task')
options = vision.FaceLandmarkerOptions(base_options=base_options,
                                       output_face_blendshapes=True,
                                       output_facial_transformation_matrixes=True,
                                       num_faces=1)
detector = vision.FaceLandmarker.create_from_options(options)

# STEP 3: Load the input image.
image = mp.Image.create_from_file("input_images/input_face.png")

# STEP 4: Detect face landmarks from the input image.
detection_result = detector.detect(image)

# STEP 5: Process the detection result. In this case, visualize it.
annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
cv2.imwrite("output_images/output_face.jpg", cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)) 