# Art Grichine
# ArtGrichine@gmail.com

import ephem
from twitter import *
import sys
import sqlite3
import time

def moon_phase(percent_illuminated):
    percent_illuminated *= 100
    if percent_illuminated >= 99:
        return 'Full Moon'
def local_time(timezone, gmt_time):
    time_zones = {'America/Chicago': -6,
                  'US/Mountain': -7,
                  'US/Arizona': -7,
                  'America/New_York': -5,
                  'US/Eastern': -5,
                  'US/Central': -6,
                  'America/Indianapolis': -5,
                  'Pacific/Samoa': -11,
                  'US/Pacific': -8,
                  'America/Denver': -7,
                  'America/Puerto_Rico': -4,
                  'America/Los_Angeles': -8,
                  'Pacific/Guam': 10,
                  'America/Adak': -10,
                  'America/Virgin': -4,
                  'Pacific/Saipan': 10,
                  'US/Alaska': -9,
                  'US/Hawaii': -10, 
                 }
                 
    time = str(gmt_time)
    local_hour = int(time[-8:-6]) + int(time_zones['{}'.format(timezone)])
    if local_hour < 0:
        local_hour += 24
    # local_time = time[:-8] + str(local_hour) + time[-6:]  #Date is included before time
    local_time = str(local_hour) + time[-6:]
    return str(local_time)

def main():

    twitter = Twitter(auth=OAuth(
                    '863439710-u1hYZ3s6NxpAgl8DXyM4sdModp9mKYL1W75IBGQz',     #Access Token
                    'UEggOxNswZXnQCVnODMUMzKSbkLlpZ9f8jhgIbzkv5yxh',          #Access Token Secret
                    'PF3WlkPo7Pygaohk1BMZKTt5D',                              #API Key
                    'aEjd8gtlvPEu31it9MHF0rOPIrWKENiUzQeJ27qQNl2BJFyrHI'))    #API Secret
    
    city   = sys.argv[1] 
    region = "US/" + sys.argv[2]                                       
    db = sqlite3.connect('us_only.sq3')
    c = db.cursor()
    
    c.execute('select latitude, longitude, time_zone from sol_places where name = "{}" and region = "{}";'.format(city, region))

    for i in c:
        latitude   = i[0]
        longitude  = i[1]
        time_zone  = i[2]
        print('Latitude: {}'.format(i[0]))
        print('Longitude: {}'.format(i[1]))
    
    #Sunrise/Set
    ob = ephem.Observer()
    ob.lat = str(latitude)
    ob.lon = str(longitude)
    ob.horizon = '-6'        #civil dusk/dawn is -6 degrees
    m = ephem.Sun()
    m.compute(ob)
    print(ob.next_rising(m))
    
   # twitter.statuses.update(status = 'In the city of {} the civil sunrise will be at {} and the civil sunset will be at {} today.'.format(
   #                                                                                      city,
   #                                                                                      local_time(time_zone, (ob.next_rising(m))), 
   #                                                                                      local_time(time_zone, (ob.next_setting(m)))))
    print('Sun will rise: ' + local_time(time_zone, (ob.next_rising(m))))    
    print('Sun will set: '  + local_time(time_zone, (ob.next_setting(m))))
    
    #Phases of the moon
    moon = ephem.Moon()
    moon.compute(ob)
    stage_of_moon = moon_phase(moon.moon_phase)
    
if __name__ == '__main__':
    main()