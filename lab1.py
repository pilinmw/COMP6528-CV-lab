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
    img_bgr = cv.imread(image_path) #用 cv.imread 读取图片
    img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB) #从 BGR 转换到 RGB
    return img_rgb #返回转换后的图片


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
    return cv.resize(img,(width, height))


def swap_red_and_blue_channels(img: np.ndarray) -> np.ndarray:
    """
    Swap the red and blue channels of an RGB image and return the new image.

    Parameters:
        img (numpy.ndarray): The input image as a 3D numpy array (H, W, 3).

    Returns:
        numpy.ndarray: The image with the red and blue channels swapped.
    """
    return cv.cvtColor(img, cv.COLOR_RGB2BGR)
    


def convert_to_grayscale(img: np.ndarray) -> np.ndarray:
    """
    Convert an RGB image to grayscale using the formula:
    gray = 0.299 * R + 0.587 * G + 0.114 * B

    Parameters:
        img (numpy.ndarray): The input image as a 3D numpy array (H, W, 3).

    Returns:
        numpy.ndarray: The grayscale image as a 2D numpy array (H, W).
    """
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]    
    gray = 0.299 * R + 0.587 * G + 0.114 * B
    return gray

def single_channel_histogram_equalization(img: np.ndarray, channel: int) -> np.ndarray:
    """
    Given a RGB image "img", perform single channel (channel index "channel") histogram equalization to achieve image enhancement.

    Parameters:
        img (numpy.ndarray): The input image as a 3D numpy array (H, W, 3).
        channel (int): The index of the channel, e.g. 0, 1, 2

    Returns:
        numpy.ndarray: The new image of size (H, W, 3), where the "channel" index of it is the enhancement of "img" with single channel histogram equalization.
    """ 
    cv_eq = img.copy()#复制原图
    cv_eq[:, :, channel] = cv.equalizeHist(img[:, :, channel])
    return cv_eq


def histogram_equalization(img: np.ndarray) -> np.ndarray:
    """
    Perform histogram equalization on each channel of a RGB image.

    Parameters:
        img (numpy.ndarray): The input RGB image as a 3D numpy array (H, W, 3).

    Returns:
        numpy.ndarray: The equalized RGB image as a 3D numpy array (H, W, 3).
    """
    img_eq = np.copy(img)
    img_eq[:, :, 0] = cv.equalizeHist(img_eq[:, :, 0])
    img_eq[:, :, 1] = cv.equalizeHist(img_eq[:, :, 1])
    img_eq[:, :, 2] = cv.equalizeHist(img_eq[:, :, 2])
    return img_eq
