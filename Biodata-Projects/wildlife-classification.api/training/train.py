import torch
import torch.nn as nn
from torchvision import models

from load_data import load_bird_dataset
from dataset import create_dataloaders

def train_model():

    # Step 1: Load dataset (toolkit or manual)
    dataset = load_bird_dataset()

    # Step 2: Create PyTorch dataloaders
    train_dl, val_dl, classes = create_dataloaders()

    # Step 3: Build model
    model = models.resnet18(pretrained=True)
    model.fc = nn.Linear(model.fc.in_features, len(classes))

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

    # Step 4: Training loop
    for epoch in range(5):
        model.train()
        for images, labels in train_dl:
            optimizer.zero_grad()
            preds = model(images)
            loss = criterion(preds, labels)
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch+1} complete")

    # Step 5: Save model + classes
    torch.save(model.state_dict(), "models/bird_model.pt")
    with open("models/classes.txt", "w") as f:
        f.write("\n".join(classes))

if __name__ == "__main__":
    train_model()
