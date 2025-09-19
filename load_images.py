import os
from pathlib import Path
from PIL import Image

# dataset root
DATA_ROOT = "/home/hice1/kpanchal30/scratch/stone mt camera full/ProjectInfo/Best Photos"

def load_images(root):
    img_paths = []
    # walk through directory tree
    for ext in ("*.jpg", "*.jpeg", "*.png"):
        img_paths.extend(Path(root).rglob(ext))
    print(f"Found {len(img_paths)} images")

    images = []
    for path in img_paths:
        try:
            img = Image.open(path).convert("RGB")
            images.append((path, img))
            print(f"Loaded {path} | size={img.size}")
        except Exception as e:
            print(f"Failed to load {path}: {e}")
    return images

if __name__ == "__main__":
    imgs = load_images(DATA_ROOT)
    print(f"\nTotal successfully loaded: {len(imgs)}")