import sys
import argparse
import os.path
from rr.download_data import download_data


def main():

    parser = argparse.ArgumentParser(
        description="M05 mini-project: Download dataset.zip online"
    )
    parser.add_argument("source", type=str, help="Data zip url")
    parser.add_argument("destination", type=str, help="Destination folder")
    args = parser.parse_args()

    download_destination = os.path.join(args.destination + "/dataset.zip")
    download_data.download_url(args.source, download_destination)
    download_data.unzip_file(download_destination, args.destination)


if __name__ == "__main__":
    sys.exit(main())
