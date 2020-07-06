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
      <td>17</td>
      <td>14</td>
      <td>4</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/4ouyyfc6v0dlout/mobilenet_v2_1.0_224_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>14</td>
      <td>224</td>
      <td>1.0</td>
      <td></td>
      <td></td>
      <td>71.80</td>
      <td>91.00</td>
      <td>18</td>
      <td>17</td>
      <td>4</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/grgrvy0z60ln0fh/mobilenet_v2_1.4_224_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>24</td>
      <td>224</td>
      <td>1.4</td>
      <td></td>
      <td></td>
      <td>75.00</td>
      <td>92.50</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/xv9nwkxbf4h7g82/mobilenet_v2_1.3_224_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>21</td>
      <td>224</td>
      <td>1.3</td>
      <td></td>
      <td></td>
      <td>74.40</td>
      <td>92.10</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/fwdd6n12cdlhbwj/mobilenet_v2_1.0_192_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>14</td>
      <td>192</td>
      <td>1.0</td>
      <td></td>
      <td></td>
      <td>70.70</td>
      <td>90.10</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/05d4mpf19a7ak65/mobilenet_v2_1.0_160_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>14</td>
      <td>160</td>
      <td>1.0</td>
      <td></td>
      <td></td>
      <td>68.80</td>
      <td>89.00</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/iepr6mhwqd1hg89/mobilenet_v2_1.0_128_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>14</td>
      <td>128</td>
      <td>1.0</td>
      <td></td>
      <td></td>
      <td>65.30</td>
      <td>86.90</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/xf6z0wsrion7cqy/mobilenet_v2_1.0_96_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>14</td>
      <td>96</td>
      <td>1.0</td>
      <td></td>
      <td></td>
      <td>60.30</td>
      <td>83.20</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/piahmqop5fd1o2r/mobilenet_v2_0.75_224_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>10</td>
      <td>224</td>
      <td>0.75</td>
      <td></td>
      <td></td>
      <td>69.80</td>
      <td>89.60</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/u5rajuspcl9wb90/mobilenet_v2_0.75_192_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>10</td>
      <td>192</td>
      <td>0.75</td>
      <td></td>
      <td></td>
      <td>68.70</td>
      <td>88.90</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/1mjhurzv1v9rywz/mobilenet_v2_0.75_160_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>10</td>
      <td>160</td>
      <td>0.75</td>
      <td></td>
      <td></td>
      <td>66.40</td>
      <td>87.30</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/v0fn0lmwgoqk5sy/mobilenet_v2_0.75_128_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>10</td>
      <td>128</td>
      <td>0.75</td>
      <td></td>
      <td></td>
      <td>63.20</td>
      <td>85.30</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/yeaopr5f5n9dv0w/mobilenet_v2_0.75_96_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>10</td>
      <td>96</td>
      <td>0.75</td>
      <td></td>
      <td></td>
      <td>58.80</td>
      <td>81.60</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/ndsacxivkr15lrp/mobilenet_v2_0.5_224_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>7.6</td>
      <td>224</td>
      <td>0.5</td>
      <td></td>
      <td></td>
      <td>65.40</td>
      <td>86.40</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/eedk7q5dolbrqh3/mobilenet_v2_0.5_192_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>7.6</td>
      <td>192</td>
      <td>0.5</td>
      <td></td>
      <td></td>
      <td>63.90</td>
      <td>85.40</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/k9xb1octgchwqk0/mobilenet_v2_0.5_160_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>7.6</td>
      <td>160</td>
      <td>0.5</td>
      <td></td>
      <td></td>
      <td>61.00</td>
      <td>83.20</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/dj0nv00jhkqognu/mobilenet_v2_0.5_128_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>7.6</td>
      <td>128</td>
      <td>0.5</td>
      <td></td>
      <td></td>
      <td>57.70</td>
      <td>80.80</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/2d1ahbpwvzzgb47/mobilenet_v2_0.5_96_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>7.6</td>
      <td>96</td>
      <td>0.5</td>
      <td></td>
      <td></td>
      <td>51.20</td>
      <td>75.80</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/1nm8fqmfl192wi7/mobilenet_v2_0.35_224_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>6.5</td>
      <td>224</td>
      <td>0.35</td>
      <td></td>
      <td></td>
      <td>60.30</td>
      <td>82.90</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/qjcicbbeo3499bx/mobilenet_v2_0.35_192_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>6.5</td>
      <td>192</td>
      <td>0.35</td>
      <td></td>
      <td></td>
      <td>58.20</td>
      <td>81.20</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/sth6xsm8ybmx7q0/mobilenet_v2_0.35_160_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>6.5</td>
      <td>160</td>
      <td>0.35</td>
      <td></td>
      <td></td>
      <td>55.70</td>
      <td>79.10</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/08gztn6ed7b6cyp/mobilenet_v2_0.35_128_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>6.5</td>
      <td>128</td>
      <td>0.35</td>
      <td></td>
      <td></td>
      <td>50.80</td>
      <td>75.00</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="https://dl.dropboxusercontent.com/s/4fcj047wtlbh2j8/mobilenet_v2_0.35_96_keras_applications.mlmodel?dl=0">MobileNet_V2</a></td>
      <td><a href="https://github.com/keras-team/keras-applications/blob/bc89834ed36935ab4a4994446e34ff81c0d8e1b7/keras_applications/mobilenet_v2.py#L127">Keras</a></td>
      <td>6.5</td>
      <td>96</td>
      <td>0.35</td>
      <td>45.42</td>
      <td>70.33</td>
      <td>45.50</td>
      <td>70.40</td>
      <td>2</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>15</td>
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
