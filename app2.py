import os
import asyncio
from threading import Thread
from fastapi import FastAPI
import uvicorn
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

import os
from dotenv import load_dotenv   # ✅ import qilish kerak

# .env faylni yuklash
load_dotenv()

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("❌ Bot token topilmadi! Render Environment Variables da TOKEN qo'shilsin.")


# Bot va Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- O'quvchilar ma'lumotlari (qisqartirilgan, o'zing to'ldirasan) ---
students = {
    "Salohiddin": {
        "Jurnaldagi raqam": "1",
        "F.I.Sh": "Adamboev Salohiddin Alisher o‘g‘li",
        "Telefon": "+998999532270",
        "Guvohnoma": "I-QQ 0236050",
        "Tug'ilgan sana": "8/23/2009",
        "JSHSHR": "52308097350024",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Surayyo": {
        "Jurnaldagi raqam": "2",
        "F.I.Sh": "Ataxonova Surayyo G'ayratjon qiz",
        "Telefon": "+998882090112",
        "Guvohnoma": "I-QQ 0242841",
        "Tug'ilgan sana": "10/1/2009",
        "JSHSHR": "60110097350026",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Bazarbayeva Maftuna": {
        "Jurnaldagi raqam": "3",
        "F.I.Sh": "Bozorbayeva Maftuna Murodjon qizi",
        "Telefon": "+998931597900",
        "Guvohnoma": "I-QQ 0243070",
        "Tug'ilgan sana": "10/10/2009",
        "JSHSHR": "61010097350066",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Alibek": {
        "Jurnaldagi raqam": "4",
        "F.I.Sh": "Bekpo'latov Alibek O'ktam o'g'li",
        "Telefon": "+998996900919",
        "Guvohnoma": "I-QQ 0208642",
        "Tug'ilgan sana": "4/2/2009",
        "JSHSHR": "50204097350070",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Bobur": {
        "Jurnaldagi raqam": "5",
        "F.I.Sh": "Baltabayev Bobur Umidjon o'g'li",
        "Telefon": "+998992174082",
        "Guvohnoma": "I-QQ 0208438",
        "Tug'ilgan sana": "3/7/2009",
        "JSHSHR": "50703097350041",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Baltabayeva Maftuna": {
        "Jurnaldagi raqam": "6",
        "F.I.Sh": "Baltabayeva Maftuna Bekjon qizi",
        "Telefon": "+998997024082",
        "Guvohnoma": "I-QQ 0243095",
        "Tug'ilgan sana": "10/19/2009",
        "JSHSHR": "61910097350072",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Arslon": {
        "Jurnaldagi raqam": "7",
        "F.I.Sh": "Buabayev Arislon Alisher o'g'li",
        "Telefon": "+998990350451",
        "Guvohnoma": "I-QQ 0239401",
        "Tug'ilgan sana": "9/4/2009",
        "JSHSHR": "50409097350046",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Gulchehra": {
        "Jurnaldagi raqam": "8",
        "F.I.Sh": "Davletboyeva Gulchehra",
        "Telefon": "+998999582504",
        "Guvohnoma": "I-QQ 0265170",
        "Tug'ilgan sana": "4/6/2010",
        "JSHSHR": "60604107350055",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Mohida": {
        "Jurnaldagi raqam": "9",
        "F.I.Sh": "Karimbayeva Mohida Rustam qizi",
        "Telefon": "+998973491028",
        "Guvohnoma": "I-QQ 0243127",
        "Tug'ilgan sana": "10/22/2009",
        "JSHSHR": "62210097350047",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Kurbanbayeva Maftuna": {
        "Jurnaldagi raqam": "10",
        "F.I.Sh": "Kurbanbayeva Maftuna",
        "Telefon": "+998912694612",
        "Guvohnoma": "I-QQ 0253223",
        "Tug'ilgan sana": "1/31/2010",
        "JSHSHR": "63101107350050",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Murodova Maftuna": {
        "Jurnaldagi raqam": "11",
        "F.I.Sh": "Murodova Maftuna Ortiqbay qizi",
        "Telefon": "+998996808487",
        "Guvohnoma": "I-QQ 0245962",
        "Tug'ilgan sana": "11/13/2009",
        "JSHSHR": "61311097350086",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Mashhura": {
        "Jurnaldagi raqam": "12",
        "F.I.Sh": "Matkarimov Mashhura Mamud qizi",
        "Telefon": "+998992207983",
        "Guvohnoma": "I-QQ 0232310",
        "Tug'ilgan sana": "8/12/2009",
        "JSHSHR": "61208097350010",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Marjona": {
        "Jurnaldagi raqam": "13",
        "F.I.Sh": "Matkarimova Marjona Maxmud qizi",
        "Telefon": "+998973599988",
        "Guvohnoma": "I-QQ 0208063",
        "Tug'ilgan sana": "1/27/2009",
        "JSHSHR": "62701097350031",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Shoira": {
        "Jurnaldagi raqam": "14",
        "F.I.Sh": "Otoxonova Shoira G'anijon qiz",
        "Telefon": "+998979608184",
        "Guvohnoma": "I-QQ 0224139",
        "Tug'ilgan sana": "5/17/2009",
        "JSHSHR": "61705097350023",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Hilola": {
        "Jurnaldagi raqam": "15",
        "F.I.Sh": "Qo'zibayeva Hilola Odilbek qizi",
        "Telefon": "+998880558204",
        "Guvohnoma": "I-QQ 0245852",
        "Tug'ilgan sana": "11/5/2009",
        "JSHSHR": "60511097350085",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Nozima": {
        "Jurnaldagi raqam": "16",
        "F.I.Sh": "Qo'zibayeva Nozima Jonibek qizi",
        "Telefon": "+998973532235",
        "Guvohnoma": "I-QQ 0224563",
        "Tug'ilgan sana": "6/25/2009",
        "JSHSHR": "62506097350034",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Asad": {
        "Jurnaldagi raqam": "17",
        "F.I.Sh": "Sadullayev Asad",
        "Telefon": "+998994021509",
        "Guvohnoma": "I-TN 0288243",
        "Tug'ilgan sana": "9/15/2009",
        "JSHSHR": "Mavjud emas",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Xurshid": {
        "Jurnaldagi raqam": "18",
        "F.I.Sh": "Samandarov Xurshid Maxsud o'g'li",
        "Telefon": "+998997940126",
        "Passport raqam": "AE2693500",
        "Guvohnoma": "I-QQ 0224074",
        "Tug'ilgan sana": "5/8/2009",
        "JSHSHR": "50805097350024",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Sarvar": {
        "Jurnaldagi raqam": "19",
        "F.I.Sh": "Saparbayev Sarvar Baxrom o'g'li",
        "Telefon": "+998770992650",
        "Guvohnoma": "I-QQ 0239545",
        "Tug'ilgan sana": "9/19/2009",
        "JSHSHR": "51909097350037",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Saida": {
        "Jurnaldagi raqam": "20",
        "F.I.Sh": "Sultonova Saida Davron qizi",
        "Telefon": "+998997358406",
        "Guvohnoma": "I-QQ 0224157",
        "Tug'ilgan sana": "5/18/2009",
        "JSHSHR": "61805097350031",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Gulmira": {
        "Jurnaldagi raqam": "21",
        "F.I.Sh": "Tajimuratova Gulmira",
        "Telefon": "+998990317540",
        "Guvohnoma": "I-QQ 0265797",
        "Tug'ilgan sana": "5/29/2010",
        "JSHSHR": "62905107350071",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Lobar": {
        "Jurnaldagi raqam": "22",
        "F.I.Sh": "Xakimova Lobar Oybek qizi",
        "Telefon": "+998975008054",
        "Guvohnoma": "I-QQ 0239399",
        "Tug'ilgan sana": "9/8/2009",
        "JSHSHR": "60809097350100",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Dilnura": {
        "Jurnaldagi raqam": "23",
        "F.I.Sh": "Yusupova Dilnura",
        "Telefon": "+9989149308520",
        "Guvohnoma": "I-QQ 0232247",
        "Tug'ilgan sana": "8/7/2009",
        "JSHSHR": "60708097350029",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Umida": {
        "Jurnaldagi raqam": "24",
        "F.I.Sh": "",
        "Telefon": "+998991794331",
        "Guvohnoma": "I-QQ 0208204",
        "Tug'ilgan sana": "2/12/2009",
        "JSHSHR": "61202097350029",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    "Nabi": {
        "Jurnaldagi raqam": "25",
        "F.I.Sh": "Yakubov  Nabi Dilshod o'g'li",
        "Telefon": "+998996962322",
        "Guvohnoma": "I-QQ 0239647",
        "Tug'ilgan sana": "9/25/2009",
        "JSHSHR": "52509097350113",
        "Qo‘shimcha": "10-A sinf o‘quvchisi"
    },
    # ❗️ qolganlarin
    # ...
}

# --- Telegram bot handlerlari ---
@dp.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer("Assalomu alaykum!\nO‘quvchi ismini kiriting:")

@dp.message()
async def get_student_info(message: Message):
    name = message.text.strip()
    if name in students:
        data = students[name]
        response = (
            f"👤 F.I.Sh: {data['F.I.Sh']}\n"
            f"🔢 Jurnaldagi raqam: {data['Jurnaldagi raqam']}\n"
            f"📞 Telefon: {data['Telefon']}\n"
            f"🪪 Passport raqam: {data.get('Passport raqam', 'Mavjud emas')}\n"
            f"📄 Guvohnoma: {data['Guvohnoma']}\n"
            f"🎂 Tug'ilgan sana: {data['Tug\'ilgan sana']}\n"
            f"🆔 JSHSHR: {data['JSHSHR']}\n"
            f"ℹ️ Qo‘shimcha: {data['Qo‘shimcha']}"
        )
    else:
        response = "❌ Bunday o‘quvchi topilmadi."
    await message.answer(response)

# --- FastAPI server ---
app = FastAPI()

@app.get("/")
async def root():
    return {"status": "Bot ishlayapti!"}

# --- Botni ishga tushirish ---
async def start_bot():
    await dp.start_polling(bot)

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot())

# --- Render parallel ishga tushirishi ---
if __name__ == "__main__":
    Thread(target=run_bot, daemon=True).start()
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
