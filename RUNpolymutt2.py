import os
import argparse
import time
import subprocess

# parse arguments: VCF, PED, cores
# TODO: parse from AWS S3
def parse_input():
    parser = argparse.ArgumentParser(description='Run Polymutt2 for variant calling with VCF and PED files')
    parser.add_argument('VCF', help='Path of VCF files')
    parser.add_argument('PED', help='Path of PED files')
    parser.add_argument('cores', type=int, help='Number of cores')
    args = parser.parse_args()
    return args

def check_file_path(file_list):
    for f in file_list:
        try:
            os.path.isfile(f)
        except OSError:
            print("Can not read %s, Did you specify absolute path to file?" % f)
            return False

    return True

# Allow running as a module
if __name__ == "__main__":
    # load inputs
    args = parse_input()
    vcf_in = os.path.abspath(args.VCF)

    # check if inputs were loaded properly
    if check_file_path([vcf_in]):
        # start time
        tx = time.time()
        # end time
        print time.time() - tx