import praw
from time import sleep
import logging
from datetime import datetime

dt = datetime.now()


timestamp = datetime.timestamp(dt)

str_date_time = dt.strftime("%Y-%m-%d_%H%M")

logging.basicConfig(filename='Log_' + str_date_time + '.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s ')

userAgent = 'GWBot'
clientId = 'pnsZpSjLJ9_2Bt-sxY5JmQ'
secret = 'amqJtcQeq2TYyNxDy_1_czvsbdlyNg'
username = 'mrtwrecksDEV'
password = 'R7%y6GTCvnr3&hnP'

reddit = praw.Reddit(
    user_agent=userAgent,
    client_id=clientId,
    client_secret=secret,
    username=username,
    password=password,
    )

subreddits = ["flipping", "thesidehustle", "sidehustle", "houston", "thrift", "pics", "thriftstorehauls", 'millenials', 'xennials', 'genz', 'thriftstorefinds', 'thriftgift', 'gamecollecting', 'frugal', 'frugal_jerk', 'thriftedfasion', 'cd_collectors', 'dvdcollection', 'thrifty', 'savingmoney', 'goodwill_finds', 'sneakers', 'whatisthisthing', 'cassetteculture', 'thriftstorefasion', 'repaintings', 'vinyl', 'goodwillbins', 'thriftpaintings', 'thriftflip', 'frugalwrist', 'verycheap', 'vintageaudio', 'gaming', 'streetwear', 'mildlyinteresting', 'funny', 'barbie', 'antiques', 'analogcommunity', 'bookhaul', 'glasscollecting', 'sewing', 'depop', 'vintagefashion', 'whatisthis', 'crochet', 'vintage', 'vintagetees', 'starwars', 'bargainbinvinyl', 'thredup', 'wtfgaragesale', 'donate', 'charitabledonations', 'charity', 'nonprofit', 'vinted', 'retail', 'flippingfinds', 'reselling', 'teenagers', 'resellprofits', 'askreddit', 'shoppingaddiction', 'antiwork', 'anticonsumption', 'frugalshopping', 'resell']

content = """Just a friendly reminder…

Goodwill is a deeply exploitative organization, top to bottom. Their entire business model is built on taking advantage of vulnerable people. They use their career centers to funnel individuals (often those with criminal records) to staff their stores, where they’re overworked, underpaid, and treated like shit. Many of these workers have limited options available to them and can’t just go get another job. They are stuck at Goodwill. Goodwill knows this and uses it to their advantage whenever possible.

Goodwill claims that ~89-93 cents of every dollar (varies by location) spent in their stores goes toward vocational training and employment services. That’s a complete lie. All their programs are funded by/through government grants. Look at their Form 990 filings on [ProPublica](https://projects.propublica.org/nonprofits/). At the location where I worked, only about 9 cents of every dollar actually went to those services. The rest went toward executive compensation and profit-driven operations under the guise of charity. Goodwill does next to nothing to actually help people.

In addition to not helping the public and/or community, Goodwill doesn’t even help their own employees! After a major hurricane in which many employees were without power and some lost their homes/everything, etc. Goodwill told us if we needed anything, we should contact Workforce Solutions. Goodwill offered *zero* assistance. They also required us to go into the office or face termination. Their warehouses and offices are often filled with OSHA violations, requiring employees to stay at work at times when there is no running water or bathroom available, or when there is no A/C. Hell, my location tried to force us into an office that they knew was infested with bedbugs and threatened to terminate us if we didn’t go in.

Goodwill management *loves* to threaten employees. It’s their go-to for anything and everything. So, let’s say you are actually terminated by Goodwill…good luck getting unemployment! Goodwill fights *every single claim* tooth and nail to make sure the terminated employee does not get a single dime in unemployment benefits. If you happen to win and are awarded benefits, they will submit as many appeals as they are legally allowed to. They have no problem kicking you while you’re down and out. They love it. Yes, they’re *this* pathetic.

This doesn’t even scratch the surface of how shitty Goodwill is. I didn’t even mention how they hire disabled workers so they can pay them below minimum wage (as little as $0.22/hr) which they’re able to do because of an archaic law that is only still on the books because Goodwill executives lobby the government to keep the law on the books (CEO of the Goodwill I worked at said that keeping this law on the books is his **top** priority every year), or how they ran a public smear campaign on an employee who died on the job due to their negligence in an attempt to sway public opinion and avoid paying out a settlement to the family (They also fired the whistleblower btw), or any of the million other terrible things they’ve done…🙄

They give little back to the community and operate with the same greed you’d expect from a for-profit corporation—just without the accountability.

**They take more than they give. They harm more than they help**. **Stop giving them your money**. **They don’t deserve it.**"""

keywords = {'Goodwill'}

resultsCount = 0

for sub in subreddits:
    subreddit = reddit.subreddit(sub)
    # Check posts
    for submission in subreddit.hot(limit=20):
        text = (submission.title + " " + submission.selftext).lower()
        if any(keyword.lower() in text for keyword in keywords):
            if submission.author and submission.author.name.lower() == username.lower():
                continue
            print("Bot replying to post: ")
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)
            print("----------------------------")
            print(content, "This was generated by a bot!")
            print()
            try:
                submission.reply(content)
                resultsCount += 1
                logging.info(f"Replied to post in r/{sub}: {submission.title}")
                sleep(60)
            except Exception as e:
                print("Error replying to post: ", e)
                logging.info(f"Error replying to post in r/{sub}: {e}")
        # Check comments
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            if any(keyword.lower() in comment.body.lower() for keyword in keywords):
                print("Bot replying to comment: ")
                print("Comment: ", comment.body)
                print("----------------------------")
                try:
                    comment.reply(content)
                    resultsCount += 1
                    logging.info(f"Replied to comment in r/{sub}: {comment.body}...")
                    sleep(120)
                except Exception as e:
                    print("Error replying to comment: ", e)
                    logging.info(f"Error replying to comment in r/{sub}: {e}")

if resultsCount == 0:
    print()
    print("Sorry. I didn't find any posts or comments with those keywords.")
    logging.info("No posts or comments found with the specified keywords.")