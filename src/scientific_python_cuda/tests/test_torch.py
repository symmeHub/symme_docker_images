import torch

cuda_available = torch.cuda.is_available()
print("Torch CUDA available: ", cuda_available)
print("Torch version: ", torch.__version__)
print("Torch CUDA version: ", torch.version.cuda)
print("Torch device: ", torch.cuda.get_device_name(0))
