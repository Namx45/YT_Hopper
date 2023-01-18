from pytube import YouTube 
import os
  


def path():
    # change first str acording to your desktop path
    path = "D:\\OneDrive\\שולחן העבודה\\"
    #os.mkdir(path + "\\Songs")
    return path
  

# where to save
SAVE_PATH = path() #current_path()

  
# link of the video to be downloaded 
# opening the file 
with open('songList.txt', 'r') as links:
    for link in links.readlines(): 
        try: 
            # Current song (link)
            yt = YouTube(link) 
        except Exception as e: 
            print(e)  
      
        #filters audio only from all the files 
        audiofiles = yt.streams.filter(only_audio=True).all()
      
        print(type(audiofiles))
        print(audiofiles)
        try: 
            # downloading the audio 
            audiofiles[0].download(SAVE_PATH)
        except Exception as e: 
            print(e) 



print('Script completed...') 