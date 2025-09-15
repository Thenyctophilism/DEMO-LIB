import json
import uuid
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib import messages
from django.urls import reverse
from datetime import datetime , timedelta

# def login(request):
#     return render(request, 'panels/login.html')

# def check_login(request):
#    if request.POST: 
#      username = request.POST.get('username')
#      password = request.POST.get('password')
#    with open('users.json' , 'r') as infile:
#       userdata = json.load(infile)
#    for item in userdata:
#       if item['username'] == username and item['password'] == password :
#         messages.success(request, "Login successfully!")
#         return redirect(reverse('userpanel', args=[username]))


#       else:
#         messages.error(request, "Invalid username or password")
#         return redirect("login")




def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        with open('users.json', 'r') as infile:
            userdata = json.load(infile)

        for item in userdata:
            if item['username'] == username and item['password'] == password:
                id = item["id"]
                messages.success(request, "Login successfully!")
                return redirect(reverse('userpanel', args=[id]))

        
        messages.error(request, "Invalid username or password")
        return redirect("login")
 
    return render(request, 'panels/login.html')


def adminlogin(request):
 if request.method == "POST":
        adminname = request.POST.get('adminname')
        adminpassword = request.POST.get('adminpassword')

        with open('admin.json', 'r') as infile:
            admindata = json.load(infile)

        for item in admindata:
            if item['username'] == adminname and item['password'] == adminpassword:
                messages.success(request, "Login successfully!")
                return redirect('adminpanel')

        
        messages.error(request, "Invalid username or password")
        return redirect("login") 
 
 return render(request, 'panels/adminlogin.html')


def adminpanel(request):
   return render(request, 'panels/adminpanel.html')


def adminbookshelf(request):
    with open("bookinf.json" , "r") as infile:
     data = json.load(infile)
    genre_list = set()
    for item in data:   
       genre_list.add(item['genre']) 
    genre_list = list(genre_list)          
    return render(request ,'panels/adminbookshelf.html', {"data":data , "genre" : genre_list})


def bookchange(request,bookid):
   with open("bookinf.json" , "r") as infile:
     data1 = json.load(infile)
   if request.method == "POST":
      author = request.POST.get("author", "").strip()
      year = request.POST.get("year", "").strip()
      genre = request.POST.get("genre", "").strip()
      summary = request.POST.get("summary", "").strip()

      for item in data1:
       if item["id"] == int(bookid):
         if author :
             item["author"] = author
         if year : 
             item["year"] = year
         if genre :
               item["genre"] = genre
         if summary :
               item["summary"] = summary      
      with open("bookinf.json" , "w") as outfile:
           json.dump(data1 , outfile)   
      
      for item in data1:
         if item["id"] == int(bookid):
          return render(request , 'panels/bookchange.html' , {"data":item})

   
   for item in data1:
         if item["id"] == int(bookid):
          return render(request , 'panels/bookchange.html' , {"data":item})   


def adminusermanagement(request):
    with open("users.json" , "r") as infile:
     data = json.load(infile)         
    return render(request ,'panels/adminusermanagement.html', {"data":data})


def adminuserchanger(request,userid):
   with open("users.json" , "r") as infile:
     data2 = json.load(infile)
   if request.method == "POST":
      username = request.POST.get("username", "").strip()
      password = request.POST.get("password", "").strip()
      email = request.POST.get("email", "").strip()
      full_name = request.POST.get("fullname", "").strip()
      borrow_requests = request.POST.get("borrow_requests", "").strip()
      borrowed_books = request.POST.get("borrowed_books", "").strip()

      for item in data2:
       if item["id"] == int(userid):
         if username :
             item["username"] = username
         if password : 
             item["password"] = password
         if email :
               item["email"] = email
         if full_name :
               item["full_name"] = full_name
         if borrow_requests :
               item["borrow_requests"] = borrow_requests
         if borrowed_books :
               item["borrowed_books"] = borrowed_books

      with open("users.json" , "w") as outfile:
           json.dump(data2 , outfile)   
      
      for item in data2:
         if item["id"] == int(userid):
          return render(request , 'panels/userchanger.html' , {"data":item})

   
   for item in data2:
         if item["id"] == int(userid):
          return render(request , 'panels/userchanger.html' , {"data":item})







def userpanel(request,userid):
 

    with open('users.json' , 'r') as infile:
        userdata = json.load(infile)

    with open('bookinf.json' , 'r') as infile:
       bookdata = json.load(infile)   

    #age khastan taghir bedan

    if request.method == "POST":
      username = request.POST.get("username2", "").strip()
      password = request.POST.get("password2", "").strip()
      email = request.POST.get("email2", "").strip()
      full_name = request.POST.get("fullname2", "").strip()
    

      for item in userdata:
       if item["id"] == int(userid):
         if username :
             item["username"] = username
         if password : 
             item["password"] = password
         if email :
               item["email"] = email
         if full_name :
               item["full_name"] = full_name
        #  if borrow_requests :
        #        item["borrow_requests"] = borrow_requests
        #  if borrowed_books :
        #        item["borrowed_books"] = borrowed_books

      with open("users.json" , "w") as outfile:
           json.dump(userdata , outfile)  

      for item in userdata:
         if item["id"] == int(userid):
          return render(request , 'panels/userpanel.html' , {"data":item})

    #namayesh ketabhaye azad

    borrowed_books = set()
    for user in userdata:
       for book in user['borrowed_books']:
        borrowed_books.add(book['title']) 
    
    freebooks = []
    for book in bookdata:
       if book['title'] not in borrowed_books:
          freebooks.append(book['title'])
         

    for item in userdata:
        if item['id'] == int(userid):
         return render(request, 'panels/userpanel.html' , {'data' : item , 'freebooks':freebooks})   
        

def borrow(request):
    if request.method == "POST":
        book_title = request.POST.get("booktitle", "").strip()
        userid = request.POST.get("userid", "").strip()
        
        with open("users.json", "r") as infile:
            users = json.load(infile)
        with open("bookinf.json", "r") as infile:
            books = json.load(infile)
        with open("inbox.json", "r") as infile:
            inbox = json.load(infile)

        for item in inbox:
           if item["user_id"] == int(userid):
              return HttpResponse("you already have a request")


        book_id = None
        for book in books:
            if book["title"] == book_title:
                book_id = book["id"]
                break
        if book_id is None:
            return HttpResponse("Book not found")

        
        user = None
        for u in users:
            if u["id"] == int(userid):
                user = u
                break
        if not user:
            return HttpResponse("User not found")

        
        if user.get("delay_flag", 0) >= 2:
            return HttpResponse("You can't borrow books (too many delays)")

        
        request_id = str(uuid.uuid4())
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        new_request = {
            "request_id": request_id,
            "book_id": book_id,
            "status": "pending",
            "request_date": today  
        }

        
        user["borrow_requests"].append(new_request)

        
        inbox_entry = {
            "request_id": request_id,
            "user_id": user["id"],
            "user_fullname" : user["full_name"],
            "book_id": book_id,
            "answered": "no"
        }
        inbox.append(inbox_entry)

        
        with open("users.json", "w") as outfile:
            json.dump(users, outfile, indent=2)
        with open("inbox.json", "w") as outfile:
            json.dump(inbox, outfile, indent=2)

        return HttpResponse("Borrow request submitted!")

    return HttpResponse("Invalid request method")


def inbox_handeling(request):
     with open("inbox.json" , "r") as infile:
         data = json.load(infile)
     with open("users.json" , "r") as infile:
         userdata = json.load(infile)    
     with open("bookinf.json" , "r") as infile:
         bookdata = json.load(infile)    
     pending = []
     if request.method == "POST":
        request_id = request.POST.get("reqid" , "").strip()
        book_id = request.POST.get("book_id", "").strip()
        user_id = request.POST.get("user_id", "").strip()
        answer = request.POST.get("action" , "").strip()

        if answer == "yes":
         temp = None
         next_week = datetime.now() + timedelta(days=7)
         for book in bookdata:
             if book["id"] == int(book_id):
              temp = {"book_id" : book["id"] , "title" : book["title"]  , "borrow_date" : datetime.now().strftime("%Y-%m-%d") , "due_date": next_week.strftime("%Y-%m-%d")}    
        
         for req in data:
             if req["request_id"] == request_id:
              req["answered"] = answer


         for user in userdata:
             if user["id"] == int(user_id) :
              for item in user["borrow_requests"]:
                 if item["request_id"] == request_id:
                     item["status"] = "approved" 
              user["borrowed_books"][0] = temp   

        elif answer == "no":
            for req in data:
             if req["request_id"] == request_id:
              req["answered"] = answer

            for user in userdata:
             if user["id"] == int(user_id) :
              for item in user["borrow_requests"]:
                 if item["request_id"] == request_id:
                     item["status"] = "rejected"   

            
           

     for item in data:
         if item["answered"] == "no":
             pending.append(item)
             return render(request , "panels/inbox_handler.html" , {"data":pending})
         else:
             return HttpResponse("You dont have any new request")    