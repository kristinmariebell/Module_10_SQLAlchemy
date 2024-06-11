# 1. import Flask
from flask import Flask, jsonify
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func, desc
from sqlalchemy.orm import sessionmaker
import numpy as np
import pandas as pd
import datetime as dt
from datetime import timedelta









#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
database_path = '../Resources/hawaii.sqlite'
engine = create_engine(f"sqlite:///{database_path}")

# reflect the tables
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(bind = engine)

#################################################
# Flask Setup
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)
#################################################




#################################################
# Flask Routes
@app.route("/")
def home():
    return """
    <h1>Welcome to my Climate App page!</h1>
   <a href="/api/v1.0/precipitation">precipitation</a> 
   <br/>
    <a href="/api/v1.0/2017-08-23">start_date</a> 
    """

@app.route("/api/v1.0/precipitation")
def precipitation():
    #my code here
    clean_data = {}
    session.close()
    return jsonify(clean_data)

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

@app.route("/api/v1.0/<start>")
def starts(start):
    print("Server received request for 'About' page...")
    return start

# @app.route("/api/v1.0/<start>/<end>")
# def start_end():
#     print("Server received request for 'About' page...")
#     return "Welcome to my 'About' page!"
#################################################
if __name__ == "__main__":
    app.run(debug=True)