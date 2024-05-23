# symme_docker_images
Docker images from SYMME lab.

# How to bluid the images
## the scientific python image
execute the following command in the `scientific_python` directory:
```bash
sh build_image.sh
```
## the scientific python image with cuda support
execute the following command in the `scientific_python_cuda` directory:
```bash
sh build_image.sh
```

## An image for ortools
execute the following command in the `ortools_python` directory:
```bash
sh build_image.sh
```

## Build images using Windows / WSL2
### Pre-requisites
- Install WSL2
- install an Ubuntu distribution from the Microsoft Store
- Install Docker Desktop and enable WSL2 integration of the Ubuntu distribution
- If you want to use the GPU, you need to install the NVIDIA driver and the CUDA toolkit on your PC (not into the Ubuntu distro), detail are available at the following links: https://docs.nvidia.com/cuda/wsl-user-guide/index.html, and (https://developer.nvidia.com) [https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local]

### Build the images
- Open the Ubuntu distribution in WSL
- Clone this repository in the Ubuntu distribution (This is a way to avoid the problem of the line endings of the files formatted in Windows)
- Go to the directory of the image you want to build by excuting the following command:
```bash
sh build_image.sh
```




