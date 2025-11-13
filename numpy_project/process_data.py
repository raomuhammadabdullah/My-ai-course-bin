import numpy as np

# 1. The filename is now simple because the file is in the same folder!
# 2. We add 'dtype=float' to prevent the secondary error you saw.
data = np.genfromtxt(r'/C:\Users\Rao Abdullah\Documents\GitHub\My-ai-course-bin\numpy_project\kaggledataset.csvkaggledataset.csv', 
                     delimiter=None, # This is usually good for CSV files
                     skip_header=0, # If you don't have a header row
                     usecols=(0, 4, 8, 9), 
                     unpack=True,
                     dtype=float)

# Optional: Print the first few values to make sure it worked
print(data[0][:5]) 

# If it works, you can unpack the data like you did before:
# ids, price, long, lat = data