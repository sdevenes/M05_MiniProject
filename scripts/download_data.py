import requests 
import sys 
import zipfile


# Function to download a file through http.get using requests
def download_url(url, save_path):
    with open(save_path, "wb") as f:
            print("Downloading {} from {}".format(save_path, url))
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                    sys.stdout.flush()
    print()


# Function to unzip files
def unzip_file(path_to_zip_file, directory_to_extract_to):
    print("Unzip files..")
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)


if __name__ == '__main__':
  url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00506/casas-dataset.zip"
  url_test = "https://archive.ics.uci.edu/ml/machine-learning-databases/00405/Postures.zip" # Smaller zip to test
  save_path = "../data/casas-dataset.zip"
  # Download zip file
  download_url(url, save_path)
  # Unzip it
  unzip_file(save_path, "../data_test/")
  print("Done")