Reference: https://arxiv.org/abs/1512.03385

|   | CoreML Top-1 | CoreML Top-5 | Source | Source Top-1 | Source Top-5 | Conversion Diff |
|---|--------------|--------------|--------|--------------|--------------|-----------------|
| [ResNet18](https://dl.dropboxusercontent.com/s/kb9cvlhq7napk0l/resnet18_torchvision.mlmodel?dl=0) | 69.75 | 89.08 | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L232) | 69.76 | 89.08 | 9.9e-6 |
| [ResNet34](https://dl.dropboxusercontent.com/s/1mswx0g912emzov/resnet34_torchvision.mlmodel?dl=0) | 73.32 | 91.43 | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L244) | 73.30 | 91.42 | 6.8e-6 |
| [ResNet50](https://dl.dropboxusercontent.com/s/s9hllnvbvxdp8j2/resnet50_torchvision.mlmodel?dl=0) | 76.11 | 92.87 | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L256) | 76.15 | 92.87 | 5.2e-6 |
| [ResNet50](https://dl.dropboxusercontent.com/s/h4rmfx72n9o1pvr/resnet50_keras_applications.mlmodel?dl=0) | 74.72 | 91.96 | [Keras](https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/resnet_common.py#L423) | 74.93	| 92.06 | 4.6e-2 |
| [ResNet101](https://dl.dropboxusercontent.com/s/xuwfhjeinndmyh2/resnet101_torchvision.mlmodel?dl=0) | 77.37 | 93.54 | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L268) | 77.37 | 93.56 | 9.4e-6 |
| [ResNet101](https://dl.dropboxusercontent.com/s/h7vuy33pyqkvehq/resnet101_keras_applications.mlmodel?dl=0) | - | - | [Keras](https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/resnet_common.py#L443) | 76.42	| 92.79 | 4.1e-2 |
| [ResNet152](https://dl.dropboxusercontent.com/s/krztu2psx1z7exx/resnet152_torchvision.mlmodel?dl=0) | - | - | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L280) | 78.31 | 94.06 | 3.9e-6 |
| [ResNet152](https://dl.dropboxusercontent.com/s/wqzr2owu8i6498m/resnet152_keras_applications.mlmodel?dl=0) | - | - | [Keras](https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/resnet_common.py#L463) | 76.60	| 93.12 | 6.8e-2 |

<table>
  <tbody>
    <tr>
      <td rowspan=3></td>
      <td rowspan=3 align="center"><b>Size, MB</b></td>
      <td colspan="5" align="center"><b>Latency, ms</b></td>
    </tr>
    <tr>
      <td colspan="3" align="center"><b>iPhone 11 Pro</b></td>
      <td colspan="2" align="center"><b>iPhone 7</b></td>
    </tr>
    <tr>
      <td><b>CPU</b></td>
      <td><b>GPU</b></td>
      <td><b>ANE</b></td>
      <td><b>CPU</b></td>
      <td><b>GPU</b></td>
    </tr>
    <tr>
      <td>ResNet18</td>
      <td>45</td>
      <td>21</td>
      <td>37</td>
      <td>37</td>
      <td>80</td>
      <td>58</td>
    </tr>
    <tr>
      <td>ResNet34</td>
      <td>83</td>
      <td>36</td>
      <td>56</td>
      <td>56</td>
      <td>150</td>
      <td>65</td>
    </tr>
    <tr>
      <td>ResNet50</td>
      <td>98</td>
      <td>92</td>
      <td>58</td>
      <td>58</td>
      <td>190</td>
      <td>72</td>
    </tr>
    <tr>
      <td>ResNet50</td>
      <td>98</td>
      <td>73</td>
      <td>45</td>
      <td>8</td>
      <td>170</td>
      <td>62</td>
    </tr>
    <tr>
      <td>ResNet101</td>
      <td>170</td>
      <td>162</td>
      <td>61</td>
      <td>61</td>
      <td>330</td>
      <td>125</td>
    </tr>
    <tr>
      <td>ResNet101</td>
      <td>171</td>
      <td>151</td>
      <td>57</td>
      <td>10</td>
      <td>310</td>
      <td>135</td>
    </tr>
    <tr>
      <td>ResNet152</td>
      <td>230</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>484</td>
      <td>205</td>
    </tr>
    <tr>
      <td>ResNet152</td>
      <td>231</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>441</td>
      <td>165</td>
    </tr>
  </tbody>
</table>
