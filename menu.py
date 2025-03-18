import json
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Carica il file JSON
with open('config.json', 'r') as file:
    config = json.load(file)

# Token del bot -> metodo per interagire con l'API di Telegram
TOKEN = config['TOKEN']

# Tastiera personalizzata per il menu
keyboard = [
    ["🔔 Imposta Promemoria", "📋 Visualizza Promemoria", "❌ Cancella Promemoria"]
]

# Creazione del layout della tastiera personalizzata
reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True  # Ridimensiona la tastiera per adattarla alla schermata dell'utente
)

async def start(update: Update, context: CallbackContext) -> None:
    """Mostra la tastiera personalizzata e un messaggio di benvenuto"""
    await update.message.reply_text(
        "Ciao! 👋 Sono il tuo assistente per gestire promemoria e notifiche.\n\n"
        "Con me, puoi facilmente:\n"
        "🔔 Impostare un promemoria\n"
        "📋 Visualizzare i promemoria attivi\n"
        "❌ Cancellare un promemoria\n\n"
        "Scegli un'opzione per iniziare:",
        reply_markup=reply_markup
    )


async def handle_message(update: Update, context: CallbackContext) -> None:
    """Gestisce i messaggi inviati dall'utente e risponde con un messaggio di errore"""
    text = update.message.text

    if text == "🔔 Imposta Promemoria":
        await update.message.reply_text("Funzione Imposta Promemoria 📅 (da implementare)")
    elif text == "📋 Visualizza Promemoria":
        await update.message.reply_text("Ecco i tuoi promemoria 📋 (da implementare)")
    elif text == "❌ Cancela Promemoria":
        await update.message.reply_text("Funzione Cancella Promemoria 📅 (da implementare)")
    else:
        await update.message.reply_text("Non ho capito. Usa i pulsanti per interagire! 😊")

def main():
    # Creazione dell'istanza principale del bot Telegram
    app = Application.builder().token(TOKEN).build() # Inizializza e configura il bot Telegram, impostando il token di autenticazione e creando l'istanza pronta all'uso. 
    
    # Comando /start per mostrare il menu
    app.add_handler(CommandHandler("start", start))
    
    # Gestore per rispondere ai messaggi inviati dagli utenti
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot avviato...")
    app.run_polling()

if __name__ == "__main__":
    main()
