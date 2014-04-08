import abc
import random

class Method:
    '''this is the classifier method'''
    methodName = ''
    methodType = ''
    methodDescription = ''
    
    k = 0
    data = {}
    training_instances = []
    testing_instances = []
    
    #function of class method
    def __init__(self, name, mType):
        self.methodName = name
        self.methodType = mType

    def classify(self):
        result = []
        for test_instance in self.testing_instances:
            test_latitude = self.data[test_instance]['latitude']
            test_longtitude = self.data[test_instance]['longtitude']
            test_categories = self.data[test_instance]['category']
            
            distance_dict = {}
            for train_instance in self.training_instances:
                train_latitude = self.data[train_instance]['latitude']
                train_longtitude = self.data[train_instance]['longtitude']
                train_categories = self.data[train_instance]['category']
                tag = False
                for category in test_categories:
                    if category in train_categories:
                        tag = True
                        break
                if tag == True:
                    distance = (test_latitude - train_latitude) ** 2 + (test_longtitude - train_longtitude) ** 2
                    if distance not in distance_dict:
                        distance_dict[distance] = []
                    distance_dict[distance].append(train_instance)
            if distance_dict == {}:
                #result.append(random.randint(0, 5))
                result.append('#')
                continue
            distance_list = distance_dict.keys()
            knn = []
            while len(knn) < self.k:
                min_distance = min(distance_list)
                distance_list.remove(min_distance)
                neighbor_list = distance_dict[min_distance]
                for neighbor in neighbor_list:
                    if len(knn) < self.k:
                        knn.append(neighbor)
                if distance_list == []:
                    break
            stars = 0.0
            for neighbor in knn:
                stars = stars + self.data[neighbor]['star']
            result.append(stars/float(len(knn)))
        return result
            
            
            
            
            

