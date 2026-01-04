import os
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def get_dataloaders(data_dir="data/birds", batch_size=32):

    train_tfms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
    ])

    test_tfms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    train_ds = datasets.ImageFolder(os.path.join(data_dir, "train"), transform=train_tfms)
    val_ds   = datasets.ImageFolder(os.path.join(data_dir, "val"), transform=test_tfms)

    train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    val_dl   = DataLoader(val_ds, batch_size=batch_size)

    return train_dl, val_dl, train_ds.classes
