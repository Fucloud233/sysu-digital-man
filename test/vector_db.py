import sys
sys.path.append(".")

from ai_module.enhance.dboperator import DBOperator

DBOperator().reload_documents("data/sysu_data.csv")