import random

Rgreet = "Hello! How can i help?"
Rbye = "Goodbye!"
Raskhow = "I am fine. Thank you for asking!"
Rwelc = "You are welcome!"
Rsure = "Sure! You can ask me!"

#science responses
Rsci1a = "Jupiter!"
Rsci1b = "It is the largest planet in our solar system!"

Rsci2a = "Carbon dioxide!"
Rsci2b = "It is a gas that plants take in to make their food!"

Rsci3a = "Nectar!"
Rsci3b = "It is what bees collect from flowers to make honey!"

Rsci4 = "Eight!"

Rsci5a = "Photosynthesis!"
Rsci5b = "It is the process by which plants make their own food by using sunlight!"

Rsci6a = "Nucleas!"
Rsci6b = "It is the center of an atom!"

Rsci7a = "Gravity!"
Rsci7b = "It is the force that pulls objects towards Earth!"

Rsci8a = "Nitrogen!"
Rsci8b = "It is the main gas found in the air we breathe!"

Rsci9a = "Mars!"
Rsci9b = "It is the planet known as the \"Red Planet\"!"

Rsci10 = "100 degrees Celsius!"

Rsci11a = "The Roots!"
Rsci11b = "It is the part of the plant that absorbs nutrients from the soil!"

Rsci12a = "Ice!"
Rsci12b = "It is the solid form of water!"

Rsci13a = "A Geologist!"
Rsci13b = "This is a scientist that studies rocks!"

Rsci14 = "Eight planets!"

Rsci15a = "A Cell!"
Rsci15b = "It is the smallest unit in life!"

Rsci16a = "It is H2O!"
Rsci16b = "It is the chemical symbol for water!"

Rsci17a = "The Sun!"
Rsci17b = "That is the closest star to Earth!"

Rsci18a = "Herbivores!"
Rsci18b = "These are animals who only eat plants!"

Rsci19 = "There are 206 bones in the adult human body1"

Rsci20a = "Lungs!"
Rsci20b = "These are the organs used for breathing!"


#No response available responses

def NotAvail():
    responseNotAv = ["I don't quite understand, could you try again?? ",
                "Not sure, can you ask another question?",
                "I don't think i can help you with that, ask me another question!",
                "I don't know what that means, could you ask me another question?",
                "I don't have an answer to that question, want to try again?"][
        random.randrange(5)]
    return responseNotAv
