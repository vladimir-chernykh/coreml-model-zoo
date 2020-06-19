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
* Model **size**
* **Quality metrics** both for source and converted versions
* **Performance metrics** such as latency/RPS for different mobile devices (iPhone 7, iPhone 11 Pro) and accelerators (CPU, GPU, ANE)

## Computer Vision models

All the Computer Vision models are placed under [`vision`](./vision) folder and are split by problem they are solving.

**Inputs** to all the models are **unified**:
* **3-channel RGB**
* **[0-255] pixel** range

All the necessary **preprocessing** steps are already **embedded** into the model so that the user should not worry about that.

### Classification

| Model | Reference | Year |
|-------|-----------|------|
| [ResNetV1](./vision/classification/resnet_v1) | ["Deep Residual Learning for Image Recognition"](https://arxiv.org/abs/1512.03385) | 2015 |

# Usage

# Targets
- [ ] Model Zoo
  - [x] Model file
  - [ ] Description
  - [x] Source
  - [x] Statistical quality
  - [x] Speed
  - [ ] Quantization
  - [x] All preprocessing in network, input is RGB 0-255
  - [ ] Flexible input shape (possibly)
  - [ ] Example of usage
  - [x] Tests including the conversion quality test
- [ ] Example app
  - [ ] Launch every model from the zoo
  - [ ] Process and show results
