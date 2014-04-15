import ephem
import twitter
import sys
import sqlite3

def main():
    city =  sys.argv[1]                     
 #    state = sys.argv[2]                      
    db = sqlite3.connect('us_only.sq3')
    c = db.cursor()
    
    # sun = ephem.Sun()
#     p = ephem.Sun('2014/4/5')
#     x = ephem.Sun('2000/4/5')
#     print(p.size)
#     print(x.size)
#     print(sun.name)
# select latitude from sol_places where name = "Los Angeles";
    c.execute('select latitude from sol_places where name = "{}";'.format(city))
    # nyc = ephem.city('New York')
    # print(nyc.lat)
    for i in c:
        print('latitude: {}'.format(i))
    
if __name__ == '__main__':
    main()