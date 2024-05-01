import matplotlib.pyplot as plt
import pandas as pd

# data downloaded April 2024; newer data may be different

# 1, read in the data ----------------
df = pd.read_csv("u32SOLNS/u323SOLNS/data.csv", header=0)    # header=0 means there is a header in row 0

# create a list of unique 'CONTRIBUTING FACTOR VEHICLE 1'
# TODO

# print("debugging unique factors:", unique_factors)




# 2, create a list of counts -----------------------
# this will require a loop
counts = []
# TODO

# print("debugging counts:", counts)
# print("checking length, must be the same")
# print(len(unique_factors))
# print(len(counts))




# 3, create a pie chart ----------------------
plt.title('Causes of accidents between motor vehicles and bicycles')
# TODO

# plt.show()

