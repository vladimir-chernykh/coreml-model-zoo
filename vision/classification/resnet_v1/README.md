<table>
  <tbody>
    <tr>
      <td rowspan=3 align="center"><b>Model</b></td>
      <td rowspan=3 align="center"><b>Source</b></td>
      <td rowspan=3 align="center"><b>Size, MB</b></td>
      <td colspan=4 align="center"><b>Quality: Accuracy, %</b></td>
<!--       <td rowspan=11 align="center"></td> -->
      <td colspan=5 align="center"><b>Latency, ms</b></td>
    </tr>
    <tr>
      <td colspan="2" align="center"><b>CoreML</b></td>
      <td colspan="2" align="center"><b>Source</b></td>
      <td colspan="3" align="center"><b>iPhone 11 Pro</b></td>
      <td colspan="2" align="center"><b>iPhone 7</b></td>
    </tr>
    <tr>
      <td><b>Top-1</b></td>
      <td><b>Top-5</b></td>
      <td><b>Top-1</b></td>
      <td><b>Top-5</b></td>
      <td><b>CPU</b></td>
      <td><b>GPU</b></td>
      <td><b>ANE</b></td>
      <td><b>CPU</b></td>
      <td><b>GPU</b></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/kb9cvlhq7napk0l/resnet18_v1_torchvision.mlmodel?dl=0">ResNet18_V1</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L232">PyTorch</a></td>
      <td>45</td>
      <td>69.76</td>
      <td>89.08</td>
      <td>69.76</td>
      <td>89.08</td>
      <td>20</td>
      <td>35</td>
      <td>8</td>
      <td>78</td>
      <td>49</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/1mswx0g912emzov/resnet34_v1_torchvision.mlmodel?dl=0">ResNet34_V1</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L244">PyTorch</a></td>
      <td>83</td>
      <td>73.32</td>
      <td>91.42</td>
      <td>73.30</td>
      <td>91.42</td>
      <td>35</td>
      <td>47</td>
      <td>9</td>
      <td>150</td>
      <td>50</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/s9hllnvbvxdp8j2/resnet50_v1_torchvision.mlmodel?dl=0">ResNet50_V1</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L256">PyTorch</a></td>
      <td>98</td>
      <td>76.13</td>
      <td>92.86</td>
      <td>76.15</td>
      <td>92.87</td>
      <td>70</td>
      <td>50</td>
      <td>10</td>
      <td>186</td>
      <td>70</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/h4rmfx72n9o1pvr/resnet50_v1_keras_applications.mlmodel?dl=0">ResNet50_V1</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/resnet_common.py#L423">Keras</a></td>
      <td>98</td>
      <td>74.73</td>
      <td>91.95</td>
      <td>74.93</td>
      <td>92.06</td>
      <td>66</td>
      <td>45</td>
      <td>9</td>
      <td>170</td>
      <td>62</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/xuwfhjeinndmyh2/resnet101_v1_torchvision.mlmodel?dl=0">ResNet101_V1</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L268">PyTorch</a></td>
      <td>170</td>
      <td>77.37</td>
      <td>93.55</td>
      <td>77.37</td>
      <td>93.56</td>
      <td>165</td>
      <td>58</td>
      <td>11</td>
      <td>327</td>
      <td>119</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/h7vuy33pyqkvehq/resnet101_v1_keras_applications.mlmodel?dl=0">ResNet101_V1</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/resnet_common.py#L443">Keras</a></td>
      <td>165</td>
      <td>76.18</td>
      <td>92.58</td>
      <td>76.42</td>
      <td>92.79</td>
      <td>151</td>
      <td>55</td>
      <td>9</td>
      <td>313</td>
      <td>135</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/krztu2psx1z7exx/resnet152_v1_torchvision.mlmodel?dl=0">ResNet152_V1</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/resnet.py#L280">PyTorch</a></td>
      <td>230</td>
      <td>78.31</td>
      <td>94.05</td>
      <td>78.31</td>
      <td>94.06</td>
      <td>216</td>
      <td>75</td>
      <td>14</td>
      <td>490</td>
      <td>204</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/wqzr2owu8i6498m/resnet152_v1_keras_applications.mlmodel?dl=0">ResNet152_V1</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/resnet_common.py#L463">Keras</a></td>
      <td>231</td>
      <td>76.40</td>
      <td>92.92</td>
      <td>76.60</td>
      <td>93.12</td>
      <td>214</td>
      <td>73</td>
      <td>12</td>
      <td>441</td>
      <td>165</td>
    </tr>
  </tbody>
</table>

Reference: https://arxiv.org/abs/1512.03385

Inputs:
* **224x224**
* **3-channel RGB**
* **[0-255] pixel** range

Dataset:
* [ImageNet1k](http://www.image-net.org/challenges/LSVRC/)

Versions:
* iOS 13.5.1
* XCode 11.5
