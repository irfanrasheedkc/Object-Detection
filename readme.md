
# Object Detection
Object Detection model using tensorflow.

### 1.Install Dependencies
    pip install -r requirement.txt

### 2.Data Collection using opencv
    python collect_data.py
Captured images are stored in data/images

### 3.Annotate Images with LabelMe
    labelme
- It pop up a gui .

- Open dir -> data/images

- Change output dir -> data/labels

- Select "Create Rectangle" in edit tab and select the object and give a label name.

### 4.Split datas to train , test and split.
Datas are distributed among different folder named test , train , val . Each of these folder contains images and labels.
    
    python data_split.py

### 5.Data augmentation
Datas are augmented using albumentations.The stored data along with labels will store in aug_data folder.
    
    python data_augmentation.py