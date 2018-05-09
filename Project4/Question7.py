import NeuralNet
import Testing

def main():
    trainList = [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])]
    testList = [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])]
    totalResults = []

    for i in range(0, 101):
        print "Testing with", i, "perceptrons in hidden layer."
        results = []

        for j in range(0, 10):
            if i == 0:
                results.append(NeuralNet.buildNeuralNet((trainList, testList), maxItr = 200, hiddenLayerList = [])[1])
            else:
                results.append(NeuralNet.buildNeuralNet((trainList, testList), maxItr = 200, hiddenLayerList = [i])[1])

        totalResults.append((i, max(results), Testing.average(results), Testing.stDeviation(results)))

    for i, maximum, avg, sd in totalResults:
        print i, ",", maximum, ",", avg, ",", sd

if __name__ == '__main__':
	main()
