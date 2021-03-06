import argparse
import csv
from time import sleep
from mettler_toledo_device import MettlerToledoDevice
from datetime import datetime
import os.path

def connect_to_device(port):
    return MettlerToledoDevice(port=port)

def create_file_with_headers_if_not_exists(path_to_csv, headers):
    if not os.path.isfile(path_to_csv): 
        with open(path_to_csv, 'w', newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(headers)

def append_to_csv(path_to_csv, data):
    with open(path_to_csv, 'a', newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read data from Mettler Toledo device and write to csv file.')
    parser.add_argument('--port', type=str, help='Port the device is connected to.', default='COM5')
    parser.add_argument('--out', type=str, help='Path to output csv file.', default='data.csv')
    parser.add_argument('--refresh', type=int, help='Refresh frequence in secomds', default=1)
    args = parser.parse_args()

    dev = connect_to_device(args.port)

    print(f'Connected to device: {dev.get_serial_number()}')

    create_file_with_headers_if_not_exists(args.out, ['Weight', 'Unit', 'Type', 'Weight Difference', 'Date Time', 'Time Step (s)', 'Time Difference (s)'])

    start_time = datetime.now()
    prev_time = start_time
    prev_weight = 0
    while True:
        current_time = datetime.now()
        row = dev.get_weight()
        # weight difference
        current_weight = row[0]
        row.append(current_weight - prev_weight)
        prev_weight = current_weight
        # current date and time
        row.append(current_time.strftime('%Y-%m-%d %H:%M:%S'))
        # time difference in seconds from start time
        row.append((current_time - start_time).total_seconds())
        # time difference in seconds from prev time
        row.append((current_time - prev_time).total_seconds())
        prev_time = current_time

        print(row)
        append_to_csv(args.out, row)
        sleep(args.refresh)
