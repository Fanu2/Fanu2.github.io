import cv2
import numpy as np

def main():
    # Load the two images (1.jpg and 2.jpg)
    img1 = cv2.imread('/home/jasvir/Music/jodha6/1.jpg')
    img2 = cv2.imread('/home/jasvir/Music/jodha6/2.jpg')

    # Check if the images were loaded correctly
    if img1 is None or img2 is None:
        print("Could not open or find the images.")
        return

    # Resize img2 to match the dimensions of img1
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Create a VideoWriter object to save the video
    video = cv2.VideoWriter('/home/jasvir/Music/jodha6/output.avi',
                            cv2.VideoWriter_fourcc(*'MJPG'),
                            10, (img1.shape[1], img1.shape[0]))

    # Check if video was opened correctly
    if not video.isOpened():
        print("Could not open the video for writing.")
        return

    # Perform morphing by interpolating between the two images
    alpha = 0.0  # Alpha for blending

    # Create a window to display the morphing process
    cv2.namedWindow("Morph", cv2.WINDOW_AUTOSIZE)

    # Loop through different blending levels (alpha from 0 to 1)
    while alpha <= 1.0:
        # Morphing: linear interpolation between img1 and img2
        morph_image = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0.0)

        # Display the morphing image
        cv2.imshow("Morph", morph_image)

        # Write the frame to the video
        video.write(morph_image)

        # Wait for a short duration
        if cv2.waitKey(30) & 0xFF == 27:  # Break loop on 'ESC' key
            break

        alpha += 0.01  # Increment alpha

    # Release the video writer
    video.release()

    # Close the display window
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
