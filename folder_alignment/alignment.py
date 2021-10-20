import os
import shutil


class Align:

    def __init__(self,log_file,log_object,train_path,test_path,val_path):
        self.log_file = log_file
        self.log_object = log_object
        self.train_des = train_path
        self.test_des = test_path
        self.val_des = val_path
        self.path = r'C:\Users\LENOVO\Desktop\Projects\Deep Learning Projects\RockPaperScicer\rps-cv-images'

    def seperatefolder(self):
        """method = seperatefolder
        this method seperate train test and val folders
        """
        folders = os.listdir(self.path)
        for folder in folders:
            new_path = os.path.join(self.path, folder)
            train_val = os.listdir(new_path)[:round(len(os.listdir(new_path)) * 0.8)]
            train = train_val[:round(len(train_val) * 0.8)]
            for img in train:
                shutil.copy(os.path.join(new_path, img), os.path.join(self.train_des, folder))
            self.log_object.log(self.log_file,f"folder name is : {folder} train size = {len(train)}")

            test = os.listdir(new_path)[len(train_val):]
            for img in test:
                shutil.copy(os.path.join(new_path, img), os.path.join(self.test_des, folder))
            self.log_object.log(self.log_file,f"folder name is : {folder} train size = {len(test)}")

            val = train_val[len(train):]
            for img in val:
                shutil.copy(os.path.join(new_path, img), os.path.join(self.val_des, folder))
            self.log_object.log(self.log_file,f"folder name is : {folder} train size = {len(val)}")