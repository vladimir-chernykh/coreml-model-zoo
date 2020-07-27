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
      <td><a href="https://dl.dropboxusercontent.com/s/knqjsvn72szjunq/densenet121_torchvision.mlmodel?dl=0">DenseNet121</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/densenet.py#L226">PyTorch</a></td>
      <td>31</td>
      <td></td>
      <td></td>
      <td>74.65</td>
      <td>92.17</td>
      <td>50</td>
      <td>62</td>
      <td>9</td>
      <td>140</td>
      <td>80</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/wj9i9f8ki9d3c69/densenet121_keras_applications.mlmodel?dl=0">DenseNet121</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/densenet.py#L300">Keras</a></td>
      <td>31</td>
      <td></td>
      <td></td>
      <td>75.00</td>
      <td>92.30</td>
      <td>65</td>
      <td>61</td>
      <td>7</td>
      <td>150</td>
      <td>74</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/2p7k1u5n8a4upst/densenet161_torchvision.mlmodel?dl=0">DenseNet161</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/densenet.py#L240">PyTorch</a></td>
      <td>110</td>
      <td></td>
      <td></td>
      <td>77.65</td>
      <td>93.80</td>
      <td>195</td>
      <td>74</td>
      <td>16</td>
      <td>378</td>
      <td>210</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/grs1l8j06mza2pk/densenet169_torchvision.mlmodel?dl=0">DenseNet169</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/densenet.py#L254">PyTorch</a></td>
      <td>55</td>
      <td></td>
      <td></td>
      <td>76.00</td>
      <td>93.00</td>
      <td>92</td>
      <td>62</td>
      <td>10</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/siiwu6pbhy4m3td/densenet169_keras_applications.mlmodel?dl=0">DenseNet169</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/densenet.py#L314">Keras</a></td>
      <td>55</td>
      <td></td>
      <td></td>
      <td>76.20</td>
      <td>93.20</td>
      <td>91</td>
      <td>61</td>
      <td>7</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/sz6eo05n5drrhvv/densenet201_torchvision.mlmodel?dl=0">DenseNet201</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/densenet.py#L268">PyTorch</a></td>
      <td>77</td>
      <td></td>
      <td></td>
      <td>77.20</td>
      <td>93.57</td>
      <td>132</td>
      <td>65</td>
      <td>14</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/9fxmcibsogbiq8d/densenet201_keras_applications.mlmodel?dl=0">DenseNet201</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/densenet.py#L328">Keras</a></td>
      <td>77</td>
      <td></td>
      <td></td>
      <td>77.30</td>
      <td>93.60</td>
      <td>129</td>
      <td>61</td>
      <td>10</td>
      <td></td>
      <td></td>
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
