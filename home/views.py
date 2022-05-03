from django.shortcuts import render,redirect,HttpResponse
import mysql.connector as sql

firstName=""
lastName=""
email=""
role=""
passsword=""


# Create your views here.
def loginpage(request):
    return redirect("/login")

def loginUser(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('userType')
        print(email,password,user_type)
        sqlObj = sql.connect(host="localhost",user="root",password="",database="resumeScreening")
        cursor = sqlObj.cursor()                        
        selectCommand = "select * from users where email='{}' and password='{}' and role='{}' ".format(email,password,user_type)
        print(selectCommand)
        cursor.execute(selectCommand)
        usersData = tuple(cursor.fetchall())
        print(usersData)
        if(usersData == ()):
            return render(request,'login.html')
        else:
            return HttpResponse("Welcome {}  ".format(usersData[0][0]))
    return render(request, 'login.html')

def signup(request):
    global firstName,lastName,role,email,passsword
    if request.method=="POST":
        sqlObj = sql.connect(host="localhost",user="root",password="",database="resumeScreening")
        cursor = sqlObj.cursor()
        signupData = request.POST
        for key,value in signupData.items():
            if(key=="firstName"):
                firstName=value
            elif(key=="lastName"):
                lastName=value
            elif(key=="email"):
                email=value
            elif(key=="role"):
                role=value
            else:
                passsword=value
                                
        insertCommand = "insert into users Values('{}','{}','{}','{}','{}')".format(firstName,lastName,email,role,passsword)
        
        cursor.execute(insertCommand)
        sqlObj.commit()
    return render(request,'signup.html')
    