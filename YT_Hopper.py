from pytube import YouTube 
import os

def path():
    # change path according to your desktop path
    # dont forget for every '\' add a second one :)
    path = "D:\\Users\\User\\Desktop\\"
    # remove comment to force downloading to a folder instead of desktop
    #path += "\\Songs"; os.mkdir(path)
    return path

# loops through 
def links_loop(save_path):
    # loops through songs list & downloads to desktop
    with open('songList.txt', 'r', encoding="utf8") as links:
        for link in links.readlines():
            splited = link.split("|")
            song_link, song_name = splited[0], splited[1].strip()
            # downloads song (by link)
            if (download_song(song_link, save_path)) is None:
                print(f"Error with downloading song [%s]" % song_name)

# downloads (the first) song by its name by search in youtube
def search():
    print("\nComing soon...\nTry one of the other options :)\n")

def playlist(save_path):
    print("\nComing soon...\nTry one of the other options :)\n")

# download song via given link
def download_song(link, save_path):
    try: 
            # Current song (link)
            yt = YouTube(link) 
            # filters audio only from all the files
            audiofiles = yt.streams.filter(only_audio=True)
            # downloading the audio (to desktop path)
            audiofiles[0].download(save_path)
            return 1
    except Exception as e: 
            print(e) # debug
            return None



def menu():  
    save_path = path()
    print("""1. Download via searching song name
2. Download via list
3. Download via playlist
type 'quit' at menu choice to quit
    """)
    while (True):
        try:
            choice = input("")
            if (choice == "1"):
                search()
            elif (choice == "2"):
                links_loop(save_path)
            elif (choice == "3"):
                playlist(save_path)
            elif (choice.lower() == "quit"):
                sys.exit()
            else:
                raise Exception()
        except:
            print("Invalid choice\nLets try again...")


if (__name__ == "__main__"):
    #menu()
    links_loop(path())

print('Script completed...') 
