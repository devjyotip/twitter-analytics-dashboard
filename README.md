Realtime Twitter Sentiment Analyzer Dashboard
_____________________________________________


1. Requirements
- python 2.7
- python2.7-dev
- mongodb server
- Flask
- 


2. Installation & Setup
apt-get install python2.7 python2.7-dev mongodb-server


Download and install required libs and data

    python setup.py develop
    python toolbox/setup-app.py



3. Data Collection
The base of data training is an assumption that tweets with happy emoticons :) are positive and tweets
with sad :( emoticons have negative sentiment polarity

Collect 2000 'happy' tweets

    python toolbox/collect-tweets.py happy 2000

Collect 2000 'sad' tweets

    python toolbox/collect-tweets.py sad 2000



4. Train classifier
Create and save new classifier trained from collected tweets

    python toolbox/train-classifier.py bayes 1000


5. Start server stack
open 3 shells and type in each:
    
    python start-collector.py

    python start-classifier.py

    python start-server.py
    

open browser on http://127.0.0.1:5000


6. ToDo
Run everything behind nginx>=1.3.13, automate processes management with supervisor.

Since nginx 1.3.13 supports websockets, so you should probably use latest stable version.

This is only one way of many to deploy the app.


