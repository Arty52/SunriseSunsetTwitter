Author:         Art Grichine
Email:          ArtGrichine@gmail.com
Assignment:     08
Date:           23 April 2014

Twitter account: @ArtGrichine

What does this program do?
This program will give the user civil dusk/dawn and moon phase from an input of city and state.
This program sleeps until 3am and then tweets. Once tweet is produced it sleeps for 24 hours and
then repeats.

Note:
    1. 'astrotweet.py' code for tweeting on twitter of account @ArtGrichine
    2. requirements.txt file is result of pip freeze on mysite in virtualenv. This
        file contains 

Use:
To use this program type: python astrotweet.py "city of choice" States-initials
                 Example: python astrotweet.py "Fullerton" ca
                 Output:  In the city of Fullerton the sunrise will be at 4:42:02 and the sunset 
                          will be at 18:57:15 today. The moon phase today is waning crescent.
                 
tweets/output will be posted on www.twitter.com on account @ArtGrichine