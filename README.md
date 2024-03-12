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

## Hint for WSL installation
- GPU and wsl : 
    - https://docs.nvidia.com/cuda/wsl-user-guide/index.html
    - (https://developer.nvidia.com) [https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local]

