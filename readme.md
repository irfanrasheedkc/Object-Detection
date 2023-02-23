
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

### 6.Model Training
Pretrained model vgg16 is used for training. Output of vgg16 is given to a classification model which check wheather a face present and regression model to predict the position of the face.
Seperate loss functions are used for classification and regression.
![Model Training Loss Functions Plot](https://github.com/irfanrasheedkc/Object-Detection/blob/main/util_md/loss_tensorboard.png)

### 7.Save Model
Model saved as __facetrain.h5__ .

### 8.Real time object detection
Opencv-python is used for real time object detection . It shows a rectangle bounding object if it present in the frame.

    python real_time.py
