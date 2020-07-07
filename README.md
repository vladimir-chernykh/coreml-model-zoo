# CoreML Model Zoo

This is a collection of **Machine Learning models** converted into the [**CoreML**](https://developer.apple.com/documentation/coreml) framework. These models can run on Apple devices under one of the following operating systems: **iOS**, **macOS**, **tvOS**, **watchOS**.

All the models in the repo:
* have **pre-trained** weights
* are intended mainly for **inference**
* are **optimized** for mobile devices

Below there are few sections:
* [**Format and Available Models**](#format-and-available-models) describes all the models available and details about them
* [**Usage**](#usage) gives examples/links/information on how to use the models

# Format and Available models

All models should be run on one of the following systems: iOS (11.0+), macOS (10.13+), tvOS (11.0+), watchOS (4.0+). While the specified versions are the minimum required versions to be able to run CoreML models at all, it is highly recommended to use the **latest available OS version**. Otherwise, some of the models might run much slower or might even fail to run if they require some of the new features.

Currently only **Computer Vision** models are presented. In future, Natural Language Processing and Speech Processing models might be ported as well and any contribution is welcomed.

Each model has:
* Model file in the format of **\*.mlmodel**
* Model **size** in MB
* **Input** size in pixels
* **Quality metrics** both for source and converted versions
* **Performance metrics** such as latency/RPS for different mobile devices (iPhone 7, iPhone 11 Pro) and accelerators (CPU, GPU, ANE).

For more info on how the performance is measured please look in the [coreml-performance](https://github.com/vladimir-chernykh/coreml-performance) repo.

## Computer Vision models

All the Computer Vision models are placed under [`vision`](./vision) folder and are split by problem they are solving.

**Inputs** to all the models are **unified**:
* **3-channel RGB**
* **[0-255] pixel** range

All the necessary **preprocessing** steps are already **embedded** into the model so that the user should not worry about that.

### Classification

| Model | Reference | Year |
|-------|-----------|------|
| [AlexNet](./vision/classification/alexnet) | ["One weird trick for parallelizing convolutional neural networks"](https://arxiv.org/abs/1404.5997) | 2012 |
| [VGG](./vision/classification/vgg) | ["Very Deep Convolutional Networks for Large-Scale Image Recognition"](https://arxiv.org/abs/1409.1556) | 2014 |
| [ResNetV1](./vision/classification/resnet_v1) | ["Deep Residual Learning for Image Recognition"](https://arxiv.org/abs/1512.03385) | 2015 |
| [DenseNet](./vision/classification/densenet) | ["Densely Connected Convolutional Networks"](https://arxiv.org/abs/1608.06993) | 2017 |
| [MobileNetV2](./vision/classification/mobilenet_v2) | ["MobileNetV2: Inverted Residuals and Linear Bottlenecks"](https://arxiv.org/abs/1801.04381) | 2018 |
| [ResNeSt](./vision/classification/resnest) | ["ResNeSt: Split-Attention Networks"](https://arxiv.org/abs/2004.08955) | 2020 |

# Usage

The easiest way to run the Coputer Vision models on device is to use [**Apple Vision**](https://developer.apple.com/documentation/vision) library and auto-generated code for the **\*.mlmodel** file. Below is an example for [`resnet18_v1_torchvision`](./vision/classification/resnet_v1) model (see [this tutorial](https://developer.apple.com/documentation/vision/classifying_images_with_vision_and_core_ml) for more). Note that there is no error processing in this example which should be a must-have in real application.

```swift
import Vision
import CoreImage

let model = try VNCoreMLModel(for: resnet18_v1_torchvision().model)

let request = VNCoreMLRequest(model: model)
request.imageCropAndScaleOption = .centerCrop

let handler = VNImageRequestHandler(ciImage: ciImage)
try! handler.perform([request])

let results = emotionsRequest.results! as! [VNClassificationObservation]
```

There are other ways to use raw CoreML model without any frameworks. One might find example of this in the [coreml-performance](https://github.com/vladimir-chernykh/coreml-performance) repo.
