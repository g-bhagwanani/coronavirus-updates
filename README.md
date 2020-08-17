<div align="center">

# coronavirus-updates
This is a project that will send regular updates to the subscribers about coronavirus statistics in their country.

![Home Page](https://user-images.githubusercontent.com/46627073/78516325-bf098400-77d6-11ea-8e71-da15344630e0.png)

</div>

------------------------------------------

### Features

- A web app where visitors can subscribe for regular updates and/or check the current stats.
![Stats on web page](https://user-images.githubusercontent.com/46627073/78516726-3986d380-77d8-11ea-9bb3-b0d0cc1b96ec.png)
- Subscribers will recieve emails daily about the stats in their country. 
- The information is gathered and updated in real time from [Worldometers](https://www.worldometers.info/coronavirus/) which collects this data from reliable sources such as Governments' communication channels.

------------------------------------------

### Technologies used

- **Frontend:** HTML, CSS, JS, React
- **Backend:** Python (Flask framework)
- **Database:** AWS RDS (MySQL)
- **Hosting:** AWS EC2 instance

------------------------------------------

## To run locally
### Installation

```
git clone https://github.com/g-bhagwanani/coronavirus-updates.git
virtualenv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd frontend
npm install
```

### Local Settings

You will need to create a MySQL database (We have used MySQL Commmunity Engine of Amazon RDS which comes under AWS free tier).
Open the file ```local_settings.py``` in the root directory of the project.
Theese are the variables that need to be set in order to store data of subscribers, and send them email updates.

### Start the python server

In the root directory,
```
source myvenv/bin/activate
python run.py
```

### Start the react server

You need node and npm installed on your machine in order to run the react server.

In the root directory,
```
cd frontend
npm start
```

### Update the CSV files

The following commands are used to populate the CSV files that supply data to the frontend

In the root directory,
```
source myvenv/bin/activate
python refresh_csv.py
python daily_stats.py
```
It is expected to setup cron jobs for these commands. ```daily_stats.py``` is used to store the history of stats of each country. So, this file should be run once a day. ```refresh_csv.py``` is used to store the current stats of each country, so this file should be run at small intervals so that the stats remain up-to-date.

### Send updates

The following command is used to send emails to subscribers about the stats in their country.

In the root directory,
```
source myvenv/bin/activate
python send_mail.py
```
A cron job can be set to run this command at the same time every day to send stats to the users.
