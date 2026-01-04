import torch
import torch.nn as nn
from torchvision import models
from dataset import get_dataloaders

def train_model():

    train_dl, val_dl, classes = get_dataloaders()

    model = models.resnet18(pretrained=True)
    model.fc = nn.Linear(model.fc.in_features, len(classes))

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

    for epoch in range(5):
        model.train()
        for images, labels in train_dl:
            optimizer.zero_grad()
            preds = model(images)
            loss = criterion(preds, labels)
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch+1} complete")

    torch.save(model.state_dict(), "models/bird_model.pt")
    with open("models/classes.txt", "w") as f:
        f.write("\n".join(classes))

if __name__ == "__main__":
    train_model()
