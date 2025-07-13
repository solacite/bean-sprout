# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("bean", who_color="#575783")
define s = Character("sprout", who_color="#a6c39b")
define n = Character("narrator", who_color="#606060")
define m = Character("???", who_color="#606060")
define db = Character("Bean's Doppelganger", who_color="#d65656")

# bean: concerned, confused, happy
# sprout: confused, dumb, inquisitive

image bean = "bean.png"
image bean concerned = "bean concerned.png"
image bean confused = "bean confused.png"
image bean happy = "bean happy.png"

image sprout = "sprout.png"
image sprout confused = "sprout confused.png"
image sprout dumb = "sprout dumb.png"
image sprout inquisitive = "sprout inquisitive.png"

transform small:
    zoom 0.8
    xalign 0.5

transform smallright:
    zoom 0.8
    xalign 1.0

transform smallleft:
    zoom 0.8
    xalign 0.0

label clear:
    hide bean
    hide sprout
    hide concerned bean
    hide confused bean
    hide happy bean
    hide confused sprout
    hide inquisitive sprout
    hide dumb sprout
    return

label start:

    play music "vibe.mp3" loop

    scene background

    jump intro


label intro:
    show bean at small
    with dissolve

    n "This is Bean."

    b "Hello :D"

    b "(whispering) I don't know what else to say."

    n "Okay..."

    hide bean

    show sprout at small

    n "This is Sprout."

    s "Hi."

    n "Tell us about yourself, Sprout."

    s "I don't know what to say either..."

    menu:
        "What will you do?"

        "Pressure him into talking":

            show confused sprout at small

            s "..."

        "Say nothing":
            s "Well..."


    s "I go to the same school as Bean, I guess...nothing much..."

    s "And I'm pretty hungry."

    jump out_for_lunch

label out_for_lunch:
    menu:
        "Should Sprout..."

        "Ask Bean out for lunch":

            hide sprout

            s "Alright...I'll do it."

        "Starve":

            show inquisitive sprout at small

            s "This seems like a terrible idea. I'll not listen to you."

    call clear

    show sprout at smallleft
    
    show bean at smallright

    s "Do you want to eat out, Bean?"

    s "..."

    s "...Bean?"

    s "...B-"

    show concerned bean at smallright

    b "I'M TRYING TO FOCUSSAJDLKSFSFAO"

    show inquisitive sprout at smallleft

    s "ON WHAT EXACTLY???"

    b "JENGA?????"

    s "I have so many questions for you..."

    menu:
        "Choose a question."

        "ARE YOU HUNGRY????":

            b "Moderately so."

            s "What is that supposed to mean?"

            b "It means what it means..."

            show dumb sprout at smallleft

            s "???"

        "WHY ARE YOU PLAYING JENGA ALONE????":

            show confused bean at smallright

            b "I'm trying to FOCUS."

            s "THAT DOESN'T ANSWER THE QUESTION??"

            b "BUT IT DOES??"
        
        "WHAT HAPPENED TO STUDYING FOR FINALS????":

            show happy bean at smallright

            b "I gave up."

            s "Loser."

    hide sprout with dissolve

    hide bean with dissolve

    jump after_lunch

label after_lunch:
    n "After coming back from a well-deserved (for Sprout) fast food outing, the two return to their comfort cove."

    n "Or, rather, a rather dead patch of grass bordering their town's park."

    show sprout at smallleft
    with dissolve

    show confused bean at smallright
    with dissolve

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

    show concerned bean at smallright

    b "I'M HUNGRY YOU STUPID KNUCKLEBUNS"

    show inquisitive sprout at smallleft

    s "..."

    menu:
        "Choose a question."

        "WHY THE HELL ARE YOU STILL HUNGRY????":

            show bean at smallright

            b "Smart people eat more."

            s "And where did you hear that from..."

            b "The internet!"

            s "..."

        "WHAT THE HELL IS A KNUCKLEBUNS????":

            show happy bean at smallright

            b "See, you're stupid. It's a part of the vocabulary these days."

            s "These days...?"

            b "You're old."

            s "We're the same age."

            b "Nonetheless. You're still old as hell."

            show bean at smallright

        "WHY THE HELL ARE YOU CALLING ME STUPID????":

            show bean at smallright

            b "I only speak the truth."

            s "You're stupid."

            b "Says the stupid one."

            s "You're stupider."

            b "And you must be the stupidest."

            s "..."

            jump go_home
    
label go_home:
    s "I'm feeling a bit tired. I'll probably go soon."

    show confused bean at smallright

    b "What about me??"

    menu:
        "Choose for Sprout."

        "Take Bean with you":

            show happy bean at smallright

            b "Yippee!!!!"

            s "Don't make me change my mind."

            b "Wasn't going to!"

            s "I'm already regretting it..."

            b "What'd you say?"

            s "Nothing..."

            b "Okay then..."

            s "Let's go. Unless you want to sleep outside."

            b "Fiiiiiiiiiiine."

        "Abandon Bean in the streets":
            b "Noooooooooooooooooooooo"
            
            b "-oooooooooooooooooooooooooooooooooooo-"

            b "-ooooooooooooooooooooooooooooooooooooooooooooooooooo!"

            b "You can't do me like this!"

            show inquisitive sprout at smallleft

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

            show confused bean at smallright

            b "You wanna die???"

            show confused sprout at smallleft

            s "N-"

            b "BET."

            s "I was joking!"

            b "Uh-huh."
    jump cookie_steal

label cookie_steal:

    show bean at smallright

    show sprout at smallleft

    n "Bean is about to say something when-"

    m "Hehehe!"

    show concerned bean at smallright

    show inquisitive sprout at smallleft

    b "HEY! Give that back!"

    m "(unceremoniously skedaddles)"

    show confused sprout at smallleft

    s "What'd they take??"

    b "MY CHOCOLATE CHIP COOKIE!!"

    b "(skedaddles after the mystery figure)"

    show inquisitive sprout at smallleft

    s "That thing is literally worth less than my life savings, and I don't even work a job..."

    default skedaddle = False

    while not skedaddle:
        menu:
            "What should Sprout do?"

            "Run after Bean":
                $ skedaddle = True
                s "I'M COMINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"

            "Stay still":
                s "..."

    s "(skedaddles after bean)"

    jump chase

label chase:
    n "The mystery figure darts down an alleyway, Bean close behind."

    n "There is a low wall at the end of the alley."

    menu:
        "What will Sprout do?"

        "Follow Bean and the mystery figure down the narrow alley.":
            n "The mystery figure struggles for a handhold on the brick wall at the end of the alley, but manages to pull themselves up."

            n "Bean is close behind, hand reaching out for the figure's shoes."

            n "Sprout stands behind Bean, out of breath. He can't progress further because of how narrow the alley is."

            m "You'll never catch me!"

            m "It's MY cookie now-"

            n "Bean grabs the figure's shoes and pulls them down."

            m "Augh-ack-oomf!"

        "Run around the block and intercept the mystery figure.":
            n "Sprout runs as if his life depends on it. It doesn't."

            n "As he turns the corner, a flash of gray appears in front of him and-"

            m "OW!"

            n "The mystery figure body-slams into Sprout from the direction of the alley."

            b "Bro, when did you get there?"

            s "Uhhh."

            n "Sprout is still recovering from the physical shock."

            m "(makes a move to run)"

            b "(grabs the figure) Nuh-uh!"

        jump caught

label fight:
    m "That wasn't very nice!"

    b "Now give it back."

    m "Hmm..."

    n "The mystery figure punches Bean on the side of his face."

    b "Ow!"

    menu:
        "What should they do?"

        "Attack the figure simultaneously":
            b "Ahhhhhh!"

            s "Ahhhhhh!"

            m "AHHHHHH!"

            n "The figure falls after being jumped by Bean and Sprout."

        "Attack the figure one by one":
            b "Ahhhhhh! (punches the figure)"

            m "Ahhhhhh!"

    n "The figure cowers in despair. Bean appears dismayed."

    b "It was that easy?"

    n "Bean takes the cookie from the figure's hands and uncovers their mask."

    b "Wha...huh???"

    db "Hi. I'm Bean."

    b "Why do you look EXACTLY LIKE ME??"

    db "You're me. I'm not you. I'm the real one. I'm-"

    b "THERE CAN ONLY BE ONE!"

    n "Bean proceeds to sucker-punch his doppelganger."

    jump sunset

label sunset:
    #