from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")

def make_reply(msg):
	reply = None
	if msg is not None:
		reply = msg
	return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            bot.execute_command(message)
            f = open("results.txt", "r")
            reply = make_reply(f.read())
            bot.send_message(reply, from_)