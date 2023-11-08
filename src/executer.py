import json
import pandas as pd


class Exec:
    def __init__(self, path):
        self.path = path

    def receiver_json(self)->str:
        #print ('Hello EXEC')
        path = self.path
       
        
        #remove project_linkbr for call this function
        #path_replace = path.replace('/project_linkbr', '')
        with open(path, 'r') as f:
            data = json.load(f)
       
        return (data)

    def return_dataframe(self)->pd.DataFrame:
        json = self.receiver_json()
        json1 = json
        json1.pop('email')
        df = pd.DataFrame([json1]).T.reset_index().rename(columns={'index':'', 0:''})
        return df
    
    def email_receiver(self)->str:
        json = self.receiver_json()
        email = json['email']
        return email