from Dataset import Dataset
from Method import Method
from Evaluation import Evaluation
from Result import Result
from Setting import Setting
import numpy as np

#--------------------------- run the exp ----------------------------
if 1:
    k = 5
    fold = 10
    dataset = Dataset('', '')
    dataset.file_folder_path = '../data/input/'
    
    method = Method('', '')
    method.k = k
    
    evaluation = Evaluation('')
    
    result = Result('', '')
    result.k = k
    
    setting = Setting('', '', dataset, method, result, evaluation)
    setting.fold = fold
    setting.load_classify_save()

if 1:
    fold = 10
    k = 5
    
    result = Result('', '')
    result.k = k
    evaluation = Evaluation('')
    
    evaluation_result_of_each_fold = []
    for fold_count in range(1, fold + 1):
        final_result = result.load(fold_count)
        predict_result = final_result['predict_result']
        ground_truth = final_result['ground_truth']
        evaluation_result_of_each_fold.append(evaluation.evaluate(predict_result, ground_truth))
    print 'mean of MSE:' + str(np.mean(evaluation_result_of_each_fold))
    print 'std of MSE:' + str(np.std(evaluation_result_of_each_fold))
        
        
        
    