import speech_recognition
from transformers import pipeline

# Load the question-answering pipeline
qa_pipeline = pipeline("question-answering")

recognizer = speech_recognition.Recognizer()

# Adjust recognizer settings
recognizer.energy_threshold = 4000

def ask_question(question):
    options = []

    #Define responses for different types of questions
    question_responses = {
        "dinner": ["pasta", "chicken", "pizza", "salad"],
        "color": ["red", "blue", "green", "yellow"],
        #Add more types of questions and their responses as needed
    }

    #Check if any response matches the question
    for q_type, response in question_responses.items():
        if q_type in question:
            options.extend(response)

    #If no matching response found, provide default options
    if not options:
        options = ["option1", "option2", "option3"] #Default options

    return options

def main():
    print("Welcome to the conversational question-answering system!")
    print("You can ask any question, and I'll try to provide an answer.")

    while True:
        try:
            with speech_recognition.Microphone() as mic:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                audio = recognizer.listen(mic)

                print("Recongizing...")
                text = recognizer.recognize_google(audio)
                text = text.lower()

                print(f"Recognized {text}")

                # Check for a stop keyword or phrase
                if "stop" in text:
                    print("Stopping the program")
                    break
                #Ask the question and get the response
                response = ask_question(text)
                print("Chatbot:", ", ".join(response))

        except speech_recognition.UnkownValueError:
            print("Could not understand audio")
            continue
        except speech_recognition.RequestError as e:
            print(f"Error:{e}")
            continue
        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__=="__main__":
    main()