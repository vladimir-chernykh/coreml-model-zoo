Reference: https://arxiv.org/abs/1512.03385

|   | CoreML Top-1 | CoreML Top-5 | Source | Source Top-1 | Source Top-5 | Conversion Diff |
|---|--------------|--------------|--------|--------------|--------------|-----------------|
| [ResNet18](https://dl.dropboxusercontent.com/s/kb9cvlhq7napk0l/resnet18_torchvision.mlmodel?dl=0) | 69.75 | 89.08 | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L232) | 69.76 | 89.08 | 0.0158 |
| [ResNet34](https://dl.dropboxusercontent.com/s/1mswx0g912emzov/resnet34_torchvision.mlmodel?dl=0) | 73.32 | 91.43 | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L244) | 73.30 | 91.42 | 0.0193 |
| [ResNet50](https://dl.dropboxusercontent.com/s/s9hllnvbvxdp8j2/resnet50_torchvision.mlmodel?dl=0) | 76.11 | 92.87 | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L256) | 76.15 | 92.87 | 0.0183 |
| [ResNet50](https://dl.dropboxusercontent.com/s/h4rmfx72n9o1pvr/resnet50_keras_applications.mlmodel?dl=0) | 74.72 | 91.96 | [Keras](https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/resnet_common.py#L423) | 74.93	| 92.06 | 0.0463 |
| [ResNet101](https://dl.dropboxusercontent.com/s/xuwfhjeinndmyh2/resnet101_torchvision.mlmodel?dl=0) | 77.37 | 93.54 | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L268) | 77.37 | 93.56 | 0.0454 |
| [ResNet101](https://dl.dropboxusercontent.com/s/h7vuy33pyqkvehq/resnet101_keras_applications.mlmodel?dl=0) | - | - | [Keras](https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/resnet_common.py#L443) | 76.42	| 92.79 | 0.0413 |
| [ResNet152](https://dl.dropboxusercontent.com/s/krztu2psx1z7exx/resnet152_torchvision.mlmodel?dl=0) | - | - | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L280) | 78.31 | 94.06 | 0.0803 |
| [ResNet152](https://dl.dropboxusercontent.com/s/wqzr2owu8i6498m/resnet152_keras_applications.mlmodel?dl=0) | - | - | [Keras](https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/resnet_common.py#L463) | 76.60	| 93.12 | 0.0676 |

<table>
  <tbody>
    <tr>
      <td rowspan=3></td>
      <td rowspan=3 align="center">Size, MB</td>
      <td colspan="5" align="center">Latency, ms</td>
    </tr>
    <tr>
      <td colspan="3" align="center">iPhone 11 Pro</td>
      <td colspan="2" align="center">iPhone 7</td>
    </tr>
    <tr>
      <td>CPU</td>
      <td>GPU</td>
      <td>ANE</td>
      <td>CPU</td>
      <td>GPU</td>
    </tr>
    <tr>
      <td>ResNet18</td>
      <td>45</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>78</td>
      <td>56</td>
    </tr>
    <tr>
      <td>ResNet34</td>
      <td>83</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>150</td>
      <td>65</td>
    </tr>
    <tr>
      <td>ResNet50</td>
      <td>98</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>200</td>
      <td>72</td>
    </tr>
    <tr>
      <td>ResNet50</td>
      <td>98</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>188</td>
      <td>62</td>
    </tr>
    <tr>
      <td>ResNet101</td>
      <td>170</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>ResNet101</td>
      <td>171</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>ResNet152</td>
      <td>230</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>ResNet152</td>
      <td>231</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>
