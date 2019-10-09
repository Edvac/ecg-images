from matplotlib import pyplot
from scipy.stats import normaltest, anderson
from statsmodels.graphics.gofplots import qqplot


def is_normally_dist(patient_array):
    # Quantile - Quantile test
    # qqplot(patient_array, line='s')
    # pyplot.show()


    print("\nD’Agostino’s K^2 Test")
    stat, p = normaltest(patient_array, axis=0)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')
    # pyplot.savefig('testplot.png')
    # Image.open('testplot.png').save('testplot.jpg', 'JPEG')

    print("\nAnderson-Darling")
    result = anderson(patient_array)
    print('Statistic: %.3f' % result.statistic)
    p = 0
    for i in range(len(result.critical_values)):
        sl, cv = result.significance_level[i], result.critical_values[i]
        if result.statistic < result.critical_values[i]:
            print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
        else:
            print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))

