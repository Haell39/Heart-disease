import kaggle

kaggle.api.authenticate()
kaggle.api.dataset_download_files('oktayrdeki/heart-disease', path='datasets/', unzip=True)