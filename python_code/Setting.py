from sklearn.cross_validation import KFold

class Setting:
   
    settingName = ''
    settingDescription = ''
    
    fold = 0
    
    settingDataset = []
    settingMethod = []
    settingResult = []
    settingEvaluation = []

    def __init__(self, name, description, dataset, method, result, evaluation):
        self.settingName = name
        self.settingDescription = description
        self.settingDataset = dataset
        self.settingMethod = method
        self.settingResult = result
        self.settingEvaluation = evaluation


    def load_classify_save(self):
        data = self.settingDataset.load()
        #instances = data.keys()[0:50]
        instances = data.keys()
        
        kv = KFold(len(instances), self.fold)
        fold_count = 0
        for [train_index, test_index] in kv:
            fold_count = fold_count + 1
            print 'fold_count: ' + str(fold_count)
            training_instances = [instances[index] for index in train_index]
            testing_instances = [instances[index] for index in test_index]
            self.settingMethod.data = data
            self.settingMethod.training_instances = training_instances
            self.settingMethod.testing_instances = testing_instances
            ground_truth = [data[test_instance]['star'] for test_instance in testing_instances]
            result = self.settingMethod.classify()
            final_result = {'ground_truth': ground_truth, 'predict_result': result, 'test_instances': testing_instances}
            self.settingResult.save(fold_count, final_result)
        

