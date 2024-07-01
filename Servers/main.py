from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent, LikeEvent, SubscribeEvent
from colorama import Fore, Style, init

# Initialize colorama
init()

# Create the client
client: TikTokLiveClient = TikTokLiveClient(unique_id="@vitolin_r")

# Listen to an event with a decorator!
@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"Connected to @{event.unique_id} (Room ID: {client.room_id}") 
    
    
# Event to comment
async def on_comment(event: CommentEvent) -> None:
    comment = event.comment
    if comment.lower().startswith("caracola"):
        print("-----------------------------------------")
        print(Fore.RED + f"{event.user.nickname} -> {comment}" + Style.RESET_ALL)
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
    print(f"{event.user.nickname} followed you")


if __name__ == '__main__':
    client.run()
