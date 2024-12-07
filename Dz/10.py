import requests
from PIL import Image
import torch
from torchvision import models, transforms
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from io import BytesIO

url = 'https://yt3.ggpht.com/o9hTH-iMyo3WntI1iXIZWntC7An1rMliO_e8-aEiAAkMKGWruJ0KZN64SD2umWRjeQG5XCpO=s108-c-k-c0x00ffffff-no-rj'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

transform = transforms.Compose([
    transforms.ToTensor(),
])
img_tensor = transform(img).unsqueeze(0)

model_faster_rcnn = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model_faster_rcnn.eval()

with torch.no_grad():
    predictions = model_faster_rcnn(img_tensor)

confidence_threshold = 0.8

fig, ax = plt.subplots(1)
ax.imshow(img)

for element in range(len(predictions[0]['boxes'])):
    score = predictions[0]['scores'][element].item()
    if score > confidence_threshold:
        box = predictions[0]['boxes'][element].numpy()
        rect = patches.Rectangle(
            (box[0], box[1]),
            box[2] - box[0],
            box[3] - box[1],
            linewidth=2,
            edgecolor='g',
            facecolor='none'
        )
        ax.add_patch(rect)

plt.show()
