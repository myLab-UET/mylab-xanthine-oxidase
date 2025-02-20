# Unveiling Potent Xanthine Oxidase Inhibitors in two Balanophora spp. Extracts using ML-based Virtual Screening and Molecular Docking Approach

Nguyen Ngoc An*, Dao Quang Tung, Le Van Tue, Nguyen Thanh Son, Nguyen Thanh Tung, Huong-Giang Le, Thai Chinh Tam, Daniel Baeker, Nguyen Thi Thuan, Do Thi Mai Dung

*Correspondence: [ngocan@vnu.edu.vn](mailto:ngocan@vnu.edu.vn) (N.N.A)

This repository is the prove of our paper, which has been submitted for publication in Link.

### Dependencies and implementation

You will need a working Python environment to run the code. The recommended way to set up your environment is through the [Anaconda Python distribution](https://www.anaconda.com/download/) which provides the `conda` package manager. Anaconda can be installed in your user directory and does not interfere with the system Python installation. The required dependencies are specified in the file `*.yml` in the `env` folder. We recommened to run the command below in Linux operating system terminal.

Run the following command in the repository folder (where `env/*.yml` files is located) to create a separate environment and install all required dependencies in it:

```
conda env create -f my-rdkit-env.yml -n your_env_name
conda env create -f tmap-env.yml -n your_other_env_name
```

Then verify that the new environment was installed correctly:

```
conda env list
```

### Project structures
- The source code are available in the src folder.
- The results of our work is in the results folder.

### Dataset location

- The train, test and validation data are available in the data_for_modeling/train_test_data folder
- The screening dataset is available in the data_for_modeling/screening_dataset.
