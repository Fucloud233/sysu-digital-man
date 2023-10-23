import sys
sys.path.append("./ai_module")
sys.path.append("./ai_module/enhance")

from dboperator import DBOPT

# 预加载DBOPT
if DBOPT.is_empty:
    DBOPT.load_documents('data/wiki_data.csv')