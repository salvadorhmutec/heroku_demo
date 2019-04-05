import web

db_host = 'localhost'
db_name = 'heroku_demo'
db_user = 'heroku'
db_pw = 'heroku.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )