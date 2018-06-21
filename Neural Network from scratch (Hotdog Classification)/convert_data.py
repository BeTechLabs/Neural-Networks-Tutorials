import os
import cv2
import numpy as np
import pandas as pd
from sklearn.utils import shuffle


def see_image(img_object):
	#window name will be the image size
	window_name = 'x'.join(str(tmp) for tmp in img_object.shape)
	cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
	cv2.imshow(window_name, img_object)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



def convert_data(path):
	print(path)
	storage = []
	# loop over train addresses
	for i, filename in enumerate(os.listdir(path)):
		print(i, filename)
		# print how many images are saved every 100 images
		if i % 100 == 0 and i > 1:
			print("Train data: {}".format(i))

		# read an image and resize to (224, 224)
		img = cv2.imread(path+'/'+filename)
		img = cv2.resize(img, (64, 64), interpolation=cv2.INTER_CUBIC)#
		# cv2 load images as BGR, convert it to RGB
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

		# save the image
		storage.append(img)
	return storage

def save_images(filename, d):
	#d is the dictionary
	#filename is the ouptut filename
	hf = h5py.File(filename+".h5", 'w')
	# spec_dtype = h5py.special_dtype(vlen=np.dtype('float64'))
	hf.create_dataset(filename, data=d)#, dtype=spec_dtype
	hf.close()


if __name__ == "__main__":\
	#training data
	train_hot_dog = convert_data("./data/train/hot_dog")
	train_label_hot_dog = [1 for i in range(len(train_hot_dog))]
	train_not_hot_dog = convert_data("./data/train/not_hot_dog")
	train_label_not_hot_dog = [0 for i in range(len(train_not_hot_dog))]
	df = pd.DataFrame({ "image": train_hot_dog+train_not_hot_dog,
						"label": train_label_hot_dog+train_label_not_hot_dog})
	#shuffle the data frame
	df = shuffle(df)
	df.to_hdf(path_or_buf= 'train.h5', key="train", mode= 'w')

	
	#testing data
	test_hot_dog = convert_data("./data/test/hot_dog")
	test_label_hot_dog = [1 for i in range(len(test_hot_dog))]
	test_not_hot_dog = convert_data("./data/test/not_hot_dog")
	test_label_not_hot_dog = [0 for i in range(len(test_not_hot_dog))]
	df = pd.DataFrame({ "image": test_hot_dog+test_not_hot_dog,
						"label": test_label_hot_dog+test_label_not_hot_dog})
	#shuffle the data frame
	df = shuffle(df)
	df.to_hdf(path_or_buf= 'test.h5', key="test", mode= 'w')

