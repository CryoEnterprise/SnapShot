# Needed Imports:
import datetime
import os
import cv2
import numpy as np


def SnapShot():
    # Assign opencv to default camera:
    camera_snapshot = cv2.VideoCapture(0)

    # Instructions on how to operate program:
    print("\nPlease Press s to take snapshot\n")

    print("Please Press q to quit\n")

    while True:
        # While loop needs definition inside the loop to update:
        image_out_put_path = "Output/Images/"

        # Check and create the video output path:
        if os.path.isdir(image_out_put_path) is False:
            os.makedirs(image_out_put_path)

        # Set up file name:
        image_time_stamp = datetime.datetime.now()
        image_fileName = "{}.png".format(image_time_stamp.strftime("%Y-%m-%d_%H-%M-%S"))
        image_output_path = os.path.sep.join((image_out_put_path, image_fileName))

        # Define Waitkey:
        snapshot_key = cv2.waitKey(1)

        # Grab Frames from the Camera:
        camera_status, camera_frames = camera_snapshot.read()

        # View Current Frames
        cv2.imshow("OpenCV SnapShot Training", camera_frames)

        # Grab Save and Write Frame to OutPut Path:
        if snapshot_key == ord('s'):
            print("Taking SnapShot\n")
            # Write Captured frames to the output variable:
            cv2.imwrite(filename=image_output_path, img=camera_frames)
            print("SnapShot saved!\n")
            pass

        # Listen for ShutDown Key then Perform Cleanup:
        elif snapshot_key == ord('q'):
            print("Closing Camera\n")
            camera_snapshot.release()
            cv2.destroyAllWindows()
            break
    pass


# Create Main Entry Point:
if __name__ == '__main__':
    SnapShot()
