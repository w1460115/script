import sys
import pymysql.cursors
from conf import server_db_info

# sql="select * from test;"
backup_sql = """
    insert into {table_name}_his (select * from {table_name} where {date_key} BETWEEN \'{start_date}\' and \'{end_date}\')
"""
delete_sql="""
    delete from test where date BETWEEN \'{start_date}\' and \'{end_date}\'
"""
delete_audit_log="""
    delete from t_audit_log where datediff(curdate(),date)>=7;
"""

# table_name=input("table_name:")
# start_date = input("start_date:")
# end_date = input("end_date:")

table_name=sys.argv[1]
date_key=sys.argv[2]
start_date=sys.argv[3]
end_date=sys.argv[4]


backup_sql = backup_sql.format(table_name=table_name,date_key=date_key,start_date=start_date, end_date=end_date)
delete_sql=delete_sql.format(start_date=start_date, end_date=end_date)
connection = pymysql.connect(host=server_db_info["ip"],
                             user=server_db_info["username"],
                             password=server_db_info["passwd"],
                             db=server_db_info["db"],
                             charset="utf8")
# print(backup_sql)
with connection.cursor() as cursor:
    cursor.execute(backup_sql)
    cursor.execute(delete_sql)
    connection.commit()
    print("backup table %s successed" %(table_name))

    cursor.execute(delete_audit_log)
    connection.commit()
    print("empty table t_audit_log successed")
# except:
#     connection.rollback()

connection.close()
