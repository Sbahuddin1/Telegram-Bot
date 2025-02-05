from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from deepseek import generate_response  # Import the model's response generation function

TOKEN: Final = "<token>"
BOT_USERNAME: Final = "@username" #@ <-- this sign is necessary at the start of username

#Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm Geek bot, right at your service. My only Purpose is to answer Math Problems.")
    

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("you can take a look at the commands section for that, I am trained on deepseeks qwen 1.5B parameter math model to solve math problems for you! Also, I am just a test project so I have shortcomings.")

async def commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here are the commands you can use:\n/start - Start the bot\n/help - Get help\n/commands - Get a list of commands\n/facebook - Get facebook \n/linkedin - get link to Linkedin\n/github - Get link to the girhub)")
                                    
async def linkedin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is the LinkedIn (https://www.linkedin.com/)", parse_mode='Markdown')
    
async def facebook(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is the Facebook (https://www.facebook.com/)", parse_mode='Markdown')
    
async def github(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here is the Github (https://github.com/)", parse_mode='Markdown')

#Response Handler
    
def handle_response(text: str) -> str:
    processed = text.lower()
    
    # Responses dictionary. If your AI model is good enough, you dont need all these, you can handle reponce with generate_responce function
    responses = {
        # Greetings
        "hi": "Hello! How can I help you?",
        "hello": "Hi there! How can I assist you today?",
        "hey": "Hey! What's on your mind?",
        "good morning": "Good morning! Hope you have a productive day ahead!",
        "good afternoon": "Good afternoon! How's it going?",
        "good evening": "Good evening! What can I do for you?",
        "how are you": "I'm a bot, so I'm always good",
        "what's up": "Not much! Just here to help",
        
        #casuals
        "ok": "Alright, let me know if you need anything else!",
        "okay": "Got it! What's next?",
        "cool": "Cool indeed! 😎 Anything else on your mind?",
        "good": "That's great to hear! How can I assist you further?",
        "nice": "Nice! I'm glad you think so.",
        "great": "Fantastic! Let me know if I can help with anything.",
        "awesome": "Awesome! I’m here if you need more help.",
        "wow": "Wow indeed! Did that surprise you?",
        "oops": "No worries, mistakes happen! Let me know if you need help fixing it.",
        "damn": "Oh, is something wrong? Let me know if I can help.",
        "sure": "Sure thing! What do you need?",
        "maybe": "Take your time! Let me know when you're ready.",
        "yep": "Yep! I'm here to assist you.",
        "nope": "Alright, let me know if you change your mind!",
        "lol": "Haha, I'm glad you found that funny!",
        "haha": "Glad to bring a smile! 😊",
        "oh": "Oh? Care to elaborate?",
        "huh": "Confused? Let me help you clear things up.",
        "ah": "Ah, gotcha! Need more info?",
        "hmm": "Thinking about something? Feel free to ask!",
        "yes": "Great!",
        "yeah": "Cool! What's next?",
        "yup": "Alright! Let me know how I can help.",
        "absolutely": "Absolutely! What do you need?",
        "of course": "Of course! I'm here to help.",
        "indeed": "Indeed! Glad we’re on the same page.",
        "right": "Right on! Let’s proceed.",
        "true": "Got it! Let’s move forward.",
        "correct": "Correct! Anything else I can do?",
        "no": "Alright!",
        "nah": "No problem, take your time!",
        "never": "Never say never! I’m here if you change your mind.",
        "false": "Okay, thanks for clarifying.",
        "wrong": "Oops, my bad! Let me correct that.",
        "not really": "Alright!",
        "same to you" : "Thanks!",

        # Farewells
        "bye": "Goodbye! Have a wonderful day!",
        "goodbye": "Take care! Hope to chat again soon!",
        "see you": "See you later! Stay safe!",
        "later": "Catch you later! Have a good one!",
        "take care": "You too! Stay awesome!",

        # Gratitude
        "thanks": "You're welcome! Always happy to assist.",
        "thank you": "You're welcome! Need help with anything else?",
        "much appreciated": "No problem at all!",
        "you're the best": "Aw, thanks! You made my day!",
        "appreciate it": "Glad I could help!",

        # Bot Info
        "who are you": "I'm Geek Bot, your friendly assistant!",
        "what can you do": "I can help with links, commands, jokes, quotes, and more! Use /commands to explore.",
        "what is your purpose": "To assist, entertain, and make your day a bit easier!",
        "help": "Need help? Use /commands to see what I can do!",
        "what is your name": "I'm Geek Bot, at your service!",
        "what do you do": "Nothin much actually",

        # Fun
        "tell me a joke": "I'm a geek, i don't joke around",
        "make me laugh": "Why don’t you take a look at your past for that?",
        "tell me a fact": "Did you know that the first computer virus was created in 1983, in Pakistan?",
    }

    # Search through the responses dictionary
    for key, response in responses.items():
        if key in processed:
            return response

    # Default fallback if no match is found
    return generate_response(text)
        
    
#Message Handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str =  update.message.chat.type
    text: str = update.message.text

    print(f'User {update.message.chat.id} in {message_type}: "{text}"')
    
    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text) 
        else:
            return
        
    else:
        response: str = handle_response(text)
        
    print(f'Bot: "{response}"')
    await update.message.reply_text(response)
    
    
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    
    
if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    
    #commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("commands", commands))
    app.add_handler(CommandHandler("linkedin", linkedin))
    app.add_handler(CommandHandler("facebook", facebook))
    app.add_handler(CommandHandler("github", github))
    
    #message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    #error
    app.add_error_handler(error)
    print("Bot is running...")
    app.run_polling(poll_interval=30)