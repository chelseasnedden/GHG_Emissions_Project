from flask import Flask, render_template
import pymongo
app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.Carbon_Dioxide_Emissions

GHGemissions = db.GHG_Emissions

Countries = db.Location_for_Countries

@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    GHGinfo = list(GHGemissions.find())
    print(GHGinfo)


    Countriesinfo = list(Countries.find())
    print(Countriesinfo)
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", GHGinfo=GHGinfo,Countriesinfo=Countriesinfo)

@app.route("/Page_1")
def Page1():
    # write a statement that finds all the items in the db and sets it to a variable
    GHGinfo = list(GHGemissions.find())
    print(GHGinfo)

    Countriesinfo = list(Countries.find())
    print(Countriesinfo)
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("Page_1.html", GHGemissions=GHGemissions,Countries=Countries)

@app.route("/Page_2")
def Page2():
    # write a statement that finds all the items in the db and sets it to a variable
    GHGinfo = list(GHGemissions.find())
    print(GHGinfo)

    Countriesinfo = list(Countries.find())
    print(Countriesinfo)
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("Page_2.html", GHGemissions=GHGemissions,Countries=Countries)

  
@app.route("/Page_3")
def Page3():
    # write a statement that finds all the items in the db and sets it to a variable
    GHGinfo = list(GHGemissions.find())
    print(GHGinfo)

    Countriesinfo = list(Countries.find())
    print(Countriesinfo)
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("Page_3.html", GHGemissions=GHGemissions,Countries=Countries)



if __name__ == "__main__":
    app.run(debug=True)