import requests
import sys
import zipfile


# Function to download_data a file through http.get using requests
def download_url(url, save_path):
    """Download a file from the given url using http

    Args:
        url (str): The url from which the file need to be downloaded
        save_path (str): The filename where the contents should be saved
    Returns:
        None
    Raises:
        None
    """
    with open(save_path, "wb") as f:
        print("Downloading {} from {}...".format(save_path, url))
        response = requests.get(url, stream=True)
        total_length = response.headers.get("content-length")

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ("=" * done, " " * (50 - done)))
                sys.stdout.flush()
        print("Download succes.\n")


# Function to unzip files
def unzip_file(path_to_zip_file, directory_to_extract_to):
    """Unzip a .zip file

    Args:
        path_to_zip_file (str): The file path of the zip to extract
        directory_to_extract_to (str): The directory path where the contents should be extracted
    Returns:
        None
    Raises:
        None
    """
    print("Unzip {} to {}...".format(path_to_zip_file, directory_to_extract_to))
    with zipfile.ZipFile(path_to_zip_file, "r") as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
        print("Unzip succes.\n")
