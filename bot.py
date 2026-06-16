from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

TOKEN = "8365620682:AAEhhJUpAtWbf8oZ14CVIEmwUn_mUpSbBas"

async def receber(update: Update, context: ContextTypes.DEFAULT_TYPE):

    link = update.message.text

    imagem_url = "https://via.placeholder.com/500"

    response = requests.get(imagem_url)

    produto = Image.open(BytesIO(response.content))

    fundo = Image.new("RGB", (500, 500), (245,245,245))

    produto.thumbnail((300,300))

    fundo.paste(produto, (100,80))

    draw = ImageDraw.Draw(fundo)

    draw.text((150,400), "R$ 89,90", fill="red")

    arquivo = "resultado.jpg"

    fundo.save(arquivo)

    await update.message.reply_photo(photo=open(arquivo,"rb"))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT, receber)
)

app.run_polling()