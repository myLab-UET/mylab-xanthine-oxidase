from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit.Chem import Descriptors, MACCSkeys
from rdkit.ML.Descriptors import MoleculeDescriptors

from tqdm import tqdm
import numpy as np

class PharmacyCommon:
    def __init__(self):
        pass
    
    def gen_maccs_fpts(self, data) -> np.ndarray:
        Maccs_fpts = []
        count = 0
        with tqdm(total=len(data), desc='Progress') as pbar:
            for i in data:
                try:
                    mol = Chem.MolFromSmiles(i)
                except:
                    print("An exception occurred with " + str(count))
                    continue
                fpts = MACCSkeys.GenMACCSKeys(mol)
                mfpts = np.array(fpts)
                Maccs_fpts.append(mfpts)
                count += 1
                pbar.update(1)  # Update the progress bar
        return np.array(Maccs_fpts)
    
    def gen_ecfp4_fpts(self, data, bits) -> np.ndarray:
        if bits not in [1024, 2048]:
            raise ValueError("Invalid value for bits. Must be either 1024 or 2048.")

        result_fpts = []
        count = 0
        with tqdm(total=len(data), desc='Progress') as pbar:
            for i in data:
                try:
                    mol = Chem.MolFromSmiles(i)
                except:
                    print("An exeption1 occurred with " + str(count))
                    count +=1
                    continue
                try: 
                    fpts = np.array(AllChem.GetMorganFingerprintAsBitVect(mol, 2, bits))
                    result_fpts.append(fpts)
                    # count += 1
                    # pbar.update(1)  # Update the progress bar
                except: 
                    print("An exception2 occurred with " + str(count))
                count +=1
                pbar.update(1) # Update the progress bar
        return np.array(result_fpts) 
    
    def gen_ecfp6_fpts(self, data, bits) -> np.ndarray:
        if bits not in [1024, 2048]:
            raise ValueError("Invalid value for bits. Must be either 1024 or 2048.")
        result_fpts = []
        count = 0
        with tqdm(total=len(data), desc='Progress') as pbar:
            for i in data:
                try:
                    mol = Chem.MolFromSmiles(i)
                except:
                    print("An exception occurred with " + str(count))
                    continue
                try:
                    fpts = np.array(AllChem.GetMorganFingerprintAsBitVect(mol, 3, bits))
                    result_fpts.append(fpts)
                except:
                    print("An exception2 occurred with " + str(count))
                count += 1
                pbar.update(1)  # Update the progress bar
        return np.array(result_fpts) 