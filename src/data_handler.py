# StumbleUpon Evergreen Classification Challenge
## Kaggle Competition 

#Authors :  Cédric FLAMANT & Axel CHENU 

def get_file_path_data(project, name, version):
    return get_file_path(project, name, version, ".csv")

def load_data(project="", name="train_full_raw", version=""):
    file_path = get_file_path_data(project, name, version)
    print("Loading data from " + str(file_path))
    return read_csv(file_path)