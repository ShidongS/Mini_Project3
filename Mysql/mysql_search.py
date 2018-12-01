import mysql.connector
from mysql.connector import errorcode


cnx = mysql.connector.connect(user='username',
	                          password='password',
                              database='Mini3')
cursor = cnx.cursor(buffered=True)

while(1):
    a=input("Please select your function: 1.Show account of most pictures; 2.Show most popular tags; 3.Search\n")
    # Print all accounts of the sequence of the number of pictures they have
    if a=='1':
        name=[]
        cursor.execute("SELECT * FROM pictures")
        result=cursor.fetchall()
        for x in result:
            name.append(x[2])
        name=list(set(name))
        k=[]
        for element in name:
            cursor.execute("SELECT COUNT(*) FROM pictures WHERE account_name = '"+element+"'")
            result=cursor.fetchall()
            k.append((element,result[0][0]))
        k=sorted(k,key=lambda s:s[1], reverse=True)
        print(k)

    # Print all tags of the sequence of how many times they appear
    if a=='2':
        name=[]
        cursor.execute("SELECT * FROM link")
        result=cursor.fetchall()
        for x in result:
            name.append(x[1])
        name=list(set(name))
        k=[]
        for element in name:
            element=str(element)
            cursor.execute("SELECT COUNT(*) FROM link WHERE tag_no = '"+element+"'")
            result=cursor.fetchall()
            count=result[0][0]
            cursor.execute("SELECT * FROM tags WHERE tag_no = '"+element+"'")
            result=cursor.fetchall()
            tagname=result[0][1]
            k.append((tagname,count))
        k=sorted(k,key=lambda s:s[1], reverse=True)
        for l in k:
            print(l)
        print()

    # type in a tag and find which account(s) has it
    if a=='3':
        b=input("Please type in the tag you wang to search:")
        cursor.execute("SELECT * FROM tags WHERE tag_name = '"+b+"'")
        result=cursor.fetchall()
        if len(result)==0:
            print("Can't find this tag")
        else:
            tag_no=str(result[0][0])
            cursor.execute("SELECT * FROM link WHERE tag_no = '"+tag_no+"'")
            pic_no=[]
            for row in cursor.fetchall():
                pic_no.append(row[0])
            #print(pic_no)
            acc=[]
            for pic in pic_no:
                pic=str(pic)
                cursor.execute("SELECT * FROM pictures WHERE pic_no = '"+pic+"'")
                for row in cursor.fetchall():
                    acc.append(row[2])
            acc=list(set(acc))
            print("The following account(s) have this tag: ")
            print(acc)
        print()
        
    if a!='1' and a!='2' and a!='3':
        print("Please select the right function\n")
cursor.close()
cnx.close()
