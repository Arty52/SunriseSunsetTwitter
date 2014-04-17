# Art Grichine
# ArtGrichine@gmail.com

import ephem
from twitter import *
import sys
import sqlite3

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
        local_hour = local_hour + 24
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
    
    ob = ephem.Observer()
    ob.lat = str(latitude)
    ob.lon = str(longitude)
    m = ephem.Sun()
    m.compute(ob)
    print(ob.next_rising(m))
    
    twitter.statuses.update(status = 'The sun will rise at {} and set at {} today.'.format(
                                                                                        local_time(time_zone, (ob.next_rising(m))), 
                                                                                        local_time(time_zone, (ob.next_setting(m)))))
    print('Sun will rise: ' + local_time(time_zone, (ob.next_rising(m))))    
    print('Sun will set: '  + local_time(time_zone, (ob.next_setting(m))))
    
if __name__ == '__main__':
    main()