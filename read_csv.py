#!/usr/bin/env python

import csv

def main():
    with open('container-credentials.csv.sample', 'r') as f:
        reader = csv.reader(f)

        labels = []
        values = []
        for row in reader:
            if reader.line_num == 1:
                labels = row
                continue

            line = {labels[i]: row[i] for i in range(len(row))}
            values.append(line)
        
        return values

if __name__ == '__main__':
    main()
