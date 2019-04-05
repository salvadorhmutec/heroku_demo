import web

db_host = 'jlg7sfncbhyvga14.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'usl1622abz6pzo3j'
db_user = 'lfg1hswvttdddaeo'
db_pw = 'wiqe510m36qhn2fx'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )