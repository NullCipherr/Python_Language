import os
import cv2
import numpy as np





# Constants for adjustable values
INPUT_FOLDER = "InputImages"  # Input directory
OUTPUT_FOLDER = "OutputImages"  # Output directory
INPUT_IMAGE = "img001.jpg"  # Input image name
HUE = 10  # Hue value
HUE_RANGE = 125  # Hue range width





"""
    Adjusts the hue range in an image in the HSV color space.

    Args:
        img_path (str): Path to the input image.
        h (int): Central hue value to be adjusted.
        x (int): Width of the hue range to be adjusted.

    Returns:
        numpy.ndarray: Resulting image with adjusted hues.
"""
def adjust_hue_range(img_path, h, x) :
    try :
        # Load the image in BGR format
        img = cv2.imread(img_path)

        # Check if the image was loaded successfully
        if img is None:
            raise FileNotFoundError("Error: Failed to load the image.")

        # Convert the image to HSV.
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Convert h to the range [0, 180]
        h = h % 180

        # Set the lower and upper bounds of the hue range
        lower = np.array([max(0, h - x), 0, 0])
        upper = np.array([min(180, h + x), 255, 255])

        # Create a mask for hues in the range [h-x, h+x]
        mask = cv2.inRange(img_hsv, lower, upper)

        # Replace hues in the range [h-x, h+x] with their inverses
        img_hsv[mask > 0, 0] = (img_hsv[mask > 0, 0] + 180) % 180

        # Convert the image back to the BGR color space
        img_result = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

        return img_result
    except Exception as e :
        print(e)
        return None





"""
    Generates the output file name based on the input file name.

    Args:
        input_filename (str): Input file name.

    Returns:
        str: Output file name.
"""
def generate_output_filename(input_filename) :
    
    # Get the file name without extension
    file_name_without_extension = os.path.splitext(input_filename)[0]
    
    return f"{file_name_without_extension}_output.jpg"





def main():
    try:
        # Input and output directories
        current_directory = os.getcwd()
        input_path = os.path.join(current_directory, INPUT_FOLDER, INPUT_IMAGE)
        output_path = os.path.join(current_directory, OUTPUT_FOLDER, generate_output_filename(INPUT_IMAGE))

        # Hue and hue range values
        h = HUE
        x = HUE_RANGE

        output_image = adjust_hue_range(input_path, h, x)

        # Check if the output image was generated successfully
        if output_image is not None:
            # Check and create output directories if necessary
            os.makedirs(os.path.join(current_directory, OUTPUT_FOLDER), exist_ok=True)

            # Save the output image based on the input image name
            cv2.imwrite(output_path, output_image)

            # Set the size of the output window
            cv2.namedWindow("Output Image", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Output Image", 800, 800)

            # Display the output image
            cv2.imshow("Output Image", output_image)

            # Wait for a key press
            cv2.waitKey(0)

            # Close the window
            cv2.destroyAllWindows()
        else:
            print("Failed to generate the output image.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
