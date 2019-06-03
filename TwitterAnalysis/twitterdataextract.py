import tweepy
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import timedelta

scope = ['https://spreadsheets.google.com/feeds',#google spread shit
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('google_sec.json',scope)
client = gspread.authorize(creds)
sheet = client.open('TwitterStockSheets').sheet1


auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)

row = 2

for status in tweepy.Cursor(api.search, #only can get one week period of time, but can set dates
                           q="Queensland floods", #Edit: Answer (added lines after q=) since='2015-03-16', until='2015-03-17',
                           count=10,
                           result_type='recent',
                           include_entities=True,
                           monitor_rate_limit=True,
                           wait_on_rate_limit=True,
                           lang="en").items():

    eastern_time = status.created_at - timedelta(hours=4)
    edt_time = eastern_time.strftime('%Y-%m-%d %H:%M')
    col = 1

    print ("Time: ",edt_time)
    print ("--- ")
    print ("Follower Count: ",status.user.followers_count)
    print ("Location: ",status.user.location)
    print ("--- ")
    print (status.text)

        
    sheet.update_cell(row,col,status.text)
    col = col + 1
    sheet.update_cell(row, col, status.user.location)
    col = col + 1
    sheet.update_cell(row, col, status.user.followers_count)
    col = col + 1
    sheet.update_cell(row, col, edt_time)

    row = row + 1

