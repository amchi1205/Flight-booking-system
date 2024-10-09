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
