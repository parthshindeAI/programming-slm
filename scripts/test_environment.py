import sys
import torch

print("=" * 50)
print("PROGRAMMING SLM - ENVIRONMENT CHECK")
print("=" * 50)

print(f"Python version : {sys.version}")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available : {torch.cuda.is_available()}")
print(f"PyTorch CUDA   : {torch.version.cuda}")

if torch.cuda.is_available():
    print(f"GPU            : {torch.cuda.get_device_name(0)}")
    print(
        f"GPU VRAM       : "
        f"{torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB"
    )

print("=" * 50)