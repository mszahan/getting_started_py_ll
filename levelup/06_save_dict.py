import pickle

def save_dict(dict_to_save, file_path):
    ## 'wb' is for write binary
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)

def load_dict(file_path):
    ## 'rb' is for read binary
    with open(file_path, 'rb') as file:
        return pickle.load(file)