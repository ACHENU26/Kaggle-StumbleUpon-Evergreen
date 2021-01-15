# StumbleUpon Evergreen Classification Challenge
## Kaggle Competition 

#Authors :  Cédric FLAMANT & Axel CHENU 

import Algorithmia
from joblib import load
from .front import front
from .. import __version__ as version

#client = Algorithmia.client()
#model_path = client.file("data://louisdorard/models/stumbleupon" + version + ".pkl").getFile().name
#model = load(model_path)

def apply(input):
    
    o = front(input, model, env="prod")

    # TODO: log output to production database, for monitoring purposes
    # (prediction, app version, and raw feature values)
    
    return o