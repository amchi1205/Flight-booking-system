from flask import Flask, render_template, json
import os
import Database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()
# Routes


@app.route('/')
def root():
    return render_template("main.j2")


@app.route('/seat-admin')
def seat_admin():
    query = "SELECT `Seat_ID`, TC.`Travel_Class_Name` AS Class, `Flight_ID` AS Flight, `Seat_Number`, `Available`, `Passenger_Name` FROM seats INNER JOIN travel_classes AS TC ON seats.`Travel_Class_ID`=`TC`.`Travel_Class_ID` WHERE Flight_ID = 1;"  # Replace with true query later
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("seat_admin.j2", data=results)


@app.route('/flight-admin')
def flight_admin():
    query = "SELECT `Flight_ID` AS FlightNumber, `Departure_Date_Time` AS Departure, `Arrival_Date_Time` AS Arrival, OA.`Airport_Name` AS Origin, DA.`Airport_Name` AS Destination, airplane.`Airplane_Type` AS Airplane FROM Flights INNER JOIN airports AS OA ON `Flights`.`Origin_Airport_ID` = OA.`Airport_ID` INNER JOIN airports AS DA ON `Flights`.`Destination_Airport_ID` = DA.`Airport_ID` INNER JOIN airplane_types AS airplane ON `Flights`.`Airplane_Type_ID` = airplane.`Airplane_Type_ID`"  # Replace with true query later
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("flight_admin.j2", data=results)


@app.route('/airplane-admin')
def airplane_admin():
    query = "SELECT * FROM Airplane_Types;"  # Replace with true query later
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("airplane_admin.j2", data=results)


@app.route('/airport-admin')
def airport_admin():
    query = "SELECT * FROM Airports;"  # Replace with true query later
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("airport_admin.j2", data=results)


@app.route('/travelclass-admin')
def travelclass_admin():
    query = "SELECT * FROM Travel_Classes;"  # Replace with true query later
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("travelclass_admin.j2", data=results)


@app.route('/airplanetravelclass-admin')
def airplanetravelclass_admin():
    query = "SELECT ACT.`Airplane_Travel_Classes_ID`, APT.`Airplane_Type` AS Airplane, TC.`Travel_Class_Name` AS Class, ACT.`Travel_Class_Capacity` AS Capacity FROM airplane_travel_classes AS ACT INNER JOIN airplane_types AS APT ON ACT.`Airplane_Type_ID` = APT.`Airplane_Type_ID` INNER JOIN travel_classes AS TC ON ACT.`Travel_Class_ID` = TC.`Travel_Class_ID`;"  # Replace with true query later
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("airplanetravelclass_admin.j2", data=results)

# Listener


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))
    app.run(port=port, debug=True)
