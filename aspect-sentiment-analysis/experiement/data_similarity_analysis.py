import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def plot_scatter_graph(x_list, y_list, z_list):

    # plots the scatter graph of 2 variables
    # this is simply for my own use
    plt.scatter(x_list, list(range(len(x_list))), c='orange')
    plt.scatter(y_list, list(range(len(y_list))), c='blue')
    plt.scatter(z_list, list(range(len(z_list))))

    plt.show()

# plot the histograms
def plot_histogram_of_scores(scores_vaccine, scores_vaccines, scores_vaccination, bins=25, type="neutral"):

    fig = plt.figure()

    fig.suptitle(f"Distribution of {type} Scores for Aspects: Vaccine, Vaccines and Vaccinations", fontsize=14)
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    n, bins, patches = ax1.hist(scores_vaccine, bins=bins, color='r')
    ax1.set_xlabel('Aspect: "vaccine"')
    ax1.set_ylabel('Frequency')
    ax1.legend([f'{type} score for "vaccine"'])

    n, bins, patches = ax2.hist(scores_vaccines, bins=bins, color='b')
    ax2.set_xlabel('Aspect: "vaccines"')
    ax2.set_ylabel('Frequency')
    ax2.legend([f'{type} score for "vaccines"'])

    n, bins, patches = ax3.hist(scores_vaccination, bins=bins, color='g')
    ax3.set_xlabel('Aspect: "vaccination"')
    ax3.set_ylabel('Frequency')
    ax3.legend([f'{type} score for "vaccination"'])
    plt.show()

def show_correlations(data_x, data_y):

    # get the pearson correlation coeffecients
    pearson = np.corrcoef(data_x, data_y)

    # get the cov matrix
    cov_matrix = np.cov(data_x, data_y)

    return pearson, cov_matrix

def main():

    # file paths
    path_to_control = "control_data/control_dataset.csv"

    control_df = pd.read_csv(path_to_control)

    type = 'neutral'

    # compare the negative results for the control
    scores_vaccine = control_df[f"vaccine_{type}"].values
    scores_vaccines = control_df[f"vaccines_{type}"].values
    scores_vaccination = control_df[f"vaccination_{type}"].values

    # plot_histogram_of_scores(scores_vaccine, scores_vaccines, scores_vaccination, bins=50, type=type)
    #
    # #### get some summary stats
    # print(f'Average for "vaccine" : {np.mean(scores_vaccine)}')
    # print(f'Standard Deviation for "vaccine" : {np.std(scores_vaccine)}')
    # print(f'Average for "vaccines" : {np.mean(scores_vaccines)}')
    # print(f'Standard Deviation for "vaccines" : {np.std(scores_vaccines)}')
    # print(f'Average for "vaccination" : {np.mean(scores_vaccination)}')
    # print(f'Standard Deviation for "vaccination" : {np.std(scores_vaccination)}')

    # # get the correlations0
    data_x, data_y = scores_vaccines, scores_vaccination

    pearson, cov = show_correlations(data_x, data_y)

    # show the correlation coefficients
    print(f'\n\nCovariance Matrix: {cov}')
    print(f'Correlation Coeff between variables: {pearson[0][1]}')

    # calculate the t-test independents
    t2, p2 = stats.ttest_ind(data_x, data_y)
    print(f'\n\nCalculated T-Statistic: {t2}')
    print(f'Two-Tailed P-value: {p2}')




    pass

if __name__ == "__main__":
    main()