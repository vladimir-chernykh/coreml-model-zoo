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
      <td><a href="https://dl.dropboxusercontent.com/s/7qw5bk4d9h8cmoh/densenet121_torchvision.mlmodel?dl=0">DenseNet121</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/densenet.py#L226">PyTorch</a></td>
      <td>31</td>
      <td>-</td>
      <td>-</td>
      <td>74.65</td>
      <td>92.17</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/hdlqx78i2m58k53/densenet161_torchvision.mlmodel?dl=0">DenseNet161</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/densenet.py#L240">PyTorch</a></td>
      <td>110</td>
      <td>-</td>
      <td>-</td>
      <td>77.65</td>
      <td>93.80</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/fs7h8zlkr57mrs5/densenet169_torchvision.mlmodel?dl=0">DenseNet169</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/densenet.py#L254">PyTorch</a></td>
      <td>55</td>
      <td>-</td>
      <td>-</td>
      <td>76.00</td>
      <td>93.00</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/vg2wcibplqsqctu/densenet201_torchvision.mlmodel?dl=0">DenseNet201</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/densenet.py#L268">PyTorch</a></td>
      <td>77</td>
      <td>-</td>
      <td>-</td>
      <td>77.20</td>
      <td>93.57</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

Reference: https://arxiv.org/abs/1608.06993

Inputs:
* **224x224**
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
