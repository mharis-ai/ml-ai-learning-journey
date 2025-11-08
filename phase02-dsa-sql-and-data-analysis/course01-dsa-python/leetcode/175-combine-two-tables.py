import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(person,address, on = 'personId', how = 'left')
    df = df[['firstName','lastName','city','state']]
    return df