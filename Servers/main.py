from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent, LikeEvent, SubscribeEvent, EmoteChatEvent
from colorama import Fore, Style, init
from tkinter import *
import random

responses = [
    "Sí.",
    "No.",
    "Tal vez algún día...",
    "No cuentes con ello.",
    "Definitivamente sí.",
    "Pregunta de nuevo más tarde.",
    "No lo creo.",
    "Es posible.",
    "Claro que sí.",
    "Sin lugar a dudas.",
    "Probablemente.",
    "No estoy seguro.",
    "Eso es un misterio.",
    "Cuenta con ello.",
    "Las estrellas dicen que sí.",
    "Por supuesto.",
    "No puedo decirlo ahora.",
    "Lo dudo mucho.",
    "Sí, pero no ahora.",
    "Mis fuentes dicen que no.",
    "Es una buena pregunta.",
    "El tiempo lo dirá.",
    "Sí, pero necesitarás paciencia.",
    "Mejor no te lo digo ahora.",
    "Sin duda alguna.",
    "No lo veo claro.",
    "Parece prometedor.",
    "No hay dudas al respecto.",
    "Podría ser.",
    "Ciertamente.",
    "Solo si llevas calcetines a juego.",
    "No hasta que los cerdos vuelen.",
    "Es más probable que te caiga un rayo.",
    "¡Claro! Y también me compraré una isla.",
    "Pregúntale a tu gato.",
    "Solo si puedes bailar el hula hoop.",
    "No, pero podrías intentarlo.",
    "Sí, y el cielo es verde.",
    "Eso depende de qué lado de la cama te levantes.",
    "¡Sí! En un universo paralelo.",
    "Solo si haces una reverencia primero.",
    "Mis antenas dicen que sí.",
    "Solo si puedes tocarte la nariz con la lengua.",
    "Solo si prometes ser bueno.",
    "Sí, pero solo los martes."
]


# Initialize colorama
init()

# Create the client
client: TikTokLiveClient = TikTokLiveClient(unique_id="@isabella.elaaa")

# Listen to an event with a decorator!
@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"Connected to @{event.unique_id} (Room ID: {client.room_id}") 
    
    
# Event to comment
async def on_comment(event: CommentEvent) -> None:
    comment = event.comment
    if comment.lower().startswith("caracola"):
        # Eliminar "caracola" y cualquier espacio en blanco adicional al principio
        remaining_text = comment[len("caracola"):].strip()
        print("-----------------------------------------")
        print(Fore.RED + f"{event.user.nickname} pregunta:" + Style.RESET_ALL)
        print(Fore.BLUE + f"{remaining_text}" + Style.RESET_ALL)
        print(Fore.BLUE + random.choice(responses) + Style.RESET_ALL)
        print("-----------------------------------------")
    else:
        print(f"{event.user.nickname} -> {comment}")

client.add_listener(CommentEvent, on_comment)

# Event to SubscribeEvent
@client.on(SubscribeEvent)
async def on_follow(event: SubscribeEvent) -> None:
    print("-----------------------------------------")
    print(Fore.GREEN + f"{event.user.nickname} followed you")
    print("-----------------------------------------")

# EmoteChatEvent send emote

@client.on(EmoteChatEvent)
async def on_follow(event: EmoteChatEvent) -> None:
    print(Fore.YELLOW +"-----------------------------------------"+ Style.RESET_ALL)
    print(Fore.YELLOW +"-----------------------------------------"+ Style.RESET_ALL)
    print(Fore.YELLOW +"-----------------------------------------"+ Style.RESET_ALL)
    print(Fore.YELLOW + f"{event.user.nickname} 🥰 ENVIO UN REGALO 🥰"+ Style.RESET_ALL)
    print(Fore.YELLOW +"-----------------------------------------"+ Style.RESET_ALL)
    print(Fore.YELLOW +"-----------------------------------------"+ Style.RESET_ALL)
    print(Fore.YELLOW +"-----------------------------------------"+ Style.RESET_ALL)




if __name__ == '__main__':
    client.run()
    