import Testing

def main():
    penResults = []
    carResults = []

    for i in range(0, 5):
        penResults.append(Testing.testPenData()[1])
        print "testPenData iteration ", i + 1, " complete with ", penResults[i], " accuracy.\n"

    for i in range(0, 5):
        carResults.append(Testing.testCarData()[1])
        print "testCarData iteration ", i + 1, " complete with ", carResults[i], " accuracy.\n"

    print "testPenData Max = ", max(penResults)
    print "testPenData Average = ", Testing.average(penResults)
    print "testPenData Std Deviation = ", Testing.stDeviation(penResults), "\n"

    print "testCarData Max = ", max(carResults)
    print "testCarData Average = ", Testing.average(carResults)
    print "testCarData Std Deviation = ", Testing.stDeviation(carResults)

if __name__ == '__main__':
	main()

