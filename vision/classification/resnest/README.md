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
      <td><a href="https://dl.dropboxusercontent.com/s/8k33evt5b2nhp5o/resnest50_torch.mlmodel?dl=0">ResNeSt50</a></td>
      <td><a href="https://github.com/zhanghang1989/ResNeSt/blob/5fe47e93bd7e098d15bc278d8ab4812b82b49414/resnest/torch/resnest.py#L33">PyTorch</a></td>
      <td>105</td>
      <td></td>
      <td></td>
      <td>81.03</td>
      <td>95.41</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/ysi35jy86mbz51y/resnest101_torch.mlmodel?dl=0">ResNeSt101</a></td>
      <td><a href="https://github.com/zhanghang1989/ResNeSt/blob/5fe47e93bd7e098d15bc278d8ab4812b82b49414/resnest/torch/resnest.py#L43">PyTorch</a></td>
      <td>185</td>
      <td></td>
      <td></td>
      <td>82.83</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/ceqvmmrgql43bq0/resnest200_torch.mlmodel?dl=0">ResNeSt200</a></td>
      <td><a href="https://github.com/zhanghang1989/ResNeSt/blob/5fe47e93bd7e098d15bc278d8ab4812b82b49414/resnest/torch/resnest.py#L53">PyTorch</a></td>
      <td>269</td>
      <td></td>
      <td></td>
      <td>83.84</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/pwwxz0t1pup8sc1/resnest269_torch.mlmodel?dl=0">ResNeSt269</a></td>
      <td><a href="https://github.com/zhanghang1989/ResNeSt/blob/5fe47e93bd7e098d15bc278d8ab4812b82b49414/resnest/torch/resnest.py#L63">PyTorch</a></td>
      <td>425</td>
      <td></td>
      <td></td>
      <td>84.54</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

Reference: https://arxiv.org/abs/2004.08955

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
