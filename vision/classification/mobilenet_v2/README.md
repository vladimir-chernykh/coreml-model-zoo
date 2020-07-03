<table>
  <tbody>
    <tr>
      <td rowspan=3 align="center"><b>Model</b></td>
      <td rowspan=3 align="center"><b>Source</b></td>
      <td rowspan=3 align="center"><b>Size, MB</b></td>
      <td rowspan=3 align="center"><b>Input, px</b></td>
      <td rowspan=3 align="center"><b>Width multiplier</b></td>
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
      <td><a href="https://dl.dropboxusercontent.com/s/zku38e1556l9ynu/mobilenet_v2_torchvision.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/mobilenet.py#L163">PyTorch</a></td>
      <td>14</td>
      <td>224</td>
      <td>1.0</td>
      <td></td>
      <td></td>
      <td>71.88</td>
      <td>90.29</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/rufxuopv746j2po/mobilenet_v2_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>14</td>
      <td>224</td>
      <td>1.0</td>
      <td></td>
      <td></td>
      <td>71.80</td>
      <td>90.00</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

Reference: https://arxiv.org/abs/1801.04381

Inputs:
* **3-channel RGB**
* **[0-255] pixel** range

Dataset:
* [ImageNet1k](http://www.image-net.org/challenges/LSVRC/)

Versions:
* iOS 13.5.1
* XCode 11.5

Validation preprocessing:
* Resize to 256 max side while preserving the aspect ratio
* Central crop of 224x224 region
