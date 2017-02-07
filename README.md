#Wrong Turn

This was a project aimed at data analysis and visualization of accidents near Leeds(UK).
## Below is the procedure we followed to create the API Server
1. We took the data from https://data.gov.uk/dataset/road-traffic-accidents which had all
accident parameters including grid referencing.

2. Then we merged the csv files using mergeData.py ( Take care of changed column names from 2013).

3. Then we renamed the columns for ease of use using cleanData.py

4. We used the output from step 3.(DriverCauses.py) to train a neuralNetwork for accident causes
using conditionsCheck.py.

5. Next in the server folder we put the neuralNetModel.pickle and Data.csv files.

6. Then we wrote a flask server to judge location risks via radial queries and conditional risk via neural networks.

7. We even generated a latitude longitude file(lat_lon.csv) using pandas( df.apply command) and bng_to_latlon.

## Steps to run:
-- Start server by: python flaskServer.py

-- Sample request: localhost/getConditionRisk/?time=2345&sex=1&surface=2&veh=1&lat=53.8077491&lon=-1.5228207&age=37

(You may have to edit the port in flaskServer.py and the sample request.)

## Mapbox Usage
To generate a map using mapbox studio you need a file that has columns named 'Latitude' and 'Longitude'
(without qoutes) as in lat_lon.csv.

Check out our map at: https://api.mapbox.com/styles/v1/abhay447/ciyrpedec005y2rmmkd31qu9c.html?title=true&access_token=pk.eyJ1IjoiYWJoYXk0NDciLCJhIjoiY2l5bjFsNnhlMDAwNjMzcGNibWN3YW93aCJ9.kQtALmz_o5TQIoQeBdTlzw#0.0/0.000000/0.000000/0

Be Sure to zoom in at Leeds(uk)

![Image of Map](https://api.mapbox.com/styles/v1/abhay447/ciyrpedec005y2rmmkd31qu9c/static/-1.531494,53.794123,11.38,0.00,0.00/600x400?access_token=pk.eyJ1IjoiYWJoYXk0NDciLCJhIjoiY2l5bjFsNnhlMDAwNjMzcGNibWN3YW93aCJ9.kQtALmz_o5TQIoQeBdTlzw)
