import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_images


image_data=load_sample_images()
print(image_data)
print(type(image_data))
print(type(image_data.images[0]))


#applying the operations of EDA
data=pd.DataFrame(load_sample_images.data,columns=load_sample_images.feature_name)
print(data.head(9))




