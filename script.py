import sys
import os 
import requests
from tqdm import tqdm

print('''
+------------------------------+
|   . ݁₊ ⊹ . ݁ ⟡MPFree⟡ . ⊹ ₊ ݁.   |
+------------------------------+
|   NOT for streaming sites.   |
|    Purely for sites with     |
|     hosted video files.      |
+------------------------------+
|✦˚₊‧⁺˖script by happytilt˖⁺‧₊˚✦|
+------------------------------+
''')

script_path = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) != 3:
    print('Usage: python script.py <url> <output-filename.file-extension> \n')
    sys.exit(1)
else:
    print(f'\nDownloading content from:', sys.argv[1])
    print(f'\nOutputting as:{script_path}\\{sys.argv[2]}')
    while True:
        confirmation = input(f'\nConfirm? (y/n): ')
        if confirmation == 'y':
            print(f'\nProceeding with download...\n')
            break
        if confirmation == 'n':
            print(f'\nexiting...')
            sys.exit(0)
        else:
            print(f'\nNot a valid input...')
            continue 

url = sys.argv[1]
filename = sys.argv[2]

def download_file(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    chunk_size = 65536

    with open(filename, 'wb') as f, tqdm(
        desc=filename,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))
     
    return filename

download_file(url, filename)

print(f'\nAll done!')

'''
TO DO:
    - Locate MP4 files in HTTP GET Requests
    - Provide user options if multiple MP4s found
    - Clean up code
    - Experiment with download speeds
'''
