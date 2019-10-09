
import numpy


def calc_standard_deviation(dataset, sample):

    # std = sqrt(mean(abs(x - x.mean())**2))
    if sample:
        print("\n STD of a sample: " + str(numpy.std(dataset, ddof = 1)))
    else:
        print("\n STD of the total population: " + str(numpy.std(dataset, ddof = 0)))