from Python_packages.insert_data_functions import *
import sys

JSON = sys.argv[1]
print(f"Converting {JSON}")

DATA = open_json(JSON)
DF = json_to_dataframe(DATA)
DF_insert = load_dataset(JSON)
append_and_save_dataset(DF_insert, DF, JSON)