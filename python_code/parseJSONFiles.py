
import json
from StringIO import StringIO

sourceDir = '../data/original'
targetDir = '../data/input'

def preprocessBusinessFile():
    inFile = open(sourceDir + "/yelp_academic_dataset_business.json")
    outFile = open(targetDir + "/business.txt",'w')
    
    for line in inFile:
        io = StringIO(line)
        businessObject = json.load(io)
        name = businessObject[u'name']
        business_id = businessObject[u'business_id']
        longitude = businessObject[u'longitude']
        latitude = businessObject[u'latitude']
        stars = businessObject[u'stars']
        categories = businessObject[u'categories']   
         
        outFile.write('name: %s\nid: %s\nlongtitude: %d\nlatitude: %d\nstars: %f\n' 
                      % (name, business_id, longitude, latitude, stars))
        outFile.write('categories: %s\n\n' % (','.join(categories)))  
    inFile.close()
    outFile.close()
    
def preprocessReviewFile():
    inFile = open(sourceDir + "/yelp_academic_dataset_review.json")
    reviewFile = open(targetDir + "/review.csv",'w')
    businessReviewSummary = {}
    reviewFile.write('business_id,date,stars\n')
    
    for line in inFile:
        io = StringIO(line)
        reviewObject = json.load(io)
        business_id = reviewObject[u'business_id']
        date = reviewObject[u'date']
        stars = reviewObject[u'stars']

        reviewFile.write('%s,%s,%f\n' % (business_id,date,stars))
        
        if business_id in businessReviewSummary:
            businessReviewSummary[business_id][0] += stars
            businessReviewSummary[business_id][1] += 1
        else:
            businessReviewSummary[business_id] = [stars, 1]
    reviewFile.close()
    businessReviewFile = open(targetDir + "/business_review_summary.csv",'w')
    businessReviewFile.write('business_id, num_review,ave_stars\n')
    for business_id, summary in businessReviewSummary.iteritems():
        businessReviewFile.write('%s,%d,%f\n' % 
                                 (business_id,summary[1],summary[0]/summary[1]))
    businessReviewFile.close()
    
if __name__ == '__main__':
    preprocessBusinessFile()
    preprocessReviewFile()
    
    
    