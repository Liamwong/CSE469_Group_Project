# work for preprocessing and clustering by <income> will be done here
# source for database: http://archive.ics.uci.edu/ml/datasets/Census+Income
import csv
import sys


def data_to_csv(filename):
    with open(filename) as input_file:
        lines = input_file.readlines()
        newLines = []
        for line in lines:
            newLine = line.strip().split()
            newLines.append(newLine)

    headers = ['age', 'workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country', '<=50k >50k']

    with open('output.csv', 'wb') as test_file:
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
        for item in retval:
            # print(item[0], min(item[1]), max(item[1]))
            if item[0] == 'age':
                age_idx = idx
            if item[0] == 'hours-per-week':
                hours_idx = idx
            idx += 1
        for i in range(len(retval[age_idx][1])):
            data.append([retval[age_idx][1][i], retval[hours_idx][1][i]])
            # print(retval[age_idx][1][i])
            # print(retval[cap_gain_idx][1][i])
            # print('\n')
            # print(age_idx, cap_gain_idx)
        # print(data)
        return data     # formatted (age, hours worked a week)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        data_filename = sys.argv[1]
        cluster_number = int(sys.argv[2])
    else:
        data_filename = 'output.csv'
        cluster_number = 1
    data_to_csv('adult.data')
    preprocess(data_filename)




    # save_filename = data_filename.replace('.csv', '_hc_cluster.csv')

    # data = loadDataSet(data_filename)

    # clusterAssment = agglomerative_with_min(data, cluster_number)
    #
    # saveData(save_filename, data, clusterAssment)
