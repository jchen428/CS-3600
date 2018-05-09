import Testing

def main():

    for i in range(0, 41, 5):
        penResults = []
        for j in range(0, 5):
            if i == 0:
                penResults.append(Testing.testPenData([])[1])
            else:
                penResults.append(Testing.testPenData([i])[1])
            print "testPenData iteration ", j + 1, " complete with ", penResults[j], " accuracy.\n"

        print "testPenData Max = ", max(penResults)
        print "testPenData Average = ", Testing.average(penResults)
        print "testPenData Std Deviation = ", Testing.stDeviation(penResults), "\n"

    for i in range(0, 41, 5):
        carResults = []
        for j in range(0, 5):
            if i == 0:
                carResults.append(Testing.testCarData([])[1])
            else:
                carResults.append(Testing.testCarData([i])[1])
            print "testCarData iteration ", j + 1, " complete with ", carResults[j], " accuracy.\n"

        print "testCarData Max = ", max(carResults)
        print "testCarData Average = ", Testing.average(carResults)
        print "testCarData Std Deviation = ", Testing.stDeviation(carResults), "\n"

if __name__ == '__main__':
	main()

