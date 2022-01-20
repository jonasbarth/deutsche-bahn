# deutsche-bahn

# station data
https://data.deutschebahn.com/dataset/data-haltestellen.html

# API data
https://developer.deutschebahn.com/store/apis/info?name=Timetables&version=v1&provider=DBOpenData

# History delay
Look at historyDelay in the API description.

How to get history delay of a stop?
1. find a timetable 
1. Find a stop
2. each stop has events so find events for that stop
3. within the events, find the historic change of that stop
4. the historic change to find the historic delay

timetable -> stop -> events -> history change -> historic delay

It seems like the history delay data isn't available through the API. I will have to collect data myself and look for delays by checking the planned arrival and actual arrival.
Example:
<s id="2121877044531283563-2201192109-2">
        <tl f="F" t="p" o="80" c="ICE" n="840"/>
        <ar pt="2201192116" pp="14" hi="1" ppth="Berlin Ostbahnhof"/>
        <dp pt="2201192120" pp="14" ppth="Berlin-Spandau|Stendal Hbf|Wolfsburg Hbf|Hannover Hbf"/>
</s>

ar = arrival
dp = departure

pt = planned time
pp = planned platform

ct = changed time
cp = changed platform

# Medium article about getting delays 
https://techlabsdus.medium.com/analysis-of-deutsche-bahn-ag-long-distance-train-traffic-delays-b183aacad9a2

I need to get the planned timetable from /plan/{evaNo}/{date}/{hour}
and then the changes from /fchg/{evaNo} and /rchg/{evaNo}

1. load all station information (which is static) once
2. load all future changes (which is static) once and check which trains are affected
3. every 30s load the rchg, and check which trains are affected

What domain objects do I need?
* Station
* timetable
* train
* planned path
* departure
* arrival