import pandas as pd
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')

def main(file_name):
    src_csv = pd.read_csv(file_name[0])
    req_for = pd.read_csv(file_name[1])
    new_form = pd.DataFrame()

    def csv_operations():
        """ Write code here perform csv operations """
        new_form = pd.DataFrame(None,columns=req_for.columns)
        # pass

    new_form.to_csv('.\\new_format_{}.csv'.format(file_name[0].split('/')[-1].split('.')[0]))

def __init__():
    main(file_name)