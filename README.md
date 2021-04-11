# terraBot
# run the "pip install -r requirements.txt" to install packages required by the project

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades


################### OpenCv Example ######################

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

########################################################
