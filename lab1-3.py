# COMP4528: COMPUTER VISION, S1 2026
# Lab 1: Image Representation and Basic Processing

import cv2 as cv
import numpy as np


def load_image_and_convert_to_rgb(image_path: str) -> np.ndarray:
    """
    Load an image from the given file path and convert it to RGB format.

    Parameters:
        image_path (str): The path to the image file.

    Returns:
        numpy.ndarray: The RGB image as a 3D numpy array (H, W, 3).
    """
    

def resize_image(img: np.ndarray, width: int, height: int) -> np.ndarray:
    """
    Resize an image to the specified width and height.

    Parameters:
        img (numpy.ndarray): The input image as a 3D numpy array (H, W, 3).
        width (int): The desired width of the output image.
        height (int): The desired height of the output image.

    Returns:
        numpy.ndarray: The resized image as a 3D numpy array (height, width, 3).
    """
    cv.resize(img, (width, height))


def swap_red_and_blue_channels(img: np.ndarray) -> np.ndarray:
    """
    Swap the red and blue channels of an RGB image and return the new image.

    Parameters:
        img (numpy.ndarray): The input image as a 3D numpy array (H, W, 3).

    Returns:
        numpy.ndarray: The image with the red and blue channels swapped.
    """

    


def convert_to_grayscale(img: np.ndarray) -> np.ndarray:
    """
    Convert an RGB image to grayscale using the formula:
    gray = 0.299 * R + 0.587 * G + 0.114 * B

    Parameters:
        img (numpy.ndarray): The input image as a 3D numpy array (H, W, 3).

    Returns:
        numpy.ndarray: The grayscale image as a 2D numpy array (H, W).
    """

    


def single_channel_histogram_equalization(img: np.ndarray, channel: int) -> np.ndarray:
    """
    Given a RGB image "img", perform single channel (channel index "channel") histogram equalization to achieve image enhancement.

    Parameters:
        img (numpy.ndarray): The input image as a 3D numpy array (H, W, 3).
        channel (int): The index of the channel, e.g. 0, 1, 2

    Returns:
        numpy.ndarray: The new image of size (H, W, 3), where the "channel" index of it is the enhancement of "img" with single channel histogram equalization.
    """ 



def histogram_equalization(img: np.ndarray) -> np.ndarray:
    """
    Perform histogram equalization on each channel of a RGB image.

    Parameters:
        img (numpy.ndarray): The input RGB image as a 3D numpy array (H, W, 3).

    Returns:
        numpy.ndarray: The equalized RGB image as a 3D numpy array (H, W, 3).
    """
