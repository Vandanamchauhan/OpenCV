# import cv2
#
# img = cv2.imread("D:\photos\DSC_1804(1).JPG")
#
# image = cv2.imshow('bapu' , img)
#
# cv2.waitKey(0)

not use
# import cv2
#
# cap = cv2.VideoCapture("D:\videoes\VID-20210830-WA0001.mp4")
#
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Video', img )
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# rough work
# # Check if camera opened successfully
# if (cap.isOpened() == False):
#     print("Error opening video  file")
#
# # Read until video is completed
# while (cap.isOpened()):
#
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     if ret == True:
#
#         # Display the resulting frame
#         cv2.imshow('Frame', frame)
#
#         # Press Q on keyboard to  exit
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#
#     # Break the loop
#     else:
#         break
#
# cap.release()
#
#
# # Closes all the frames
# cv2.destroyAllWindows()

