from pathlib import Path
import requests

chunk_size=1024
# Create data directory
data_dir = Path('data')
if not data_dir.exists():
    print('Creating "data" directory')
    data_dir.mkdir()
# Download: delta_quantity_under_1b.npz
delta_quantity_path = Path.joinpath(data_dir,
                                    Path('delta_quantity_under_1b.npz'))
if not delta_quantity_path.exists():
    print('Downloading "delta_quantity_under_1b.npz"')
    url = ('https://raw.githubusercontent.com/dariush-bahrami/'
           'An-Observation-on-Distribution-of-Prime-Numbers/master/'
           'Jupyter%20Notebooks/data/delta_quantity_under_1b.npz')
    file_name = url.split('/')[-1].replace('%', ' ')
    response = requests.get(url, stream=True, allow_redirects=True)
    total_size = int(response.headers.get('content-length'))
    iterations = total_size//chunk_size + 1
    content = []
    for i in response.iter_content(chunk_size):                           
            if i:
                content.append(i)
    content = b''.join(content)

    with open(delta_quantity_path, mode='wb') as file:
        file.write(content)
# Download: delta_frequency_under_1b.csv
delta_frequency_path = Path.joinpath(data_dir,
                                     Path('delta_frequency_under_1b.csv'))
if not delta_frequency_path.exists():
    print('Downloading "delta_frequency_under_1b.csv"')
    url = ('https://raw.githubusercontent.com/dariush-bahrami/'
           'An-Observation-on-Distribution-of-Prime-Numbers/master/'
           'Jupyter%20Notebooks/data/delta_frequency_under_1b.csv')
    file_name = url.split('/')[-1].replace('%', ' ')
    response = requests.get(url, stream=True, allow_redirects=True)
    total_size = int(response.headers.get('content-length'))
    iterations = total_size//chunk_size + 1
    content = []
    for i in response.iter_content(chunk_size):                           
            if i:
                content.append(i)
    content = b''.join(content)
    with open(delta_frequency_path, mode='wb') as file:
        file.write(content)