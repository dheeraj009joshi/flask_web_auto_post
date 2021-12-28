from flask import Blueprint, render_template,request,redirect

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home", methods =["GET", "POST"])
def home():
    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            print(image)

            return redirect(request.url)

   #  if request.method == "POST":
   #    #  first_name = request.form.get("username")
   #    #  last_name = request.form.get("password")
   #    #  print(first_name)
   #     if request.files: 
   #       print('file')
   #       file=request.files("myfile") 
   #       print(file)
      #  return "Your name is "+first_name + last_name
    return render_template("home.html")