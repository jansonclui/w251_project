
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from  PIL import Image
import numpy as np 
from sklearn.model_selection import train_test_split
import h5py as h5
import os 
import sys 

#get dimensions for image 

l = int(sys.argv[1])
w = int(sys.argv[2])


all_labels = os.listdir('/root/food41')
all_labels.sort()
train_data =[]
test_data =[]


#process image as numpy array 
def prepare_image(image, target,file):
   try:  

   # resize the input image and preprocess it
      image = image.resize(target)
      image = img_to_array(image)
      image = np.expand_dims(image, axis=0)
      image = imagenet_utils.preprocess_input(image)
      image=image/255.
   # return the processed image
      return image
   except Exception as e:
      print "error while processing image:",  j 
      print e


def create_label (position):
   label = [ False for i in range(100)]
   label.insert(position,True)
   return label



for i in all_labels: 
   all_data=[]
   p=all_labels.index(i)
   for j in os.listdir('/root/food41/' + i):
      target_img=prepare_image(Image.open('/root/food41/'+i+'/'+j),target=(l,w), file=i+'/'+j)
      lbl = create_label(p)
      all_data.append([lbl,target_img])
   #randomize by category 
   train_data_cat,test_data_cat = train_test_split(all_data,test_size=0.1) 
   train_data.append(train_data_cat)
   test_data.append(test_data_cat)
   print "done with", i
   
print len(train_data), len(test_data)
print train_data[0]

# separate features from labels 

categories_train = [ element[0] for element in train_data]
train_data = [element[1] for element in train_data]
categories_test = [element[0] for element in test_data]
test_data = [element[1] for element in test_data]



# load into h5 files 

with h5py.File('./food_images_train_101_64X64.h5', 'w') as hf:
   hf.create_dataset("images", data=train_data, maxshape=(None,64,64,3))
   hf.create_dataset("categories", data=categories_train, maxshape=(None, 64, 64, 1))
   hf.create_dataset("category_names", data=all_labels, maxshape=(None))



with h5py.File('./food_images_test_101_64X64.h5', 'w') as hf:
   hf.create_dataset("images", data=test_data, maxshape=(None,64,64,3))
   hf.create_dataset("categories", data=categories_test, maxshape=(None, 64, 64, 1))
   hf.create_dataset("category_names", data=all_labels, maxshape=(None))





