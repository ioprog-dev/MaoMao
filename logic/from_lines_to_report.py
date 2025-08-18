from utils import clean_string
from utils import replaicer
from utils import gen_report

def transgres(raw_str:str,table:dict)->str:
    raw_str = raw_str.upper()
    raw_str = clean_string(raw_str,list(table.keys()))
    return gen_report(replaicer(raw_str,table))
