# StumbleUpon Evergreen Classification Challenge
## Kaggle Competition 

#Authors :  Cédric FLAMANT & Axel CHENU 

from pandas import DataFrame
import time
from .featurizer import featurization_fn
from .scorer import scoring_fn
from .thresholder import thresholding_fn, THRESHOLD
from .. import __version__ as version

def front(x_raw_json, model, env="local"):
    
    # TODO: sanitize input — client could be sending anything!

    # Turn raw input into dataframe
    x_raw = DataFrame(x_raw_json, index=[0])

    # Featurize raw input and predict
    x = featurization_fn(x_raw)
    proba = scoring_fn(x, model)

    # Prepare output
    prediction = dict()
    prediction['probabilities'] = proba.loc[0].to_dict()
    prediction['threshold'] = THRESHOLD
    prediction['is_positive'] = thresholding_fn(proba)[0]

    return dict(raw_input = x_raw_json,
                featurized_input = x.loc[0].to_dict(),
                prediction = prediction,
                time = time.asctime( time.localtime(time.time()) ),
                environment = env,
                app_version = version)