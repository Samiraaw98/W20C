import dbcreds
import mariadb


name= input('please enter  username:')
content = input('write content here:')

conn= mariadb.connect(
                    user=dbcreds.user, 
                    password=dbcreds.password, host=dbcreds.host, 
                    port=dbcreds.port, database=dbcreds.database
)
cursor=conn.cursor()
cursor.execute("INSERT INTO blog_post(username, content) VALUES(? ,?)", [name,content])

conn.commit()
run_query=cursor.execute("SELECT content FROM blog_post"),
print(run_query)




# conn.commit()
cursor.close()
conn.close()

# run_query=cursor.execute("SELECT content FRO
# M blog_post"),
# print(run_query)









