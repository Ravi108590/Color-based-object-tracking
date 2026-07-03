# 🎯 Object Tracking Based on Color using OpenCV

## 📌 Overview

This project demonstrates **real-time object tracking based on color** using **OpenCV** and **Python**. The application captures live video from the webcam, detects an object within a specified HSV color range, tracks its position, and prints movement commands based on the object's location and size.

This project is useful for learning the fundamentals of **computer vision**, **color segmentation**, **object detection**, and **basic robot navigation logic**.

---

## 🚀 Features

* Real-time webcam video capture.
* Color-based object detection using the HSV color space.
* Noise removal using image morphology.
* Contour detection to identify the target object.
* Center point calculation using image moments.
* Circular boundary visualization around the detected object.
* Direction prediction:

  * Left
  * Right
  * Front
  * Stop

---

## 🛠️ Technologies Used

* Python
* OpenCV
* Imutils
* NumPy

---

## 📂 Project Workflow

### Step 1: Capture Video

The webcam continuously captures video frames using OpenCV.

```python
camera = cv2.VideoCapture(0)
```

---

### Step 2: Resize the Frame

Each frame is resized to improve processing speed and maintain consistent dimensions.

---

### Step 3: Apply Gaussian Blur

Gaussian Blur removes small image noise before color detection.

```python
blurred = cv2.GaussianBlur(frame, (11,11), 0)
```

---

### Step 4: Convert BGR to HSV

The captured frame is converted from the BGR color space to the HSV color space.

HSV is preferred because it separates color information (Hue) from brightness, making color detection more robust under different lighting conditions.

```python
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

---

### Step 5: Create a Color Mask

A binary mask is created using predefined HSV lower and upper color boundaries.

```python
mask = cv2.inRange(hsv, redLower, redUpper)
```

Pixels inside the selected color range become white, while all other pixels become black.

---

### Step 6: Remove Noise

Morphological operations improve the quality of the binary mask.

* **Erosion** removes small unwanted white pixels.
* **Dilation** restores the size of the detected object after erosion.

```python
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
```

---

### Step 7: Detect Contours

Contours represent the boundaries of detected objects.

The largest contour is selected because it is assumed to be the target object.

```python
c = max(cnts, key=cv2.contourArea)
```

---

### Step 8: Find the Object Center

The object's center is calculated using image moments.

Image moments provide the centroid (center point) of the detected contour.

```python
M = cv2.moments(c)
```

---

### Step 9: Draw Detection

A circle is drawn around the detected object for visualization.

The center point is also displayed to indicate the tracked position.

---

### Step 10: Determine Movement Direction

The object's horizontal position and size determine the movement command.

#### Left

If the object's center is near the left side of the frame.

```text
center_x < 150
```

#### Right

If the object's center is near the right side of the frame.

```text
center_x > 450
```

#### Front

If the object is centered but still far away (small radius).

```text
radius < 250
```

#### Stop

If the object is very close (large radius).

```text
radius > 250
```

---

## 🧠 Detection Logic

```
Capture Webcam Frame
        │
        ▼
Resize Frame
        │
        ▼
Apply Gaussian Blur
        │
        ▼
Convert BGR → HSV
        │
        ▼
Create Color Mask
        │
        ▼
Remove Noise
        │
        ▼
Find Contours
        │
        ▼
Select Largest Contour
        │
        ▼
Calculate Center & Radius
        │
        ▼
Draw Circle
        │
        ▼
Predict Direction
(Left / Right / Front / Stop)
```

---

## 📊 Output

The application displays:

* Live webcam feed.
* Circular boundary around the detected object.
* Center point of the detected object.
* Direction commands printed in the terminal:

  * Left
  * Right
  * Front
  * Stop

---

## 💡 Applications

* Robot navigation
* Autonomous vehicle prototypes
* Human-computer interaction
* Gesture-controlled systems
* Object-following robots
* Color-based automation systems

---

## 📚 Learning Outcomes

Through this project, you will understand:

* HSV color space
* Color segmentation
* Image preprocessing
* Gaussian Blur
* Morphological operations (Erosion & Dilation)
* Contour detection
* Image moments
* Minimum enclosing circle
* Real-time object tracking using OpenCV

---

## ▶️ How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install opencv-python imutils numpy
```

3. Run the program:

```bash
python object_tracking.py
```

4. Place an object whose color falls within the specified HSV range in front of the webcam.

5. Press **Q** to exit the application.

---

## 📌 Future Enhancements

* Support multiple object tracking.
* Automatic HSV color selection using trackbars.
* Draw the movement trajectory of the object.
* Display FPS (Frames Per Second).
* Integrate with a robot for autonomous movement.
* Detect multiple colors simultaneously.
