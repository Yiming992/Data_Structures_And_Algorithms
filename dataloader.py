import cv2
import pandas as pd
import os

'''Assumptions

All images live in a single folder under working directory, and labels are stored in

a csv file with two columns. The first column with a column name image_names will store

names of image files, while the second column with a column name labels will store corresponding

labels of images

'''  

class DataLoader:


    def __init__(self,image_dir,label_path):

        '''
        image_dir: location of image directory
        label_path: path to label csv file
        '''
        self.Dir=image_dir
        self.Label=label_path
        self.Batch_Number=0
        self._couple()


    def _couple(self):
        file_names=os.listdir(self.Dir)
        df=pd.read_csv(self.Label)
        self.Collections=[(os.path.join(self.Dir,i),df[df['image_names']==i]['labels'].values) for i in file_names]
        self.Number_of_Images=len(self.Collections)


    def get_next_batch(self,batch_size,transform):

        num_batches=self.Number_of_Images//batch_size
        data_batch=[]

        if num_batches==self.Batch_Number:
            print('All images generated. Please use reset method to reset dataloader')

        else:
            batch_couple=self.Collections[self.Btach_Number*batch_size:(self.Batch_Number+1)*batch_size]
            for i in batch_couple:
                image_path=batch_couple[0]
                img=cv2.imread(image_path)

                ###apply transform function here: img=transform(img)

                label=batch_couple[1]

                data_batch.append((img,label))

            self.Batch_Number+=1

            return data_batch

    def reset(self):
        self.Batch_Number=0





        








        













