# work for preprocessing and clustering by <income> will be done here
# source for database: http://archive.ics.uci.edu/ml/datasets/Census+Income
import csv
import sys
import matplotlib.pyplot as plt
import sklearn.cluster
from sklearn.datasets import make_blobs
import numpy as np



def data_to_csv(filename):
    with open(filename) as input_file:
        lines = input_file.readlines()
        newLines = []
        for line in lines:
            newLine = line.strip().split()
            newLines.append(newLine)

    headers = ['age', 'workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country', '<=50k >50k']

    with open('output.csv', 'w') as test_file:
        file_writer = csv.writer(test_file)
        file_writer.writerow(headers)
        file_writer.writerows(newLines)


def preprocess(filename):
    retval = []
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        i = 0
        idx = 0
        for line in reader:
            # do something with each line to preprocess the data
            if i == 0:
                for word in line:
                    retval.append((word, []))
                i += 1
            else:
                for val in line:
                    retval[idx][1].append(val)
                    idx += 1
                idx = 0
        idx = 0
        age_idx = 0
        hours_idx = 0
        d1 = []
        d2 = []
        for item in retval:
            # print(item[0], min(item[1]), max(item[1]))
            if item[0] == 'age':
                age_idx = idx
            if item[0] == 'hours-per-week':
                hours_idx = idx
            idx += 1
        for i in range(len(retval[age_idx][1])):
            x = retval[age_idx][1][i]
            y = retval[hours_idx][1][i]
            point = [float(x[:-1]), float(y[:-1])]
            if i % 50 == 0:
                data.append(point)
                # d1.append(float(x[:-1]))
                # d2.append(float(y[:-1]))
            # print(retval[age_idx][1][i])
            # print(retval[cap_gain_idx][1][i])
            # print('\n')
            # print(age_idx, cap_gain_idx)
        print(data)
        # data.append(d1)
        # data.append(d2)
        return data     # formatted (age, hours worked a week)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        data_filename = sys.argv[1]
        cluster_number = int(sys.argv[2])
    else:
        data_filename = 'output.csv'
        cluster_number = 1
    data_to_csv('adult.data')
    data = preprocess(data_filename)
    # X, Y = make_blobs(data, n_features=2)
    # print('X: ', X)

    ag = sklearn.cluster.DBSCAN(2, 3, 'euclidean')
    fit = ag.fit_predict(data)
    # for i in fit:
    #     print(i)

    # db = pyclustering.cluster.dbscan.dbscan(data, 2, 2, False)
    # ag = pyclustering.cluster.agglomerative.agglomerative(data, 8, None, False)
    #
    # db_clusters = db.get_clusters()
    # db_noise = db.get_noise()
    #
    # ag_clusters = ag.get_clusters()
    #
    # print('db:\n\tclusters: ', db_clusters)
    # print('\tnoise: ', db_noise)
    # print('ag:\n\tclusters: ', ag_clusters)
    # if db_clusters.__len__() > 0:
    #     db.process()
    # else:
    #     print('no DB clusters :(')
    #
    # if ag_clusters.__len__() > 0:
    #     ag.process()
    # else:
    #     print('no AG clusters :(')
    #



    # save_filename = data_filename.replace('.csv', '_hc_cluster.csv')

    # data = loadDataSet(data_filename)

    # clusterAssment = agglomerative_with_min(data, cluster_number)
    #
    # saveData(save_filename, data, clusterAssment)
