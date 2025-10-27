import speech_recognition as sr
import pywhatkit
import webbrowser
import datetime
import time
import pyttsx3
import wikipedia


def voice_assistant():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for command...")
        audio = recognizer.listen(source)
        
    try:    
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")
        
        if "time" in command.lower():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Current time is {current_time}")
        
        elif "date" in command.lower():
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            print(f"Today's date is {current_date}")
        
        elif "wikipedia" in command.lower():
            query = command.lower().replace("wikipedia", "").strip()
            if query:
                summary = wikipedia.summary(query, sentences=4)
                print(f"Wikipedia summary for {query}: {summary}")
                engine.say(summary)
                engine.runAndWait()
            else:
                print("No search term provided for Wikipedia.")
                return
        
        elif "open youtube" in command.lower():
            webbrowser.open("https://www.youtube.com")
            print("Opening YouTube...")
        
        elif "play" in command.lower():
            song = command.lower().replace("play", "").strip()
            if song:
                pywhatkit.playonyt(song)
                print(f"Playing {song} on YouTube...")
            else:
                print("No song name provided to play.")
                return
        
        elif "whatsapp" in command.lower():
            webbrowser.open("https://web.whatsapp.com/")
            
        elif "local files" in command.lower():
            webbrowser.open("C:\\Users\\gdhin\\OneDrive\\Desktop\\VR\\vr\\Scripts")
            print("Opening local files...") 
            
        
        elif "exit" in command.lower() or "quit" in command.lower():
            print("Exiting program.")
        
        else:
            print("Command not recognized.")
            
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        engine.say("An unexpected error occurred.")
        engine.runAndWait()
        
    time.sleep(1)
    print("Program finished.")

# To run the function
voice_assistant()
