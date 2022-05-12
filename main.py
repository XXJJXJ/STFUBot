import telegram.ext
from profanity_check import predict_prob

TOKEN = open("TOKEN", "r").read()

THRESHOLD = 0.65

def start(update, context):
    update.message.reply_text("Thank you for adding me to this group!\n"
                              "I will my best to keep this group profanity free!\n\n"
                              "Though I might miss a few sometimes :sad")

def handleMessage(update, context):
    msg = [update.message.text]
    userDetails = update.message.from_user
    user = userDetails['username']
    likelihood_of_profanity = predict_prob(msg)
    # print(f"Msg: ({user}) {update.message.text} and vulgar level: {likelihood_of_profanity}")
    if likelihood_of_profanity > THRESHOLD:
        update.message.reply_text(f"Message by: @{user} is pretty vulgar! I have removed it!")
        bot.deleteMessage(update.message.chat.id, update.message.message_id)

    # else:
        # update.message.reply_text("Nothing wrong with whatever you said!")


bot = telegram.bot.Bot(TOKEN)
updater = telegram.ext.Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handleMessage))

updater.start_polling()
updater.idle()
