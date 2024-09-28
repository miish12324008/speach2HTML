#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Assuming necessary libraries are installed and configured correctly
from pytube import YouTube
import speech_recognition as sr
import subprocess
import os
def download_audio(youtube_link):
    yt = YouTube(youtube_link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename='downloaded_audio.mp4')

def audio_to_text():
    # Assuming ffmpeg is installed and in PATH
    # Convert downloaded audio to a format suitable for speech_recognition
    subprocess.run(['ffmpeg', '-i', 'downloaded_audio.mp4', '-ar', '16000', '-ac', '1', 'converted_audio.wav'], check=True)

    recognizer = sr.Recognizer()
    with sr.AudioFile('converted_audio.wav') as source:
        audio = recognizer.record(source)  # Load the audio file
        try:
            text = recognizer.recognize_google(audio)  # Convert audio to text
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def write_text_to_file(text, filename='output.txt'):
    with open(filename, 'w') as file:
        file.write(text)

def main(youtube_link):
    download_audio(youtube_link)
    text = audio_to_text()
    write_text_to_file(text)
    # Optionally remove temporary files
    os.remove('downloaded_audio.mp4')
    os.remove('converted_audio.wav')

# Example usage:
youtube_link = input("Enter the YouTube link: ")
main(youtube_link)


# In[3]:


from pytube import YouTube
import speech_recognition as sr
import subprocess
import os

def download_audio(youtube_link):
    yt = YouTube(youtube_link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename='downloaded_audio.mp4')

def convert_audio_to_wav():
    subprocess.run(['ffmpeg', '-i', 'downloaded_audio.mp4', '-ar', '16000', '-ac', '1', 'converted_audio.wav'], check=True)

def audio_to_text():
    recognizer = sr.Recognizer()
    with sr.AudioFile('converted_audio.wav') as source:
        audio_data = recognizer.record(source)
        try:
            # Set the language to Hindi
            text = recognizer.recognize_google(audio_data, language='hi-IN')
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def write_text_to_file(text, filename='output.txt'):
    with open(filename, 'w') as file:
        file.write(text)

def clean_up():
    os.remove('downloaded_audio.mp4')
    os.remove('converted_audio.wav')

def main(youtube_link):
    download_audio(youtube_link)
    convert_audio_to_wav()
    text = audio_to_text()
    write_text_to_file(text)
    clean_up()

# Example usage
if __name__ == "__main__":
    youtube_link = input("Enter the YouTube link: ")
    main(youtube_link)
    print("Done. Check the output file for the extracted text.")


# In[7]:


import speech_recognition as sr
import subprocess
import os
from datetime import datetime
from pytube import YouTube

def download_audio_from_youtube(youtube_link):
    yt = YouTube(youtube_link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename='downloaded_audio.mp4')
    return 'downloaded_audio.mp4'

def convert_video_to_audio(video_path):
    audio_filename = 'converted_audio.wav'
    subprocess.run(['ffmpeg', '-i', video_path, '-ar', '16000', '-ac', '1', audio_filename], check=True)
    return audio_filename

def audio_to_text(audio_path, language):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language=language)
        return text

def write_text_to_file(text):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f'output_{timestamp}.txt'
    with open(filename, 'w') as file:
        file.write(text)

def process_input(input_path, language):
    if "youtube.com" in input_path or "youtu.be" in input_path:
        audio_file = download_audio_from_youtube(input_path)
    else:
        audio_file = convert_video_to_audio(input_path)
    
    text = audio_to_text(audio_file, language)
    write_text_to_file(text)
    
    os.remove(audio_file)

if __name__ == "__main__":
    input_path = input("Enter the YouTube link or the path to your local video file: ")
    language = input("Enter the language code (e.g., 'en-US' for English, 'hi-IN' for Hindi): ")
    process_input(input_path, language)
    print("Transcription completed.")


# In[2]:


from pytube import YouTube
import speech_recognition as sr
import subprocess
import os
from datetime import datetime

def download_audio(youtube_link):
    yt = YouTube(youtube_link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename='downloaded_audio.mp4')

def audio_to_text(language):
    # Assuming ffmpeg is installed and in PATH
    subprocess.run(['ffmpeg', '-i', 'downloaded_audio.mp4', '-ar', '16000', '-ac', '1', 'converted_audio.wav'], check=True)

    recognizer = sr.Recognizer()
    with sr.AudioFile('converted_audio.wav') as source:
        audio = recognizer.record(source)  # Load the audio file
        try:
            text = recognizer.recognize_google(audio, language=language)  # Convert audio to text based on specified language
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def write_text_to_file(text):
    # Create a filename with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f'output_{timestamp}.txt'
    with open(filename, 'w') as file:
        file.write(text)

def main(youtube_link, language):
    download_audio(youtube_link)
    text = audio_to_text(language)
    write_text_to_file(text)
    # Optionally remove temporary files
    os.remove('downloaded_audio.mp4')
    os.remove('converted_audio.wav')

# Example usage:
if __name__ == "__main__":
    youtube_link = input("Enter the YouTube link: ")
    print("Choose language for transcription: 'en-US' for English, 'hi-IN' for Hindi")
    language = input("Language code: ")
    main(youtube_link, language)
    print("Transcription completed.")


# In[1]:


from pytube import YouTube
import speech_recognition as sr
import subprocess
import os
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def download_audio(youtube_link):
    yt = YouTube(youtube_link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename='downloaded_audio.mp4')

def audio_to_text(language):
    subprocess.run(['ffmpeg', '-i', 'downloaded_audio.mp4', '-ar', '16000', '-ac', '1', 'converted_audio.wav'], check=True)

    recognizer = sr.Recognizer()
    with sr.AudioFile('converted_audio.wav') as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def write_text_to_file(text):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f'output_{timestamp}.txt'
    with open(filename, 'w') as file:
        file.write(text)
    return filename

def bold_important_words(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = word_tokenize(text)
    words_ns = [word for word in words if word.lower() not in stopwords.words('english')]
    fdist = FreqDist(words_ns)
    common_words = [word[0] for word in fdist.most_common(10)]

    bolded_text = " ".join([f"**{word}**" if word in common_words else word for word in words])
    with open(filename, 'w') as file:
        file.write(bolded_text)

def main(youtube_link, language):
    download_audio(youtube_link)
    text = audio_to_text(language)
    filename = write_text_to_file(text)
    bold_important_words(filename)
    os.remove('downloaded_audio.mp4')
    os.remove('converted_audio.wav')

if __name__ == "__main__":
    youtube_link = input("Enter the YouTube link: ")
    print("Choose language for transcription: 'en-US' for English, 'hi-IN' for Hindi")
    language = input("Language code: ")
    main(youtube_link, language)
    print("Transcription completed.")



# In[4]:


from pytube import YouTube
import speech_recognition as sr
import subprocess
import os
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def download_audio(youtube_link):
    yt = YouTube(youtube_link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename='downloaded_audio.mp4')

def audio_to_text(language):
    subprocess.run(['ffmpeg', '-i', 'downloaded_audio.mp4', '-ar', '16000', '-ac', '1', 'converted_audio.wav'], check=True)

    recognizer = sr.Recognizer()
    with sr.AudioFile('converted_audio.wav') as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def write_text_to_file(text):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f'output_{timestamp}.txt'
    with open(filename, 'w') as file:
        file.write(text)
    return filename

def bold_and_increase_font_of_important_words(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = word_tokenize(text)
    words_ns = [word for word in words if word.lower() not in stopwords.words('english')]
    fdist = FreqDist(words_ns)
    common_words = [word[0] for word in fdist.most_common(10)]

    # Updated to include HTML-style font size increase for important words
    enhanced_text = " ".join([f"<span style='font-size:24px;'><b>{word}</b></span>" if word in common_words else word for word in words])
    with open(filename, 'w') as file:
        file.write(enhanced_text)

def main(youtube_link, language):
    download_audio(youtube_link)
    text = audio_to_text(language)
    filename = write_text_to_file(text)
    bold_and_increase_font_of_important_words(filename)
    os.remove('downloaded_audio.mp4')
    os.remove('converted_audio.wav')

if __name__ == "__main__":
    youtube_link = input("Enter the YouTube link: ")
    print("Choose language for transcription: 'en-US' for English, 'hi-IN' for Hindi")
    language = input("Language code: ")
    main(youtube_link, language)
    print("Transcription completed.")


# # html file code

# In[ ]:


from pytube import YouTube
import speech_recognition as sr
import subprocess
import os
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def download_audio(youtube_link):
    yt = YouTube(youtube_link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename='downloaded_audio.mp4')

def audio_to_text(language):
    subprocess.run(['ffmpeg', '-i', 'downloaded_audio.mp4', '-ar', '16000', '-ac', '1', 'converted_audio.wav'], check=True)

    recognizer = sr.Recognizer()
    with sr.AudioFile('converted_audio.wav') as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def write_text_to_html_file(text):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f'output_{timestamp}.html'
    with open(filename, 'w') as file:
        file.write("<html><body><p>" + text + "</p></body></html>")
    return filename

def bold_and_increase_font_of_important_words_in_html(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = word_tokenize(text)
    words_ns = [word for word in words if word.lower() not in stopwords.words('english')]
    fdist = FreqDist(words_ns)
    common_words = [word[0] for word in fdist.most_common(10)]

    enhanced_text = " ".join([f"<span style='font-size:24px;'><b>{word}</b></span>" if word in common_words else word for word in words])
    with open(filename, 'w') as file:
        file.write("<html><head></head><body>" + enhanced_text + "</body></html>")

def main(youtube_link, language):
    download_audio(youtube_link)
    text = audio_to_text(language)
    filename = write_text_to_html_file(text)
    bold_and_increase_font_of_important_words_in_html(filename)
    os.remove('downloaded_audio.mp4')
    os.remove('converted_audio.wav')

if __name__ == "__main__":
    youtube_link = input("Enter the YouTube link: ")
    print("Choose language for transcription: 'en-US' for English, 'hi-IN' for Hindi")
    language = input("Language code: ")
    main(youtube_link, language)
    print("Transcription completed.")



# In[5]:


import tweepy
import os
import re

def initialize_twitter_api():
    # Prompt for Twitter API credentials
    API_KEY = input("Enter your Twitter API Key: ")
    API_SECRET_KEY = input("Enter your Twitter API Secret Key: ")
    ACCESS_TOKEN = input("Enter your Twitter Access Token: ")
    ACCESS_TOKEN_SECRET = input("Enter your Twitter Access Token Secret: ")

    # Setup access to API
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    return api

def fetch_tweet_text_from_link(api, twitter_link):
    # Extract tweet ID from the link
    tweet_id_match = re.search(r'/status/(\d+)', twitter_link)
    if tweet_id_match:
        tweet_id = tweet_id_match.group(1)
        try:
            tweet = api.get_status(tweet_id, tweet_mode='extended')
            return tweet.full_text
        except tweepy.TweepError as e:
            print(f"Error fetching tweet: {e}")
            return None
    else:
        print("Could not find a tweet ID in the link.")
        return None

def process_input(api, input_link):
    if "twitter.com" in input_link:
        tweet_text = fetch_tweet_text_from_link(api, input_link)
        if tweet_text:
            print("Tweet text:", tweet_text)
        else:
            print("Failed to fetch tweet text.")
    else:
        print("Unsupported link. Please provide a Twitter link.")

if __name__ == "__main__":
    api = initialize_twitter_api()
    input_link = input("Enter the Twitter link: ")
    process_input(api, input_link)


# In[ ]:


XYKZV4Dz7EfsU6qrI0tAnSwAo//api key
7K2Tx3fXaWZTJRus3fmHwv3Yn4aD8SQVCSDwuRzdfL6fmTzsej // api secret key
1772123017331535873-bSyFvwrzBnvhe0iXwyACOgXZzCDEqX // access token
FEyGTLksiIJlXP2R75mDhKTzmvxfIi6zCixgLlh6i7JI7 // access token secret


# In[6]:


import tweepy
import os
import re

def initialize_twitter_api():
    # Prompt for Twitter API credentials
    API_KEY = input("Enter your Twitter API Key: ")
    API_SECRET_KEY = input("Enter your Twitter API Secret Key: ")
    ACCESS_TOKEN = input("Enter your Twitter Access Token: ")
    ACCESS_TOKEN_SECRET = input("Enter your Twitter Access Token Secret: ")

    # Setup access to API
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    return api

def fetch_tweet_text_from_link(api, twitter_link):
    # Extract tweet ID from the link
    tweet_id_match = re.search(r'/status/(\d+)', twitter_link)
    if tweet_id_match:
        tweet_id = tweet_id_match.group(1)
        try:
            tweet = api.get_status(tweet_id, tweet_mode='extended')
            return tweet.full_text
        except Exception as e:  # Updated to catch any exception
            print(f"Error fetching tweet: {e}")
            return None
    else:
        print("Could not find a tweet ID in the link.")
        return None

def process_input(api, input_link):
    if "twitter.com" in input_link:
        tweet_text = fetch_tweet_text_from_link(api, input_link)
        if tweet_text:
            print("Tweet text:", tweet_text)
        else:
            print("Failed to fetch tweet text.")
    else:
        print("Unsupported link. Please provide a Twitter link.")

if __name__ == "__main__":
    api = initialize_twitter_api()
    input_link = input("Enter the Twitter link: ")
    process_input(api, input_link)

    


# In[ ]:


XYKZV4Dz7EfsU6qrI0tAnSwAo//api key
7K2Tx3fXaWZTJRus3fmHwv3Yn4aD8SQVCSDwuRzdfL6fmTzsej // api secret key
1772123017331535873-bSyFvwrzBnvhe0iXwyACOgXZzCDEqX // access token
FEyGTLksiIJlXP2R75mDhKTzmvxfIi6zCixgLlh6i7JI7 // access token secret


# In[1]:


import requests

# Placeholder for initializing Graph API
ACCESS_TOKEN = 'Your-Access-Token-Here'

def get_facebook_video_info(video_url):
    # Extract the video ID or unique identifier from the video URL
    video_id = 'Extracted-Video-ID-From-URL'

    # Construct API request to get video details
    api_url = f'https://graph.facebook.com/v13.0/{video_id}?fields=description,length,created_time&access_token={ACCESS_TOKEN}'
    
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    facebook_video_url = input("Enter the Facebook video URL: ")
    video_info = get_facebook_video_info(facebook_video_url)
    if video_info:
        print(video_info)
    else:
        print("Failed to retrieve video information.")


# In[ ]:




