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
      <td><a href="https://dl.dropboxusercontent.com/s/b06w1a51s7zbi2x/vgg11_torchvision.mlmodel?dl=0">VGG11</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/vgg.py#L98">PyTorch</a></td>
      <td>507</td>
      <td>-</td>
      <td>-</td>
      <td>69.02</td>
      <td>88.63</td>
      <td>55</td>
      <td>61</td>
      <td>19</td>
      <td>175</td>
      <td>93</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/7u0rtbyn3n3qmq9/vgg11_bn_torchvision.mlmodel?dl=0">VGG11_BN</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/vgg.py#L109">PyTorch</a></td>
      <td>507</td>
      <td>-</td>
      <td>-</td>
      <td>70.38</td>
      <td>89.81</td>
      <td>57</td>
      <td>61</td>
      <td>20</td>
      <td>180</td>
      <td>86</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/wr96cjsaurqoeba/vgg13_torchvision.mlmodel?dl=0">VGG13</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/vgg.py#L120">PyTorch</a></td>
      <td>508</td>
      <td>-</td>
      <td>-</td>
      <td>69.93</td>
      <td>89.25</td>
      <td>77</td>
      <td>64</td>
      <td>21</td>
      <td>302</td>
      <td>122</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/e7et32lwud9rl00/vgg13_bn_torchvision.mlmodel?dl=0">VGG13_BN</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/vgg.py#L131">PyTorch</a></td>
      <td>508</td>
      <td>-</td>
      <td>-</td>
      <td>71.55</td>
      <td>90.37</td>
      <td>78</td>
      <td>64</td>
      <td>21</td>
      <td>290</td>
      <td>116</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/d683869rozhj29p/vgg16_torchvision.mlmodel?dl=0">VGG16</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/vgg.py#L142">PyTorch</a></td>
      <td>528</td>
      <td>-</td>
      <td>-</td>
      <td>71.59</td>
      <td>90.38</td>
      <td>107</td>
      <td>87</td>
      <td>23</td>
      <td>370</td>
      <td>149</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/x6vn92nfs26rj21/vgg16_bn_torchvision.mlmodel?dl=0">VGG16_BN</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/vgg.py#L153">PyTorch</a></td>
      <td>528</td>
      <td>-</td>
      <td>-</td>
      <td>73.37</td>
      <td>91.50</td>
      <td>98</td>
      <td>86</td>
      <td>23</td>
      <td>381</td>
      <td>153</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/x3s5m4ac7abe8n1/vgg19_torchvision.mlmodel?dl=0">VGG19</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/vgg.py#L164">PyTorch</a></td>
      <td>548</td>
      <td>-</td>
      <td>-</td>
      <td>72.38</td>
      <td>90.88</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>506</td>
      <td>208</td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/wbhx0ndh5vwk1tj/vgg19_bn_torchvision.mlmodel?dl=0">VGG19_BN</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/vgg.py#L175">PyTorch</a></td>
      <td>548</td>
      <td>-</td>
      <td>-</td>
      <td>74.24</td>
      <td>91.85</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>502</td>
      <td>199</td>
    </tr>
  </tbody>
</table>

Reference: https://arxiv.org/abs/1409.1556

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
