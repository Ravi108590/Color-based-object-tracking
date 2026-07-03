import imutils 
import cv2 

#between this range of color if object occurs then will process
#hsv values
redLower = (87, 136, 145)
redUpper = (1770, 2550, 2550)

camera = cv2.VideoCapture(0)

while True:
    (grabbed, frame) = camera.read() #frame read
    frame = imutils.resize(frame, width=600) #resize
    blurred = cv2.GaussianBlur(frame, (11, 11), 0) #(11,11) adding kernal to smooth
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) #camera gives BGR so convert in HSV

    mask = cv2.inRange(hsv, redLower, redUpper) 
    #removes the dotts from the images
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) [-2]

    center = None
    if len(cnts) > 0:
        #process the max contours (large area)
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c) #small circle

        #for counting the radious finding the moments it captures the image
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) #finding center of detected area
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            if radius > 250:
                print("stop")

            else:
                if (center[0]<150):
                    print("Left")

                elif (center[0]>450):
                    print("Right")
                elif(radius<250):
                    print("Front")
                else:
                    print("Stop")

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camera.release()
cv2.destroyeAllWindows()
