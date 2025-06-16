# 🛰️ Quality Enhancement of Drone Images using SRGAN

This project implements **Super-Resolution Generative Adversarial Networks (SRGAN)** to enhance the quality and resolution of **low-resolution drone images**. SRGAN helps generate high-resolution, photo-realistic images from low-resolution inputs using deep learning techniques.

---

## 📌 Table of Contents

- [Overview](#overview)
- [SRGAN Architecture](#srgan-architecture)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Results](#results)
- [Dependencies](#dependencies)
- [References](#references)

---

## 📖 Overview

Drone images often suffer from low resolution due to hardware limitations or transmission constraints. This project enhances those images using SRGAN, a deep learning-based super-resolution model capable of recovering fine textures and sharp details.

---

## 🧠 SRGAN Architecture

SRGAN consists of two primary networks:

- **Generator**: Upscales the low-resolution image to high-resolution.
- **Discriminator**: Distinguishes between real high-resolution images and generated ones.

Additionally, it uses a **perceptual loss function** based on high-level feature representations (usually from VGG network) to produce realistic results.

---

## 📁 Project Structure

```bash
Quality-enhancement-of-drone-images/
├── train_HR_new                   # Folder for drone images high resolution           
├── train_LR_new                   #Folder for drone images low resolution
├── test_LR                       #Folder for test images low resolution
├── results/                      #enhanced output
├── dataset.py                    # Dataset class
├── mode.py                       # training and testing script
├── losses.py                     # Defining losses
├── main.py                      # Inference script
├── requirements.txt             # List of dependencies
└── ops.py                      
|__ result.txt                   #psnr values of results
|__srgan_model.py               # SRGAN architecture
|__vgg19.py                     # model

```
**SETUP:**

Clone the repository:
`git clone https://github.com/yourusername/Quality-enhancement-of-drone-images.git`
`cd Quality-enhancement-of-drone-images`

Create a virtual environment:
`python -m venv quality_env`
`source quality_env/bin/activate  # or quality_env\Scripts\activate on Windows`

Install dependencies:
`pip install -r requirements.txt`

**HOW TO RUN?**
Train the SRGAN:
`python train.py`

Run inference on drone images:
`python main.py`

**RESULTS:**

LOW RESOLUTION:

![1](https://github.com/user-attachments/assets/b0d65915-5e29-436b-82d0-f8cb2faab263) 

HIGH RESOLUTION:
![res_0000](https://github.com/user-attachments/assets/b795ffce-dc02-426b-8cf8-69092ea1f018)

PSNR: 26.0055

**HOW TO ENHANCE RESULTS FURTHER?:**

* Patch GAN is used to reduce pixelation of output while upscaling
* pixel wise loss is added along with perceptual and adversarial loss
* more residual blocks are added

The above mentioned techniques were tried to produce clearer outputs with increased PSNR values


**REFERENCES:**
Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network (SRGAN)
PyTorch Documentation
Super-Resolution in OpenCV







