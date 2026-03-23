import numpy as np
import cv2

class ImageUpscaler:
    def __init__(self, scale_factor=2):
        self.scale_factor = scale_factor

    def upscale(self, image_path):
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or not accessible")

        # Upscale the image using INTER_CUBIC method for better quality
        upscaled_image = cv2.resize(image, 
                                     (image.shape[1] * self.scale_factor, 
                                      image.shape[0] * self.scale_factor), 
                                     interpolation=cv2.INTER_CUBIC)

        return upscaled_image

    def save_upscaled_image(self, upscaled_image, output_path):
        # Save the upscaled image
        cv2.imwrite(output_path, upscaled_image)

# Example usage:
# if __name__ == '__main__':
#     upscaler = ImageUpscaler(scale_factor=2)
#     upscaled = upscaler.upscale('path/to/image.jpg')
#     upscaler.save_upscaled_image(upscaled, 'path/to/upscaled_image.jpg')