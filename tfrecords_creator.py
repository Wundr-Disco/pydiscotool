'''\ntfrecords_creator
Create a .tfrecords from another data source. Currently only .csv is supported.
Usage: python TFRecordsCreator.py -i <input_file> -o <output_file>"
Arguments:
 -i, --input_file       The input file path
 -o, --output_file      The output tsrecords file path

Flags:
 -h      help
'''
import os
import sys
import getopt
import create_tfrecords_from_csv


def usage():
    print(sys.exit(__doc__))


def create_tsrecords_file(input_csv_file, output_file_path):

    if not output_file_path.endswith(".tfrecords"):
        output_file_path = output_file_path + ".tfrecords"
    if not os.path.exists(output_file_path):
        try:
            output_file_dir = os.path.dirname(output_file_path)
            os.makedirs(output_file_dir)
        except OSError:
            print("Creation of the directory %s failed" % output_file_dir)
        else:
            print("Successfully created the directory %s" % output_file_dir)

    create_tfrecords_from_csv.create(input_csv_file, output_file_path)


def main(argv):
    inputfile = None
    outputfile = None

    try:
        opts, _ = getopt.getopt(argv, "hi:o:", ["help", "input-file=", "output-file="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if inputfile == None:
        sys.exit("Input file is missing.")
    if outputfile == None:
        sys.exit("Output file is missing.")

    create_tsrecords_file(inputfile, outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
