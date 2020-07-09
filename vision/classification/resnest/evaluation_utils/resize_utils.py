import numpy as np

import cv2
from PIL import Image

import torchvision.transforms as T


class CropResizePIL(object):
    """ Crops central part with small margin and then resizes to the desired size.
    """

    def __init__(self, size:int = 224):
        """ Constructor.

        Args:
            size (int): size after crop/resize operation.
        """

        self.size = size
        self.resize_method = T.Resize((self.size, self.size), interpolation=Image.BICUBIC)

    def __call__(self, img: Image.Image) -> Image.Image:
        """ Implements the transformation.

        Args:
            img (Image.Image): input image.

        Return:
            Transformed image.
        """

        image_width, image_height = img.size
        image_short = min(image_width, image_height)

        # Crop
        crop_size = float(self.size) / (self.size + 32) * image_short
        crop_height, crop_width = crop_size, crop_size
        crop_top = int(round((image_height - crop_height) / 2.))
        crop_left = int(round((image_width - crop_width) / 2.))
        img = img.crop((crop_left, crop_top, crop_left + crop_width, crop_top + crop_height))

        # Resize
        img = self.resize_method(img)

        return img


_transform_resize_torch = lambda size: T.Compose([
                                           CropResizePIL(size=size)
                                       ])


transform_resize_dict = {
    "resnest14_torch": _transform_resize_torch(224),
    "resnest26_torch": _transform_resize_torch(224),
    "resnest50_torch": _transform_resize_torch(224),
    "resnest101_torch": _transform_resize_torch(256),
    "resnest200_torch": _transform_resize_torch(320),
    "resnest269_torch": _transform_resize_torch(425)
}
