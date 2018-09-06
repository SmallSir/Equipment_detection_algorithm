def get_train():
    import pandas as pd
    import pymssql
    conn = pymssql.connect(host='192.168.1.201', user='sa', password='123.com', database='GB_NEW')
    SQL = "select * from [dbo].[GB_APPOINTMENT]"
    df = pd.read_sql(SQL, con=conn)
    return df