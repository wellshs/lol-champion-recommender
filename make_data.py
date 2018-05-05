from extract_feature import extract_feature_from_name
from get_user import get_user_list
import numpy as np

data_list = []
f = open("user_list.txt", "r")
user_list = f.readlines()
f.close()

for user in user_list:
    user_data = extract_feature_from_name(user.strip())
    data_list.append(user_data)

data = np.array(data_list)
np.save(open('data.npy', 'wb'), data)
