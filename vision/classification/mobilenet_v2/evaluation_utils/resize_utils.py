import numpy as np

from PIL import Image

import tensorflow.compat.v1 as tf
import torchvision.transforms as T


class CropResizeTF(object):
    """ Crops 0.875 central part and then resizes to the desired size.

    TF is used here due to the fact the the weights have been ported from TF. And TF1 has
    weird behaviour of resizing method which is hard to repeat in other frameworks.

    https://github.com/tensorflow/tensorflow/issues/6720
    """

    def __init__(self, size:int = 224):
        """ Constructor.

        Args:
            size (int): size after crop/resize operation.
        """

        super().__init__()

        self.size = size

    def __call__(self, img: Image.Image) -> Image.Image:
        """ Implements the transformation.

        Args:
            img (Image.Image): input image.

        Return:
            Transformed image.
        """

        image = np.array(img)

        image = tf.image.central_crop(image, central_fraction=0.875)
        image = tf.expand_dims(image, 0)
        image = tf.image.resize_bilinear(image, 
                                         [self.size, self.size],
                                         align_corners=False)
        image = tf.squeeze(image, [0])

        return Image.fromarray(image.numpy().astype("uint8"))


_transform_resize_keras_applications = lambda size: T.Compose([
                                                        CropResizeTF(size=size)
                                                    ])

_transform_resize_torchvision = T.Compose([
    T.Resize(size=256, interpolation=Image.BILINEAR),
    T.CenterCrop(size=224)
])


transform_resize_dict = {
    "mobilenet_v2_torchvision": _transform_resize_torchvision,
    "mobilenet_v2_1.0_224_keras_applications": _transform_resize_keras_applications(224),
    "mobilenet_v2_1.4_224_keras_applications": _transform_resize_keras_applications(224),
    "mobilenet_v2_1.3_224_keras_applications": _transform_resize_keras_applications(224),
    "mobilenet_v2_1.0_192_keras_applications": _transform_resize_keras_applications(192),
    "mobilenet_v2_1.0_160_keras_applications": _transform_resize_keras_applications(160),
    "mobilenet_v2_1.0_128_keras_applications": _transform_resize_keras_applications(128),
    "mobilenet_v2_1.0_96_keras_applications": _transform_resize_keras_applications(96),
    "mobilenet_v2_0.75_224_keras_applications": _transform_resize_keras_applications(224),
    "mobilenet_v2_0.75_192_keras_applications": _transform_resize_keras_applications(192),
    "mobilenet_v2_0.75_160_keras_applications": _transform_resize_keras_applications(160),
    "mobilenet_v2_0.75_128_keras_applications": _transform_resize_keras_applications(128),
    "mobilenet_v2_0.75_96_keras_applications": _transform_resize_keras_applications(96),
    "mobilenet_v2_0.5_224_keras_applications": _transform_resize_keras_applications(224),
    "mobilenet_v2_0.5_192_keras_applications": _transform_resize_keras_applications(192),
    "mobilenet_v2_0.5_160_keras_applications": _transform_resize_keras_applications(160),
    "mobilenet_v2_0.5_128_keras_applications": _transform_resize_keras_applications(128),
    "mobilenet_v2_0.5_96_keras_applications": _transform_resize_keras_applications(96),
    "mobilenet_v2_0.35_224_keras_applications": _transform_resize_keras_applications(224),
    "mobilenet_v2_0.35_192_keras_applications": _transform_resize_keras_applications(192),
    "mobilenet_v2_0.35_160_keras_applications": _transform_resize_keras_applications(160),
    "mobilenet_v2_0.35_128_keras_applications": _transform_resize_keras_applications(128),
    "mobilenet_v2_0.35_96_keras_applications": _transform_resize_keras_applications(96)
}
