import os
import psycopg2
# Import modules for CGI handling 
import cgi, cgitb ## I had to modify httpd.conf and add content showed in https://httpd.apache.org/docs/2.4/howto/cgi.html to run CGI in here.

#PostgressSQL 
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='verify-ca')  ## if running locally, no ssl is needed so change 'required' to nothing or something else
cur = conn.cursor()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 


# Get data from fields
ID = form.getvalue('id')
first_name = form.getvalue('fname')
last_name  = form.getvalue('lname')
email = form.getvalue('email')
age = form.getvalue('age')
location = form.getvalue('location')

#sql query
sql = '''INSERT INTO users(id, firstname, lastname, email, age, location)
VALUES (''' + ID + ', ' + first_name + ', ' + last_name + ', ' + email + ', ' + age + ', ' + location + ')'

cur.execute(sql)

# get the generated id back
vendor_id = cur.fetchone()[0]

conn.commit()
conn.close()