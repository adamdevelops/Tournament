# Tournament
Project 2 for the Udacity Full Stack Nanodegree

Project Specification:

Develop a database schema to store details of a games matches between players.
Then write a Python module to rank the players and pair them up in matches in a tournament.

Files:

tournament.py

Contains the implementation for the Swiss tournament

tournament.sql

Contains the SQL queries to create the database, tables and views

tournament_test.py

Contains the test cases for tournament.py

Prerequisites

The latest vagrant build for the Udacity tournament project. (In project notes)

<u>Instructions:</u>

Start Vagrant
Open Terminal or cmd and browse to the vagrant folder
Type 'vagrant up' to start up vagrant VM
SSH in to the vagrant VM using 'vagrant ssh'
Change to the tournament folder located in the vagrant folder.
Type cd /vagrant/tournament
Open PSQL and run the tournament.sql
type psql
copy the contents of tournament.sql and paste in to the terminal window
type \q to quit out of PSQL
Run the tests within the tournament_test.py file

Final results in the cmd prompt:

vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py

1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.

Success! All tests pass!

References:

http://www.w3schools.com/sql/

https://docs.python.org/2/library/array.html

https://docs.python.org/2/library/random.html

https://www.google.com/search?q=random.sample+python&sourceid=ie7&rls=com.microsoft:en-US:IE-Address&ie=&oe=&gws_rd=ssl

https://discussions.udacity.com/t/how-to-pass-the-argument-to-the-sql-statement-in-pyscopg2/193999

http://initd.org/psycopg/docs/usage.html

http://stackoverflow.com/questions/14793057/how-to-include-zero-0-results-in-count-aggregate
