from dboperator import DBOPT

# 预加载DBOPT
if DBOPT.is_empty:
    DBOPT.load_documents('data/wiki_data.csv')