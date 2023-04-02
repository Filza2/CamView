import cv2,os
#By @Tweakpy - @vv1ck
urls=[
    'http://71.84.120.26/mjpg/video.mjpg?timestamp=0',
    'http://71.249.87.61/control/faststream.jpg?stream=full&fps=16',
    'http://50.158.165.198:1024/oneshotimage1?0'
]
url=urls[0];cam_switch=list();cap=cv2.VideoCapture(url)
def another_Cam(buff):
    url=urls[int(buff)]
    cap=cv2.VideoCapture(url)
    while len(cam_switch)!=3:
        ret,frame=cap.read() 
        if ret:cv2.imshow('Camera By @Tweakpy',frame)
        if cv2.waitKey(1)==ord("e"):break # To Exit the Program Click on e Button
    cap.release();cv2.destroyAllWindows();os.system('cls' if os.name=='nt' else 'clear');print(f'- Closing Now Page [ {buff} ] .\n')
    if len(cam_switch)!=3:cam_switch.append(2);another_Cam(2)
    else:os.system('cls' if os.name=='nt' else 'clear');print(f'- Done Closing All Pages  .\n')
def Cam():
    while True:
        ret,frame=cap.read() 
        if ret:cv2.imshow('Camera By @Tweakpy',frame)
        if cv2.waitKey(1)==ord("e"):break # To Exit the Program Click on e Button
    cap.release();cv2.destroyAllWindows();os.system('cls' if os.name=='nt' else 'clear');print(f'- Closing Now Page [ {0} ] .\n')
    cam_switch.append(1);another_Cam(1)
Cam()
        
        
