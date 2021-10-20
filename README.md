# Rock_paper_scissor

This project is to classify whether the image is rock,paper or scissor.The whole project created as a pipeline.

### Dataset
```bash
https://www.kaggle.com/drgfreeman/rockpaperscissors
```
### Model

For the image classification VGG19 model is used.

### Files and Folders

#### Logger -> app_logger.py 
   *which is contains a customized log method.It creates log file in to the training_logs directory*
#### folder_alignment -> alignment.py
   *It is used to align the folders in to train,test and validation* 
#### uploads
   *It has the images uploaded through web app for prediction*
#### main.py
   *main file contains the creation of the flask api*
#### model_train.py 
   *It is responsible for the model training.*
#### predict.py
   *which is responsible for prediction*

#### runtime: python 3.9
