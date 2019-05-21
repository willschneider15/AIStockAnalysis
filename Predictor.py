# Predictor is an interface to be used by other classes that can handle predicting
# and training on the data
class Predictor:
    def __init__(self):
        print("created Predictor")

    def train(self, data):
        print("trian the AI")
        #train the AI
    
    def predict(self, data=None):
        print("give prediction")
        #give a predition
        # The result is a dictionary of stocks
        # the key is the stock abbreviation (ticker symbol)
        # the value is on a scale of -1 to 1, (-1 being a bad stock, 1 being a good stock)

class samplePredictor(Predictor):
    def predict(self, data=None):
        return {'AAPL': 1}

# Sample code for creating and predicting with a predictor
# sample = samplePredictor()
# sample.predict()