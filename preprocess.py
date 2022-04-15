from mne.io import concatenate_raws, read_raw_edf, RawArray
from mne.datasets import eegbci
import mne
import numpy as np
import re
import pickle

all_data = np.array([])
all_person = set()
num_loop = 0
with open('patient14.txt') as file:
    for line in file:
        file_name = line.strip()
        person_id = re.findall('[/]\d{3}[/]', file_name)[0].replace('/', '')
        
        raw_fnames = ['data_eeg/' + file_name]
        raw = concatenate_raws([read_raw_edf(f, preload=True) for f in raw_fnames])
        try:
          converted = raw.crop(0, 500)
          all_person.add(person_id)
          if len(all_data) == 0:
            all_data = converted._data[0:22, :].T
          else:
            filtered = converted._data[0:22, :].T
            all_data = np.vstack((all_data, filtered))
        except:
          pass

# print(np.stack(all_data, axis = 1).shape)
# all_data = np.array(all_data)
print(all_data.shape)
print(len(all_person))

with open('data.p', 'bw') as f:
    f.write(pickle.dumps(all_data))



# raw_fnames = ['data/train/02_tcp_le/000/00000002/s001_2002_12_23/00000002_s001_t000.edf']
# raw = concatenate_raws([read_raw_edf(f, preload=True) for f in raw_fnames])
# eegbci.standardize(raw)  # set channel names
# print('EEG INFO')
# print(raw.info)
# print(raw.info.ch_names)
# print ('EEG DATA in ARRAY FORMAT')
# print(raw._data.shape)