import hashlib
import csv


def open_file():
    file_to_read = input(
        'Please provide the filename to be hashed (we assume the file has headers!) >> ')

    hash(file_to_read)


def hash(file_to_read):
    hashes = []
    with open(file_to_read, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            hashes.append(hashlib.sha256(row[0].encode('utf8')).hexdigest())

        write_hashes(hashes)


def write_hashes(hashes):
    file_to_write = input('What do you want the output to be called? >> ')
    filename = '{}.txt'.format(file_to_write)
    with open(filename, 'w') as out:
        for hash in hashes:
            out.write(hash+'\n')


if __name__ == '__main__':
    open_file()
