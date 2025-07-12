# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("bean")
define s = Character("sprout")
define n = Character("narrator")
# bean: concerned, confused, happy
# sprout: confused, dumb, inquisitive


label start:


    scene background

    show bean

    n "This is Bean."

    b "Hello :D"

    b "(whispering) I don't know what else to say."

    n "Okay..."

    hide bean

    show sprout

    n "This is Sprout."

    s "Hi."

    n "Tell us about yourself, Sprout."

    s "I don't know what to say either..."

    menu:
        "What will you do?"

        "Pressure him into talking":

            show confused sprout

            s "..."

            hide confused sprout

        "Say nothing":
            s "Well..."


    s "I go to the same school as Bean, I guess...nothing much..."

    s "And I'm pretty hungry."

    menu:
        "Should Sprout..."

        "Ask Bean out for lunch":
            s "Alright...I'll do it."

        "Starve":

            show inquisitive sprout

            s "This seems like a terrible idea. I'll not listen to you."

            hide inquisitive sprout

    hide sprout

    show sprout at left
    
    show bean at right

    s "Do you want to eat out, Bean?"

    s "..."

    s "...Bean?"

    s "...B-"

    show concerned bean at right

    b "I'M TRYING TO FOCUSSAJDLKSFSFAO"

    show inquisitive sprout at left

    s "ON WHAT EXACTLY???"

    b "JENGA?????"

    s "I have so many questions for you..."

    hide inquisitive sprout

    menu:
        "Choose a question."

        "ARE YOU HUNGRY????":

            hide concerned bean

            b "Moderately so."

            s "What is that supposed to mean?"

            b "It means what it means..."

            show dumb sprout at left

            s "???"

            hide dumb sprout

        "WHY ARE YOU PLAYING JENGA ALONE????":

            hide concerned bean

            show confused bean at right

            b "I'm trying to FOCUS."

            s "THAT DOESN'T ANSWER THE QUESTION??"

            b "BUT IT DOES??"

            hide confused bean
        
        "WHAT HAPPENED TO STUDYING FOR FINALS????":

            hide concerned bean

            show happy bean at right

            b "I gave up."

            s "Loser."

            hide happy bean

    hide sprout with dissolve

    hide bean with dissolve

    n "After coming back from a well-deserved (for Sprout) fast food outing, the two return to their comfort cove."

    n "Or, rather, a rather dead patch of grass bordering their town's park."

    show sprout at left

    show confused bean at right

    b "..."

    b "......"

    b "........."

    s "Spit it out."

    b "Ew, no."

    s "No, I mean...what do you want to say?"

    b "..."

    s "Well?"

    b "I'm..."

    s "You're...?"

    show concerned bean at right

    hide confused bean

    b "I'M HUNGRY YOU STUPID KNUCKLEBUNS"

    show inquisitive sprout at left

    s "..."

    hide inquisitve sprout

    menu:
        "Choose a question."

        "WHY THE HELL ARE YOU STILL HUNGRY????":

            show bean at right

            hide concerned bean

            b "Smart people eat more."

            s "And where did you hear that from..."

            b "The internet!"

            s "..."

        "WHAT THE HELL IS A KNUCKLEBUNS????":

            show happy bean at right

            hide concerned bean

            b "See, you're stupid. It's a part of the vocabulary these days."

            s "These days...?"

            b "You're old."

            s "We're the same age."

            b "Nonetheless. You're still old as hell."

            hide happy bean

        "WHY THE HELL ARE YOU CALLING ME STUPID????":

            show bean at right

            hide concerned bean

            b "I only speak the truth."

            s "You're stupid."

            b "Says the stupid one."

            s "You're stupider."

            b "And you must be the stupidest."

            s "..."
    
    s "I'm feeling a bit tired. I'll probably go soon."

    show confused bean at right

    b "What about me??"

    menu:
        "Choose for Sprout."

        "Take Bean with you":

            show happy bean at right

            b "Yippee!!!!"

            s "Don't make me change my mind."

            b "Wasn't going to!"

            s "I'm already regretting it..."

            b "What'd you say?"

            s "Nothing..."

            b "Okay then..."

        "Abandon Bean in the streets":
            b "Noooooooooooooooooooooo"
            
            b "-oooooooooooooooooooooooooooooooooooo-"

            b "-ooooooooooooooooooooooooooooooooooooooooooooooooooo!"

            b "You can't do me like this!"

            show inquisitive sprout at left

            s "What if I can?"

            b "Can't!"

            s "Can too."

            b "CAN'T!"

            s "Yuh huh."

            b "NUH UH! LET ME IN!!!!"

            s "Stop being weird."

            b "IT'S INHERENT!!!! LET ME BE ME!!!!"

            s "I said I can't bring you home."

            b "Why is that??"

            s "'Cause I said so."

            b "That's not fair."

            s "Life isn't fair."

            b "Hmph!"

            s "Bye now."

            b ">:("

        "Knock over Bean's Jenga tower and then leave":

            show confused bean at right    

            b "You wanna die???"

            show confused sprout at left

            s "N-"

            b "BET."

    return
