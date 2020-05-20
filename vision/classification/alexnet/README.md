Reference: https://arxiv.org/abs/1512.03385

|   | CoreML Top-1 | CoreML Top-5 | Source | Source Top-1 | Source Top-5 | Conversion Diff |
|---|--------------|--------------|--------|--------------|--------------|-----------------|
| [AlexNet](https://dl.dropboxusercontent.com/s/b13lpwfbiocvjnq/alexnet_torchvision.mlmodel?dl=0) | - (+0.00) | - (+0.00) | [PyTorch](https://github.com/pytorch/vision/blob/7aea80c9497ff78353fef1d9699490c5da6f41b6/torchvision/models/alexnet.py#L52) | 56.55 | 79.09 | 7.2e-6 |

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
      <td>AlexNet</td>
      <td>241</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
