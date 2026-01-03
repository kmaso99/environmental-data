import io
from PIL import Image
import torch
from torchvision import transforms, models

# Simple ImageNet labels placeholder (swap with your wildlife labels)
DEFAULT_CLASSES = [str(i) for i in range(1000)]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Transfer-learning friendly backbone (swap to efficientnet, etc.)
_model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
_model.eval()
_model.to(device)

_preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
    )
])

@torch.inference_mode()
def predict(image_bytes: bytes, class_names=None):
    class_names = class_names or DEFAULT_CLASSES

    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    x = _preprocess(img).unsqueeze(0).to(device)

    logits = _model(x)
    probs = torch.softmax(logits, dim=1)[0]
    conf, idx = torch.max(probs, dim=0)

    return {
        "class_id": int(idx.item()),
        "class_name": class_names[int(idx.item())] if int(idx.item()) < len(class_names) else str(int(idx.item())),
        "confidence": float(conf.item()),
    }
