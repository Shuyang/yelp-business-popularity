import pickle

class Result:
    resultName = ''
    resultType = ''
    result_folder_path = '../result/'
    k = 0
    
    # functions of class result
    def __init__(self, name, rType):
        self.resultName = name
        self.resultType = rType

    def save(self, fold_count, result):
        file_name = 'KNN_' + str(self.k) + '_fold_' + str(fold_count)
        file = open(self.result_folder_path + file_name, 'wb')
        pickle.dump(result, file)
        file.close()
        
 
    def load(self, fold_count):
        file_name = 'KNN_' + str(self.k) + '_fold_' + str(fold_count)
        file = open(self.result_folder_path + file_name, 'rb')
        result = pickle.load(file)
        file.close()
        return result

