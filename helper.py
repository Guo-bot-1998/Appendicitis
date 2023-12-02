import pandas as pd
import os
import nibabel as nib
import torch

def read_data(directory, shift=0, termi=10):
    """
    Traverse directories starting from 'directory', find .nil files,
    and read them into NumPy arrays.
    """
    data_dict = {}
    k = 0
    ncut = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.nii'):
                if (k<shift)       :
                  k += 1
                  continue
                file_path = os.path.join(root, file)
                nii_file =  nib.load(file_path)
                data = nii_file.get_fdata()
                data_dict[file.strip('.nii')] = data
                ncut +=  1
                if ncut == termi:
                  return data_dict
    return data_dict

def read_label(excel_path):
  with open(excel_path, 'r') as f:
    df = pd.read_csv(f)
    return df


def isgpu():
    """檢查是否有 CUDA 支持的 GPU"""
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("GPU is available")
    else:
        device = torch.device("cpu")
        raise("GPU not available")
    return device