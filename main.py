from time import *
import random as r


def speedtest(time1,time2,testinput):
    testd = time2 - time1
    time_in_minutes = testd / 60
    words_typed = len(testinput.split())
    speed = words_typed / time_in_minutes
    return round(speed)
def accu(test1, testinput):

        reference_words = test1.split()
        input_words = testinput.split()

        total_words = len(reference_words)
        total_input_words = len(input_words)
        correct_words = sum(1 for ref_word, input_word in zip(reference_words, input_words) if ref_word == input_word)


        if total_words == 0 or total_input_words == 0:
            return 0
        else:
            accuracy_percentage = (correct_words / total_input_words) * 100
            return accuracy_percentage

def get_custom_text():
    print("Enter your custom text for typing test:")
    custom_text = input()
    return custom_text

test = ["A narrative paragraph which tells a story of a certain event. A descriptive paragraph which gives details about a person, place thing or idea. An expository paragraph which explains something,"
       , "The word paragraph comes from the Latin word paragraphos, which is roughly translated to mean a short stroke marking a break. A paragraph is a group of sentences that share a common topic or idea.",
        "How many sentences are in a paragraph? It is important to note that there is a great deal of variety in how long a paragraph is and there is not a minimum or maximum number of sentences that it must have to fit its definition. "]
test1= r.choice(test)
print("   TYPING SPEED    ")

custom_input = input("Do you want to input custom text? (yes/no): ")
if custom_input.lower() == "yes":
    test1 = get_custom_text()

print(test1)
time1 = time()
testinput=input("ENTER: ")
time2 =time()
speed=speedtest(time1,time2,testinput)
print("SPEED :",speed,"w/min")

acc = accu(test1, testinput)
print("ACCURACY: {}%".format(round(acc)))
if speed > 5 and acc > 90:
    print("Excellent!")
elif speed > 3 and acc > 80:
    print("Good job!")
else:
    print("Practice more!")

