import crossover
import fitnessFunction
import mutation
import readInput
import randomLists
import top
import time

start = time.clock()

city = []

readInput.readFile(city)
cityCount=len(city)

bestAns = []
#currentbestAns = []
bestVal = 10000000000
runs = 60

populationLimit = 100
population = []
population = randomLists.randomLists(populationLimit,cityCount)



for i in range(runs):
   
    j = i + 1
    print "Run#: ", j
    print bestVal
    newGeneration=[]

    for j in range(populationLimit):
        fitnessVal = fitnessFunction.fitnessFunction(population[j],city)
        if fitnessVal < bestVal:
            bestVal = fitnessVal
            bestAns = population[j]
    
    for k in range(populationLimit):
        for l in range((k+1), populationLimit):
           # child = population[k]
            child = crossover.crossover(population[k],population[l],city)
            newGeneration.append(child)

    for member in newGeneration:
        member = mutation.mutate(member)

    for m in range(populationLimit):
        newGeneration.append(population[m])

    

    population = top.top(populationLimit,newGeneration,city)



print bestAns
print bestVal

elapsed = time.clock()

print elapsed - start
