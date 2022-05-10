import keys
import tweepy
import xlsxwriter

#prompts the user
fname = input("What would you like to name the excel file?")
tweetamount = input("How many tweets would you like to scrape?")

#creates the workbook and worksheet
dataWorkbook = xlsxwriter.Workbook( fname +".xlsx")
datasheet = dataWorkbook.add_worksheet()

#arrays for the respective fields
caption = []
tweetid = []
username = []

#creates the headings for the data sheet
datasheet.write("A1", "Caption")
datasheet.write("B1", "Tweet ID")
datasheet.write("C1", "Username")

#initializes the API key
client = tweepy.Client(bearer_token=keys.BearerToken)

#assigns keywords for filtering
keywords = '(tornado  -is:retweet)'

#creates the parameters for the responses
responses = client.search_recent_tweets(query=keywords,max_results=30, tweet_fields=['created_at','text'], expansions=["author_id"])

users = {u['id']: u for u in responses.includes['users']}
i = 1
c = 0
#for loop to cycle through all the data
for tweet in responses.data:

    if users[tweet.author_id]:
        user = users[tweet.author_id]

        #append the fields to their respective arrays
        caption.append(tweet.text)
        tweetid.append(tweet.id)
        username.append(user.username)

        #write the data to the datasheet
        datasheet.write(i,0,caption[c])
        datasheet.write(i,1,tweetid[c])
        datasheet.write(i,2,username[c])
        i+=1
        c+=1

#close the xlsx file
print("The excel file has been created.")
dataWorkbook.close()

