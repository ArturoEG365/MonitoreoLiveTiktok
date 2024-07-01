from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent, LikeEvent, SubscribeEvent
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
    "Sin lugar a dudas."
]


# Initialize colorama
init()

# Create the client
client: TikTokLiveClient = TikTokLiveClient(unique_id="@fandelospayasosdefede")

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


# Event to liked
@client.on(LikeEvent)
async def on_like(event: LikeEvent) -> None:
    print(f"{event.user.nickname} liked the stream!")


# Event to SubscribeEvent
@client.on(SubscribeEvent)
async def on_follow(event: SubscribeEvent) -> None:
    print("-----------------------------------------")
    print(Fore.GREEN + f"{event.user.nickname} followed you")
    print("-----------------------------------------")

if __name__ == '__main__':
    client.run()
    