
class Evaluation:
    """ evaluate class """
    #this is the attributes of the class evaluate
    name = ''
    evaluateDescription = ''
    
    #this is the method of class evaluate
    def __init__(self, name):
        self.name = name

    def evaluate(self, pred_result, ground_truth):
        mse = 0.0
        count = 0
        for pred_y, true_y in zip(pred_result, ground_truth):
            if pred_y != '#':
                count = count + 1
                mse = mse + (pred_y - true_y)**2
        return mse/float(count)
