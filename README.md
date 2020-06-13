# CoreML Model Zoo

This is a collection of **Machine Learning models** converted into the [**CoreML**](https://developer.apple.com/documentation/coreml) framework. These models can run on Apple devices under one of the following operating systems: **iOS**, **macOS**, **tvOS**, **watchOS**.

All the models in the repo:
* have **pre-trained** weights
* are intended mainly for **inference**
* are **optimized** for mobile devices

Below there are few sections:
* [**Format**](#format) describes the details about the models
* [**Available Models**](#available-models) lists all the models currently supported
* [**Usage**](#usage) gives examples/links/information on how to use the models

# Format

iOS (11.0+), macOS (10.13+), tvOS (11.0+), watchOS (4.0+)
While the specified versions are the minimum required versions to be able to run CoreML models at all, I highly recommend using the latest available OS version. Otherwise, some of the models might run much slower or might even fail to run if they require some of the new features.

# Available Models

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
