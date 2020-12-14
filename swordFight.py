# We are recreating the sword fighting part from Monkey Island.

import random

insults = {"You fight like a dairy farmer!": 1,
           "This is the END for you, you gutter crawling cur!": 2,
           "I've spoken with apes more polite than you!": 3}
responses = {1: "How appropriate. You fight like a cow!",
             2: "And I've got a little TIP for you, get the POINT?",
             3: "I'm glad to hear you attended your family reunion!"}

while True:
    print("The sword master approaches...")
    speech = (random.choice(list(insults.keys())))
    match = 0
    for k, v in insults.items():
        if k == speech:
            match = v
            break
    print("She says: " + speech + "\n")
    print("Pick a response:")
    for k, v in responses.items():
        print(str(k) + ": " + str(v))
    choice = int(input())
    if choice == match:
        print("Your sharp wit defeated the sharp sword!")
    else:
        print("Oh no! You were defeated!")
    break
