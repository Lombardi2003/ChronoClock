import json
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Carica del file JSON con le configurazioni del bot
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

# Funzione per gestire il comando /start
async def start(update: Update, context: CallbackContext) -> None:
    """Mostra la tastiera personalizzata e un messaggio di benvenuto"""

    await update.message.reply_text(
        "Ciao! 👋 Sono il tuo assistente per gestire promemoria e notifiche.\n\n"
        "Con me, puoi facilmente:\n"
        "🔔 Impostare un promemoria\n"
        "📋 Visualizzare i promemoria attivi\n"
        "❌ Cancellare un promemoria\n\n"
        "Scegli un'opzione per iniziare:",
        reply_markup=reply_markup # Mostra la tastiera personalizzata
    )

# Funzione per gestire l'inserimento di un nuovo promemoria
async def newremind(update: Update, context: CallbackContext) -> None:
    """Imposta un promemoria"""
    await update.message.reply_text("Funzione Imposta Promemoria 📅 (da implementare)")

# Funzione per visualizzare i promemoria attivi
async def viewremind(update: Update, context: CallbackContext) -> None:
    """Visualizza i promemoria attivi"""
    await update.message.reply_text("Ecco i tuoi promemoria 📋 (da implementare)")

# Funzione per cancellare un promemoria esistente
async def delremind(update: Update, context: CallbackContext) -> None:
    """Cancella un promemoria"""
    await update.message.reply_text("Funzione Cancella Promemoria 📅 (da implementare)")

# Funzione per gestire i messaggi inviati dall'utente: update -> informazioni sul messaggio inviato dall'utente, context -> informazioni aggiuntive per gestire il messaggio
async def handle_message(update: Update, context: CallbackContext) -> None:
    """Gestisce i messaggi inviati dall'utente e risponde con un messaggio di errore"""
    text = update.message.text # Estrae il testo del messaggio inviato dall'utente
    # Gestione delle azioni in base al testo del messaggio
    if text == "🔔 Imposta Promemoria":
        await newremind(update, context)
    elif text == "📋 Visualizza Promemoria":
        await viewremind(update, context)
    elif text == "❌ Cancela Promemoria":
        await delremind(update, context)
    else:
        await update.message.reply_text("Non ho capito. Usa i pulsanti per interagire meglio! 😊")

def main():
    # Creazione dell'istanza principale del bot Telegram
    app = Application.builder().token(TOKEN).build() # Inizializza e configura il bot Telegram, impostando il token di autenticazione e creando l'istanza pronta all'uso. 
    # Comando /start per mostrare il menu
    app.add_handler(CommandHandler("start", start))
    # Comando /newremind per mostrare il menu
    app.add_handler(CommandHandler("newremind", newremind))
    # Comando /viewremind per mostrare il menu
    app.add_handler(CommandHandler("viewremind", viewremind))
    # Comando /delremind per mostrare il menu
    app.add_handler(CommandHandler("delremind", delremind))
    # Gestore per rispondere ai messaggi inviati dagli utenti
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot avviato...")

    # Avvia il bot in modalità polling per ricevere continuamente i comandi -> il bot invia continuamente richieste ai server Telegram per controllare se ci sono nuovi messaggi da gestire
    app.run_polling()

# Avvio del programma
if __name__ == "__main__":
    main()
