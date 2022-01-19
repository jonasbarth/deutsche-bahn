# deutsche-bahn

# station data
https://data.deutschebahn.com/dataset/data-haltestellen.html

# API data
https://developer.deutschebahn.com/store/apis/info?name=Timetables&version=v1&provider=DBOpenData

# History delay
Look at historyDelay in the API description.

How to get history delay of a stop?
1. Find a stop
2. each stop has events so find events for that stop
3. within the events, find the historic change of that stop
4. the historic change to find the historic delay