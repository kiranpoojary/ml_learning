import json
import pickle
import numpy as np

__locations = None
__data_cols = None
__model = None


def getPrice(loc, sqft, bhk, bath):
    try:
        loc_index = __data_cols.index(loc.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_cols))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)


def getLocNames():
    return __locations


def loadArtifacts():
    print("Loading artifacts.....")
    global __data_cols
    global __locations

    with open("./columns.json", 'r') as f:
        __data_cols = json.load(f)['data_columns']
        __locations = __data_cols[3:]
        global __model
    with open("./Project1_Bnglr_Home_Price_Model", 'rb') as f:

        __model = pickle.load(f)
        print("loaded artifacts")


if __name__ == "__main__":
    loadArtifacts()
    print(getLocNames())
    print(getPrice('1st Phase JP Nagar', 1000, 3, 3))
    print(getPrice('1st Phase JP Nagar', 1000, 2, 2))
    print(getPrice('Kalhalli', 1000, 2, 2))  # other location
    print(getPrice('Ejipura', 1000, 2, 2))  # other location
