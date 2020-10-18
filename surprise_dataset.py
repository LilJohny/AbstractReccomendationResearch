from surprise.dataset import Dataset
from surprise.model_selection import train_test_split

def get_surprise_ml_100k(split_ratio):
    data = Dataset.load_builtin()
    data_train, data_test = train_test_split(data, split_ratio)
    return data_train, data_test



