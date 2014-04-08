
class Dataset:
    name = ''
    dataDescrition = ''
    file_folder_path = ''
    file_name = ''
    
    business = {}
    
    # constructive function
    def __init__(self, dName, dDescription):
        self.dataName = dName
        self.dataDescription = dDescription
        self.file_folder_path = ''
        self.file_name = ''
        self.business = {}

    def load(self):
        file = open(self.file_folder_path + 'business.txt', 'r')
        while 1:
            line = file.readline()
            if not line:
                break
            business_name = line.strip('\n').split(': ')[1]
            line = file.readline()
            business_id = line.strip('\n').split(': ')[1]
            line = file.readline()
            business_longtitude = float(line.strip('\n').split(': ')[1])
            line = file.readline()
            business_latitude = float(line.strip('\n').split(': ')[1])
            line = file.readline()
            business_stars = float(line.strip('\n').split(': ')[1])
            line = file.readline()
            business_categories = line.strip('\n').split(': ')[1].split(',')
            line = file.readline()
            self.business[business_id] = {'name': business_name, 'longtitude': business_longtitude, 'latitude': business_latitude, 'star': business_stars, 'category': business_categories}
        file.close()
        return self.business
            
