from moviepy.editor import VideoFileClip
import speech_recognition as sr
import pyttsx3

def init_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    return engine

def talk(engine, text):
    engine.say(text)
    engine.runAndWait()

def take_command(listener, timeout=5):
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source, timeout=timeout)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please repeat.")
        return take_command(listener, timeout)  # Recursive call to listen again
    except sr.WaitTimeoutError:
        print("Listening timed out. Please say the command again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    return command

def play_audio(filename):
    try:
        clip = VideoFileClip(filename)
        clip.preview()
    except Exception as e:
        print(f"Error playing the audio file: {e}")

def run_bot():
    listener = sr.Recognizer()
    engine = init_engine()

    while True:
        command = take_command(listener)
        print(command)

        if 'nice' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\nicetomeetyou.mp4")

        elif 'nice to meet you' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\nicetomeetyou.mp4")


        elif 'what is your name' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\iampjhsrobot.mp4")
 
        elif 'name' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\iampjhsrobot.mp4")


        elif 'could you tell me more about yourself' in command:


            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\abtmyself.mp4")

        elif 'yourself' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\abtmyself.mp4")


        elif 'could you tell me about aga khan education service' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\akespart1.mp4")

        elif 'can you tell me about aga khan education service' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\akespart1.mp4")


        elif 'tell me more about aga khan education service' in command:
            play_audio("C:\\Users\domta\\Downloads\\RootDev\Answer Voices\\akespart2.mp4")
        

        elif 'could you tell me about aga khan education services' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\akespart1.mp4")

        elif 'could you tell me about alkaline education service' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\akespart1.mp4")

        elif 'tell me about alkaline education service' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\akespart1.mp4")

        elif 'tell me about aga khan education service' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\akespart1.mp4")
 
        elif 'can you tell me about aga khan education services' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\akespart1.mp4")


        elif 'tell me more about aga khan education services' in command:
            play_audio("C:\\Users\domta\\Downloads\\RootDev\Answer Voices\\akespart2.mp4")
 

        elif 'tell me about platinum jubilee high school' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\abtpjhs.mp4")

        elif 'could you tell me about platinum jubilee high school' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\abtpjhs.mp4")

        elif 'could you tell me about platinum jewellery high school' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\abtpjhs.mp4")

        elif 'tell me about platinum jewellery high school' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\abtpjhs.mp4")

        elif 'how about learning in platinum jubilee high school' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\howabtlearninginpjhs.mp4")


        elif 'how about learning and platinum jubilee high school' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\howabtlearninginpjhs.mp4")

        elif 'learning in platinum jubilee high school' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\howabtlearninginpjhs.mp4")

        elif 'how much learning in platinum jubilee high school' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\howabtlearninginpjhs.mp4")


        elif 'what facilities does platinum jewellery high school offer' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\fecillitys.mp4")

        elif 'what facilities does platinum jubilee high school offer' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\fecillitys.mp4")


        elif 'what is the purpose of atal tinkering laboratory' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\athuallab.mp4")
        

        elif 'what is the purpose of atal tinkering laborat' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\athuallab.mp4")

        elif 'what facility does platinum jubilee high school offer' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\fecillitys.mp4")

        elif ' what facilities does platform give me high school offer' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\fecillitys.mp4")
        
        elif 'what facilities from platinum jubilee high school' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\fecillitys.mp4")


        elif 'what facilities the platinum jubilee high school' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\fecillitys.mp4")
    
        elif 'what facility does platinum jubilee high school offer' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\fecillitys.mp4")

        elif 'facility does platinum ' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\fecillitys.mp4")

        elif 'any major achievements for this academic year' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\majarachivemenrts.mp4")

        elif 'any major achievement for this academic year' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\majarachivemenrts.mp4")

        elif 'major achievement' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\majarachivemenrts.mp4")

        elif 'animation achievement for the academic year' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\majarachivemenrts.mp4")

        elif 'how many major' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\majarachivemenrts.mp4")

        elif 'when can we meet you again' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\70thani.mp4")


        elif 'who created you' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\whocreratedu.mp4")

        elif 'created' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\whocreratedu.mp4")

        elif 'created you' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\whocreratedu.mp4")
        
        elif 'bye-bye' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\nicebyebye.mp4")
        elif 'bye bye' in command:
            play_audio("C:\\Users\\domta\\Downloads\\RootDev\Answer Voices\\nicebyebye.mp4")
        
            break

if __name__ == "__main__":
    run_bot()
