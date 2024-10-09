# Flight-booking-system
A web-based application for booking and managing flight reservations. Built with Python and Flask, this project allows users to search for flights, manage bookings, and securely authenticate.

# Executive Summary
The project underwent significant simplification by removing the Passengers, Reservations, and
Invoices entities, streamlining the system to allow only one seat purchase at a time from the
database's perspective. Relationships between Seats and Flights, as well as Seats and Travel
Classes, were revised to ensure they are non-optional, preventing the addition of a seat without
its corresponding flight and travel class. T o maintain consistency across the database, the
naming syntax for Airports was updated, and specific numbers were added to the overview to
more accurately quantify the system's potential application. Some feedback, such as the
suggestion to include all four relationship types, was deemed unnecessary since there are only
three types (1:1, 1, M). Additionally, the recommendation to add a Flight ID to the
airplane
travel
_
_
classes table was not followed due to the assumption that specific airplane
types would have consistent capacities.
Further simplifications were made, reinforcing the relationships within the database to ensure
alignment with the ERD. The schema was realigned visually to better represent these
relationships, and adjustments were made to the DDL to align with insert statements and
ticketing notes. The database's naming conventions for Airports were revised to maintain
consistent attribute naming throughout. Feedback suggesting additional filters in the UI was
acknowledged, though the existing filters were maintained for simplicity. Some design decisions
were upheld, such as using TINYINT instead of BOOLEAN due to MySQL's automatic
conversion and performance considerations.
T o meet rubric requirements and facilitate database creation on OSU servers, schema creation
statements were removed from the DDL, and the schema was realigned to better reflect
relationships. The airplane
travel
_
_
classes table was updated with an INSERT statement to
ensure the addition of 0 capacity entries for each travel class when a new airplane is added.
The Seats data was updated to match the DDL, and the seats constraint was removed to be
handled in the backend. An INSERT and DELETE UI was added for seats, though this
introduced risks by allowing the creation of seats outside the standard configuration, placing a
burden on administrators. DELETE statements were implemented across all tables, with the
Flights and Seats tables converted to ON DELETE CASCADE to ensure that when an airport is
deleted, all associated flights and seats are also deleted. A flight select statement was added for
use in the Seats flight filter.
Certain feedback was not implemented based on the system's design assumptions. For
instance, the recommendation to add a Flight ID to the airplane
travel
classes table was not
_
_
followed due to the assumption that airplane types would maintain consistent capacities.
Additionally, feedback regarding transitive dependency in the Airports table was disagreed with,
as the database lacks the necessary information to make such inferences. Overall, the project
maintained its design approach, balancing feedback with the practical constraints and
assumptions of the system.

Project Outline
Overview:
The main object of this project is to provide consumers with a straightforward way to look and
book their flights. Users are able to look up seat tickets, receive information on ticket prices, and
browse flight options available at various times on a given date using this database. It stores all
the available flights and seats that are needed to plan a trip and will store, organize, and
manage a database of multiple flights. The system is scalable to support regional airlines
running 400 flights with 8000 seats at a time.
Database Outline
● Airports: records the location details of potentially serviced airports
○ Airport
ID: PK, INT , not null, AI
_
○ Airport
_
Name: VARCHAR(100), not null
○ Airport
_
City: VARCHAR(100), not null
○ Airport
_
Country: VARCHAR(100), not null
■ Airport Relationships:
● A 1:M (Optional) between Airports and Flights is implemented,
with Origin
_
Airport
_
ID as a FK in Flights.
● A 1:M (Optional) between Airports and Flights is implemented,
with Destination
_
Airport
_
ID as a FK in Flights.
● Flights: records the departure and arrival information for a specific flight
○ Flight
ID: PK, INT , not null, AI
_
○ Origin
_
Airport
ID: INT , FK
_
○ Destination
_
Airport
ID: INT , FK
_
○ Departure
Date
Time: DateTime, not null
_
_
○ Arrival
Date
Time: DateTime, not null
_
_
○ Airplane
_
Type
ID: INT , FK
_
■ Flights Relationships:
● A M (Optional):1 between Flights and Airports is implemented with
Origin
_
Airport
_
ID as a FK in Flight
Details.
_
● A M (Optional):1 between Flights and Airports is implemented,
with Destination
_
Airport as a FK in Flight
Details.
_
● A M (Optional):1 between Flights and Airplane
_
Types is
implemented with Airplane
_
Type
_
ID as a FK in Flights.
● A 1:M (Optional) between Flights and Seats is implemented with
Flight
ID as a FK in Seats.
_
● Seats: records the specific seat reserved for a reservation. A constraint is placed to limit
the number of seats of a specific class on a specific flight to the number available on the
flight’s plane type
○ Seat
ID: PK, INT , not null, AI
_
○ Seat
_
Number: VARCHAR(100), not null
○ Travel
Class
ID: INT , FK
_
_
○ Flight
ID: INT , FK
_
○ Available: TINYINT , not null
○ Passenger
_
Name: VARCHAR(100)
■ Seats Relationships:
● A M (Optional):1 (Optional) between Seats and Travel
Classes is
_
implemented with Travel
Class
ID as a FK in Seats._
_
● A 1:M (Optional) between Flights and Seats is implemented with
Flight
_
ID as a FK in Seats.
● Travel
Classes: differentiates seats based on comfort and cost
_
○ Travel
Class
ID: PK, INT , not null, AI
_
_
○ Travel
Class
_
_
Name: VARCHAR(100), not null
○ Travel
Class
_
_
Cost: Decimal(20,2), not null
■ Travel
_
Class Relationships:
● A 1 (Optional) :M (Optional) between Travel
Classes and Seats is
_
implemented with Travel
Class
ID as a FK in Seats.
_
_
● A M:M between Travel
_
Classes and Airplane
_
Types is
implemented with Airplane
Travel
Classes as a Junction T able
_
_
○ A 1:M (Optional) between Travel
Classes and
_
Airplane
Travel
_
_
Classes is implemented with
Travel
Classes
_
_
ID as a FK in Airplane
Travel
Classes.
_
_
● Airplane
_
Types: records the types of airplanes in the fleet
○ Airplane
_
Type
ID: PK, INT , not null, AI
_
○ Aiplane
_
Type: VARCHAR(100), not null
■ Airplane
_
Types Relationships:
● A 1:M (Optional) between Airplane
_
Types and Flights is
implemented with Airplane
_
Type
_
ID as a FK in Flights.
● A M:M between Travel
_
Class and Airplane
_
Types is implemented
with Airplane
Travel
Classes as a Junction T able
_
_
○ A 1:M (Optional) between Airplane
_
Types and
Airplane
Travel
_
_
Classes is implemented with
Airplane
_
Type
_
ID as a FK in Airplane
Travel
Classes.
_
_
● Airplane
Travel
_
_
Classes: used to link the number of each seat class are present on
each plane type
○ Airplane
Travel
Classes
ID: PK, INT , not null, AI
_
_
_
○ Airplane
_
Type
ID: INT , FK
_
○ Travel
Class
ID: INT , FK
_
_
○ Travel
Class
_
_
Capacity: BIGINT
■ Airplane
Travel
_
_
Classes Relationships:
● A M (Optional):1 between Airplane
Travel
_
_
Travel
_
Classes is implemented with Travel
Classes and
Class
ID as a FK in
_
_
Airplane
Travel
Classes.
_
_
● A M (Optional):1 between Airplane
Travel
_
_
Airplane
_
Types is implemented with Airplane
Classes and
Types
ID as a FK in
_
_
Airplane
_
Types.
