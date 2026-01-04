import torch
from torchvision import models, transforms
from PIL import Image

class BirdClassifier:

    def __init__(self):
        self.model = models.resnet18()
        self.model.fc = torch.nn.Linear(self.model.fc.in_features, 10)  # adjust later
        self.model.load_state_dict(torch.load("models/bird_model.pt", map_location="cpu"))
        self.model.eval()

        with open("models/classes.txt") as f:
            self.classes = [c.strip() for c in f.readlines()]

        self.tfms = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

    def predict(self, file):
        img = Image.open(file).convert("RGB")
        x = self.tfms(img).unsqueeze(0)
        with torch.no_grad():
            preds = self.model(x)
        idx = preds.argmax().item()
        return self.classes[idx]
