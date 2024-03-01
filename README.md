Advanced Calculator
===================

A web-based calculator application that allows users to perform calculations and view their calculation history. The application is built using Flask, SQLite, and Docker.

Features
--------

* Perform calculations
* View calculation history
* Export history to CSV file

Requirements
------------

* Docker

Getting Started
---------------

1. Clone the repository:
```bash
git clone https://github.com/abshka/Advanced-calculator.git
```
2. Build the Docker image:
```
docker build -t advanced-calculator:latest .
```
3. Run the Docker container:
```css
docker run -p 4000:5000 advanced-calculator:latest
```
4. Open your web browser and navigate to <http://localhost:4000>.

Usage
-----

* Enter a calculation in the input field and click the "Calculate" button to perform the calculation.
* View your calculation history by clicking the "History" button.
* Export your calculation history to a CSV file by clicking the "Export to CSV" button.

File Structure
-------------

* `app.py` - the main application file
* `Dockerfile` - the Docker configuration file
* `requirements.txt` - the list of required Python packages
* `schema.sql` - the SQL schema for the database
* `history.db` - the database
* `Templates/` - directory containing the HTML templates for the application

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
-------

[MIT](https://choosealicense.com/licenses/mit/)
