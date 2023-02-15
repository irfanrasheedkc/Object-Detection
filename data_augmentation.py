import albumentations as alb 
import os
import cv2
import json
import numpy as np

augmentor = alb.Compose([alb.RandomCrop(width=450 , height=450),
                         alb.HorizontalFlip(0.5),
                         alb.RandomBrightnessContrast(p=0.2),
                         alb.RandomGamma(p=0.2),
                         alb.RGBShift(p=0.2),
                         alb.VerticalFlip(p=0.5)],
                       bbox_params=alb.BboxParams(format='albumentations',
                                                 label_fields=['class_labels']))

for partition in ['train' , 'test' , 'val']:
    for image in os.listdir(os.path.join('data' , partition , 'images')):
        img = cv2.imread(os.path.join('data' , partition , 'images' , image))
        
        coords = [0,0,0.00001,0.00001]
        label_path = os.path.join('data' , partition , 'labels' , f'{image.split(".")[0]}.json')
        if os.path.exists(label_path):
                with open(label_path , 'r') as f:
                    label = json.load(f)
                coords[0] = label['shapes'][0]['points'][0][0]
                coords[1] = label['shapes'][0]['points'][0][1]
                coords[2] = label['shapes'][0]['points'][1][0]
                coords[3] = label['shapes'][0]['points'][1][1]
                coords = list(np.divide(coords , [640 , 480 , 640 , 480]))
        
        for x in range(60):
            augmented = augmentor(image=img , bboxes=[coords] , class_labels=['face'])
            cv2.imwrite(os.path.join('aug_data' , partition , 'images' , f'{image.split(".")[0]}.{x}.jpg') , augmented['image'])

            annotation = {}
            annotation['image'] = image

            if os.path.exists(label_path):
                if len(augmented['bboxes'])==0:
                    annotation['bbox']=[0,0,0,0]
                    annotation['class']=0
                else:
                    annotation['bbox']=augmented['bboxes'][0]
                    annotation['class']=1

                with open(os.path.join('aug_data' , partition , 'labels' , f'{image.split(".")[0]}.{x}.json'),'w') as f:
                    json.dump(annotation , f)