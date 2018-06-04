from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData()
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)



pData0 = []
pData5 = []
pData10 = []
pData15 = []
pData20 = []
pData25 = []
pData30 = []
pData35 = []
pData40 = []

cData0 = []
cData5 = []
cData10 = []
cData15 = []
cData20 = []
cData25 = []
cData30 = []
cData35 = []
cData40 = []

print 'Starting Tests'

for i in range(0,5):
    print 'PenData test %d with 0 layers' %(i)
    result = testPenData(hiddenLayers = [0])
    pData0.append(result[1])

for i in range(0,5):
    result = testPenData(hiddenLayers = [5])
    pData5.append(result[1])

for i in range(0,5):
    result = testPenData(hiddenLayers = [10])
    pData10.append(result[1])

for i in range(0,5):
    result = testPenData(hiddenLayers = [15])
    pData15.append(result[1])

for i in range(0,5):
    result = testPenData(hiddenLayers = [20])
    pData20.append(result[1])

for i in range(0,5):
    result = testPenData(hiddenLayers = [25])
    pData25.append(result[1])

for i in range(0,5):
    result = testPenData(hiddenLayers = [30])
    pData30.append(result[1])

for i in range(0,5):
    result = testPenData(hiddenLayers = [35])
    pData35.append(result[1])

for i in range(0,5):
    result = testPenData(hiddenLayers = [40])
    pData40.append(result[1])






for i in range(0,5):
    print 'CarData test %d with 0 layers' %(i)
    result = testCarData(hiddenLayers = [0])
    cData0.append(result[1])

for i in range(0,5):
    result = testCarData(hiddenLayers = [5])
    cData5.append(result[1])

for i in range(0,5):
    result = testCarData(hiddenLayers = [10])
    cData10.append(result[1])

for i in range(0,5):
    result = testCarData(hiddenLayers = [15])
    cData15.append(result[1])

for i in range(0,5):
    result = testCarData(hiddenLayers = [20])
    cData20.append(result[1])

for i in range(0,5):
    result = testCarData(hiddenLayers = [25])
    cData25.append(result[1])

for i in range(0,5):
    result = testCarData(hiddenLayers = [30])
    cData30.append(result[1])

for i in range(0,5):
    result = testCarData(hiddenLayers = [35])
    cData35.append(result[1])

for i in range(0,5):
    result = testCarData(hiddenLayers = [40])
    cData40.append(result[1])




#PEN AVERAGE
ap0 = average(pData0)
ap5 = average(pData5)
ap10 = average(pData10)
ap15 = average(pData15)
ap20 = average(pData20)
ap25 = average(pData25)
ap30 = average(pData30)
ap35 = average(pData35)
ap40 = average(pData40)

print 'Average PenData: %f with 0 Hidden Layers '%(ap0)
print 'Average PenData: %f with 5 Hidden Layers '%(ap5)
print 'Average PenData: %f with 10 Hidden Layers '%(ap10)
print 'Average PenData: %f with 15 Hidden Layers '%(ap15)
print 'Average PenData: %f with 20 Hidden Layers '%(ap20)
print 'Average PenData: %f with 25 Hidden Layers '%(ap25)
print 'Average PenData: %f with 30 Hidden Layers '%(ap30)
print 'Average PenData: %f with 35 Hidden Layers '%(ap35)
print 'Average PenData: %f with 40 Hidden Layers '%(ap40)

#CAR AVERAGE
ac0 = average(cData0)
ac5 = average(cData5)
ac10 = average(cData10)
ac15 = average(cData15)
ac20 = average(cData20)
ac25 = average(cData25)
ac30 = average(cData30)
ac35 = average(cData35)
ac40 = average(cData40)

print 'Average CarData: %f with 0 Hidden Layers '%(ac0)
print 'Average CarData: %f with 5 Hidden Layers '%(ac5)
print 'Average CarData: %f with 10 Hidden Layers '%(ac10)
print 'Average CarData: %f with 15 Hidden Layers '%(ac15)
print 'Average CarData: %f with 20 Hidden Layers '%(ac20)
print 'Average CarData: %f with 25 Hidden Layers '%(ac25)
print 'Average CarData: %f with 30 Hidden Layers '%(ac30)
print 'Average CarData: %f with 35 Hidden Layers '%(ac35)
print 'Average CarData: %f with 40 Hidden Layers '%(ac40)

#PEN MAX
mp0 = max(pData0)
mp5 = max(pData5)
mp10 = max(pData10)
mp15 = max(pData15)
mp20 = max(pData20)
mp25 = max(pData25)
mp30 = max(pData30)
mp35 = max(pData35)
mp40 = max(pData40)

print 'max PenData: %f with 0 Hidden Layers '%(mp0)
print 'max PenData: %f with 5 Hidden Layers '%(mp5)
print 'max PenData: %f with 10 Hidden Layers '%(mp10)
print 'max PenData: %f with 15 Hidden Layers '%(mp15)
print 'max PenData: %f with 20 Hidden Layers '%(mp20)
print 'max PenData: %f with 25 Hidden Layers '%(mp25)
print 'max PenData: %f with 30 Hidden Layers '%(mp30)
print 'max PenData: %f with 35 Hidden Layers '%(mp35)
print 'max PenData: %f with 40 Hidden Layers '%(mp40)

#CAR MAX
mc0 = max(cData0)
mc5 = max(cData5)
mc10 = max(cData10)
mc15 = max(cData15)
mc20 = max(cData20)
mc25 = max(cData25)
mc30 = max(cData30)
mc35 = max(cData35)
mc40 = max(cData40)

print 'max CarData: %f with 0 Hidden Layers '%(mc0)
print 'max CarData: %f with 5 Hidden Layers '%(mc5)
print 'max CarData: %f with 10 Hidden Layers '%(mc10)
print 'max CarData: %f with 15 Hidden Layers '%(mc15)
print 'max CarData: %f with 20 Hidden Layers '%(mc20)
print 'max CarData: %f with 25 Hidden Layers '%(mc25)
print 'max CarData: %f with 30 Hidden Layers '%(mc30)
print 'max CarData: %f with 35 Hidden Layers '%(mc35)
print 'max CarData: %f with 40 Hidden Layers '%(mc40)



#PEN STD
sp0 = stDeviation(pData0)
sp5 = stDeviation(pData5)
sp10 = stDeviation(pData10)
sp15 = stDeviation(pData15)
sp20 = stDeviation(pData20)
sp25 = stDeviation(pData25)
sp30 = stDeviation(pData30)
sp35 = stDeviation(pData35)
sp40 = stDeviation(pData40)

print 'stDeviation PenData: %f with 0 Hidden Layers '%(sp0)
print 'stDeviation PenData: %f with 5 Hidden Layers '%(sp5)
print 'stDeviation PenData: %f with 10 Hidden Layers '%(sp10)
print 'stDeviation PenData: %f with 15 Hidden Layers '%(sp15)
print 'stDeviation PenData: %f with 20 Hidden Layers '%(sp20)
print 'stDeviation PenData: %f with 25 Hidden Layers '%(sp25)
print 'stDeviation PenData: %f with 30 Hidden Layers '%(sp30)
print 'stDeviation PenData: %f with 35 Hidden Layers '%(sp35)
print 'stDeviation PenData: %f with 40 Hidden Layers '%(sp40)

#CAR STD
sc0 = stDeviation(cData0)
sc5 = stDeviation(cData5)
sc10 = stDeviation(cData10)
sc15 = stDeviation(cData15)
sc20 = stDeviation(cData20)
sc25 = stDeviation(cData25)
sc30 = stDeviation(cData30)
sc35 = stDeviation(cData35)
sc40 = stDeviation(cData40)

print 'STD CarData: %f with 0 Hidden Layers '%(sc0)
print 'STD CarData: %f with 5 Hidden Layers '%(sc5)
print 'STD CarData: %f with 10 Hidden Layers '%(sc10)
print 'STD CarData: %f with 15 Hidden Layers '%(sc15)
print 'STD CarData: %f with 20 Hidden Layers '%(sc20)
print 'STD CarData: %f with 25 Hidden Layers '%(sc25)
print 'STD CarData: %f with 30 Hidden Layers '%(sc30)
print 'STD CarData: %f with 35 Hidden Layers '%(sc35)
print 'STD CarData: %f with 40 Hidden Layers '%(sc40)










#lolcat = (1,0.409535)
#pData.append(lolcat[1])
#print 'Testing PenData with %f accuracy'%(pData[0])

#result = testPenData()
#pData.append(result[1])
#print '1st PenData with %f accuracy'%(pData[0])
#result = testPenData()
#pData.append(result[1])
#print "2st PenData"
#result = testPenData()
#pData.append(result[1])
#print "3st PenData"
#result = testPenData()
#pData.append(result[1])
#print "4st PenData"
#result = testPenData()
#pData.append(result[1])
#print "5st PenData"

#result = testCarData()
#cData.append(result[1])
#print "1st CarData"
#result = testCarData()
#cData.append(result[1])
#print "2st CarData"
#result = testCarData()
#cData.append(result[1])
#print "3st CarData"
#result = testCarData()
#cData.append(result[1])
#print "4st CarData"
#result = testCarData()
#cData.append(result[1])
#print "5st CarData"

#ap = average(pData)
#ac = average(cData)

#mp = max(pData)
#mc = max(cData)

#sp = stDeviation(pData)
#sc = stDeviation(cData)


#print 'Average PenData: %f Average CarsData %f '%(ap,ac)
#print 'Max PenData: %f Max CarsData %f '%(mp,mc)
#print 'Std PenData: %f Std CarsData %f '%(sp,sc)
