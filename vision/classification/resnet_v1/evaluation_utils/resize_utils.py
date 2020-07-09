from PIL import Image

import torchvision.transforms as T


_transform_resize_keras_applications = T.Compose([
    T.Resize(size=256, interpolation=Image.BICUBIC),
    T.CenterCrop(size=224)
])

_transform_resize_torchvision = T.Compose([
    T.Resize(size=256, interpolation=Image.BILINEAR),
    T.CenterCrop(size=224)
])


transform_resize_dict = {
    "resnet18_v1_torchvision": _transform_resize_torchvision,
    "resnet34_v1_torchvision": _transform_resize_torchvision,
    "resnet50_v1_torchvision": _transform_resize_torchvision,
    "resnet50_v1_keras_applications": _transform_resize_keras_applications,
    "resnet101_v1_torchvision": _transform_resize_torchvision,
    "resnet101_v1_keras_applications": _transform_resize_keras_applications,
    "resnet152_v1_torchvision": _transform_resize_torchvision,
    "resnet152_v1_keras_applications": _transform_resize_keras_applications
}
