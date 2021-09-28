import mysql.connector

word = input("Enter a word in English and press Enter: ")

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pmldatabase"
)


cursor = con.cursor()

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word )
results = cursor.fetchall()

if results:
    for rt in results:
        print(rt[1])
else:
    print("We couldn't find any results about that.")