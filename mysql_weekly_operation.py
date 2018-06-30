import sys
import pymysql.cursors
from conf import server_db_info

# sql="select * from test;"

delete_audit_log="""
    delete from t_audit_log where datediff(curdate(),date)>=7;
"""

connection = pymysql.connect(host=server_db_info["ip"],
                             user=server_db_info["username"],
                             password=server_db_info["passwd"],
                             db=server_db_info["db"],
                             charset="utf8")
# print(backup_sql)
with connection.cursor() as cursor:

    cursor.execute(delete_audit_log)
    connection.commit()
    print("empty table t_audit_log successed")
# except:
#     connection.rollback()

connection.close()
