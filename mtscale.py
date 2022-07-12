import argparse
import csv
from time import sleep
from mettler_toledo_device import MettlerToledoDevice

def connect_to_device(port):
    return MettlerToledoDevice(port=port)

def append_to_csv(path_to_csv, data):
    with open(path_to_csv, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read data from Mettler Toledo device and write to csv file.')
    parser.add_argument('--port', type=str, help='Port the device is connected to.', default='COM5')
    parser.add_argument('--out', type=str, help='Path to output csv file.', default='data.csv')
    parser.add_argument('--refresh', type=int, help='Seconds between data refresh', default=1)
    args = parser.parse_args()

    dev = connect_to_device(args.port)

    print(f'Connected to device: {dev.get_serial_number()}')

    while True:
        append_to_csv(args.out, dev.get_weight())
        sleep(args.refresh)
