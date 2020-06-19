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
      <td><a href="https://dl.dropboxusercontent.com/s/b13lpwfbiocvjnq/alexnet_torchvision.mlmodel?dl=0">AlexNet</a></td>
      <td><a href="https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/alexnet.py#L52">PyTorch</a></td>
      <td>241</td>
      <td>-</td>
      <td>-</td>
      <td>56.55</td>
      <td>79.09</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

Reference: https://arxiv.org/abs/1404.5997
