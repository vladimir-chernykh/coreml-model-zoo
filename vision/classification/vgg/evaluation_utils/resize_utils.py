import numpy as np

import cv2
from PIL import Image

import torchvision.transforms as T


class ResizeCropCV2(object):
    """ Resizes with preserving the aspect ratio and then crops the given PIL Image.
    """

    def __init__(self, resize_size:int = 256, crop_size:int = 224):
        """ Constructor.

        Args:
            resize_size (int): resizing size.
            crop_size (int): crop size after resizing.
        """

        super().__init__()

        self.resize_size = resize_size
        self.crop_size = crop_size

    def __call__(self, img: Image.Image) -> Image.Image:
        """ Implements the transformation.

        Args:
            img (Image.Image): input image.

        Return:
            Transformed image.
        """

        img = np.array(img)[..., ::-1]

        # Resize
        height, width, _ = img.shape
        new_height = height * self.resize_size // min(width, height)
        new_width = width * self.resize_size // min(width, height)
        img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

        # Crop
        height, width, _ = img.shape
        startx = width // 2 - (self.crop_size // 2)
        starty = height // 2 - (self.crop_size // 2)
        img = img[starty:starty + self.crop_size, startx:startx + self.crop_size][..., ::-1]

        return Image.fromarray(img)


_transform_resize_keras_applications = T.Compose([
    ResizeCropCV2()
])

_transform_resize_torchvision = T.Compose([
    T.Resize(size=256, interpolation=Image.BILINEAR),
    T.CenterCrop(size=224)
])


transform_resize_dict = {
    "vgg11_torchvision": _transform_resize_torchvision,
    "vgg11_bn_torchvision": _transform_resize_torchvision,
    "vgg13_torchvision": _transform_resize_torchvision,
    "vgg13_bn_torchvision": _transform_resize_torchvision,
    "vgg16_torchvision": _transform_resize_torchvision,
    "vgg16_keras_applications": _transform_resize_keras_applications,
    "vgg16_bn_torchvision": _transform_resize_torchvision,
    "vgg19_torchvision": _transform_resize_torchvision,
    "vgg19_keras_applications": _transform_resize_keras_applications,
    "vgg19_bn_torchvision": _transform_resize_torchvision
}
