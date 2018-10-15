import hashlib     
import csv

file_to_read = input('Please provide the filename to be hashed >> ')

with open(file_to_read, 'rb') as csvfile:
    for row in file_to_read:
        print(hashlib.sha256("zyper@zyper.com".encode('utf8')).hexdigest())
