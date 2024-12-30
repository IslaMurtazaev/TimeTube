import csv


def write(filename, data):
    print('\nStart generating CSV file\n')

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print('\nFinish generating CSV file\n')
