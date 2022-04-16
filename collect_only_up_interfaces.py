import re
import csv
import os

csv_path = "/Users/zhajili/Desktop/Python/General Networking Scripts/csv_outputs" # path
regex_for_up_interfaces = r"(?P<hostname>\S+)#show"  # regex to catch all up interfaces and hostname of device
regex_pattern = re.compile(regex_for_up_interfaces)


def collect_only_up_interfaces(initial_config):
    with open(initial_config) as f:
        match = regex_pattern.search(f.read())
        if match:
            filename = os.path.join(csv_path,match.group(1) + "_int_status.csv") # save filename to directory ,here
            # hostname is taken via regex pattern and concatenated with string to get final file name ,os.path is
            # used to get path directory + filename.
            with open(filename,"w") as k:
                return "King Julien"
        else:
            print("NOTHING MATCHED!")


if __name__ == "__main__":
    collect_only_up_interfaces("device_outputs/rn2bacsw036.txt")
