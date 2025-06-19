from flask import Flask, request, jsonify
import snscrape.modules.twitter as sntwitter

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape_tweets():
    data = request.json
    query = data.get('query', '')
    max_results = int(data.get('limit', 10))

    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_results:
            break
        tweets.append({
            'text': tweet.content,
            'url': tweet.url,
            'date': tweet.date.isoformat(),
            'likes': tweet.likeCount,
            'retweets': tweet.retweetCount,
            'username': tweet.user.username
        })

    return jsonify(tweets)

app.run(host='0.0.0.0', port=8080)
