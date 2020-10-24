#!/usr/bin/env python
# coding: utf-8

# In[21]:


import csv
with open(r'C:\Users\siddhartha\iris.data.txt.csv') as csvfile:
  lines = csv.reader(csvfile)
  for row in lines:
    print(', '.join(row))
    


# In[22]:


import csv
import random
def loadDataset(filename, split, trainingset=[], testset=[]):
    with open(filename,'r') as csvfile:
       lines = csv.reader(csvfile)
       dataset = list(lines)
       for x in range(1,len(dataset)-1):
            for y in range(4):
               dataset[x][y]= float(dataset[x][y])
            if random.random()<split:
                 trainingset.append(dataset[x])
            else:
                  testset.append(dataset[x])
                


# In[23]:


#trainingset=[]
#testset=[]
#loadDataset(r'iris.data.txt.csv',0.66,trainingset,testset)
#print("train:" +repr(len(trainingset)))
#print("test:" +repr(len(testset)))


# In[24]:


import math
def euclideanDistance(instance1, instance2, length):
    distance=0
    for x in range(length):
     distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)
        


# In[62]:


#data1=[2,2,2,'a']
#data2=[4,4,4,'b']
#distance = euclideanDistance(data1,data2,3)
#print("Distance: =" +repr(distance))


# In[88]:


import operator
def getNeighbours(trainingset, testinstance, k):
    distances = []
    length = len(testinstance)-1
    for x in range(len(trainingset)):
        dist= euclideanDistance(trainingset[x],testinstance,length)
        distances.append((trainingset[x],dist))
    distances.sort(key= operator.itemgetter(1))
    neighbours=[]
    for x in range(k):
        neighbours.append(distances[x][0])
        
    return neighbours
        


# In[64]:


#trainset=[[2,2,2,'a'],[5,5,5,'b']]
#testset=[4,4,4]
#k=2
#neigh = getNeighbours(trainset,testset,k)
#print (neigh)


# In[65]:


import operator
def getResponse(neigh):
    classVotes={}
    for x in range(len(neigh)):
        response= neigh[x][-1]
        if(response in classVotes):
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(),key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


# In[66]:


#neighbors = [[1,1,1,'b'],[2,2,2,'d'],[3,3,3,'d']]
#response = getResponse(neighbors)
#print (response)


# In[105]:


def getAccuracy(testset,predictions):
    corr=0
    for x in range(len(testset)):
        if(predictions[x] == testset[x][-1]):
            corr += 1
    return (corr/float(len(testset)))*100.0


# In[106]:


#testset = [[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'b']]
#predictions = ['a','a','a']
#acc = getAccuracy(testset,predictions)
#print (acc)


# In[107]:


def main():
    trainingset=[]
    testset=[]
    split = 0.67
    loadDataset(r'iris.data.txt.csv',split,trainingset,testset)
    print("train:" +repr(len(trainingset)))
    print("test:" +repr(len(testset)))
    predictions =[]
    k=3
    for x in range(len(testset)):
        neighbors = getNeighbours(trainingset, testset[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print ("predicted:" +repr(result) + ' ' + "actual:"+repr(testset[x][-1]))
    accuracy = getAccuracy(testset,predictions)
    print (repr(accuracy))


# In[113]:


main()


# In[ ]:





# In[ ]:





# In[ ]:




