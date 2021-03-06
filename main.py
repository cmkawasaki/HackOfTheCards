from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
from flask import make_response

import cgi
import urllib
import webapp2

from google.appengine.ext import ndb

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

DEFAULT_CHAT_NAME = "Test_Chat"

def chatlog_key(chatlog_name=DEFAULT_CHAT_NAME):
	return ndb.Key('ChatLog', chatlog_name)

class ChatLog(ndb.Model):
	author = ndb.StringProperty(indexed=False)
	content = ndb.StringProperty(indexed=False)
	date = ndb.DateTimeProperty(auto_now_add=True)

@app.route('/')
def hello():
	"""Return a friendly HTTP greeting."""
	user = request.args.get('name', "")
	#chatlist = []

	if user is None:
		user = ""

	#Insert DB Query here.
	#historyQuery = ChatLog.query(ancestor = chatlog_key(DEFAULT_CHAT_NAME)).order(+ChatLog.date)
	#history = historyQuery.fetch(10)

	#for item in history:
	#	chatlist.append('<b>%s</b>: ' % cgi.escape(item.author))
	#	chatlist.append('%s<br>' % cgi.escape(item.content))

	#chat = ''.join(chatlist)

	return render_template('index.html', username=user)

@app.route('/write', methods=['GET', 'POST'])
def writeMe():
	if request.method == 'GET':
		user = request.args.get('chat_name')
		message = request.args.get('content')
	else:
		if request.json:
			user = request.json('chat_name')
			message = request.json('content')
		else:
			user = request.form['chat_name']
			message = request.form['content']

	app.logger.error(request)
	if user is None:
		user = "Anonymous"
	
	if message is None:
		message = ""

	chat = ChatLog(parent=chatlog_key(DEFAULT_CHAT_NAME))
	chat.author = user
	chat.content = message
	chat.put()
	return make_response("", 200)

@app.route('/chat', methods=['GET'])
def getLogs():
	historyQuery = ChatLog.query(ancestor = chatlog_key(DEFAULT_CHAT_NAME)).order(-ChatLog.date)
	history = historyQuery.fetch(10)
	history.reverse()
	chatlist = []
	for item in history:
		if item.author is None:
			item.author = ""
		if item.content is None:
			item.content = ""
		chatlist.append('<b>%s</b>: ' % cgi.escape(item.author))
		chatlist.append('%s<br>' % cgi.escape(item.content))

	chat = ''.join(chatlist)
	return chat

@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, nothing at this URL.', 404
