from extract_feature import extract_feature_from_name
from get_user import get_user_list
import numpy as np

data_list = []
user_list = get_user_list()
for idx, user in enumerate(user_list):
    print(idx)
    user_data = extract_feature_from_name(user)
    data_list.append(user_data)

data = np.array(data_list)
np.save(open('data.npy', 'wb'), data)
