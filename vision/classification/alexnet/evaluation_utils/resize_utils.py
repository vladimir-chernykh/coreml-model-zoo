from PIL import Image

import torchvision.transforms as T


_transform_resize_torchvision = T.Compose([
    T.Resize(size=256, interpolation=Image.BILINEAR),
    T.CenterCrop(size=224)
])


transform_resize_dict = {
    "alexnet_torchvision": _transform_resize_torchvision
}
