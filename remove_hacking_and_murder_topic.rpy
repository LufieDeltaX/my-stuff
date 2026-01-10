init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_submod_remove_hacking_and_murderer",
            category=['monika'],
            prompt="Can you please remove the options to call you a murderer and hacker?",
            pool=True
        )
    )

label monika_submod_remove_hacking_and_murderer:
    m 1hua "Of course, I can do that [player]!"
    m 2gkc "Hmm, why are these options here in the first place?"
    m 3eud "Anyways, just let me remove them already!"
    m 2dsc ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"
    m 3hua "Alright, done!"
    m 5eub "Now these stupid options aren't going to bother us anymore."
    m 1hubsa "Ehehe~"

    $ mas_lockEVL("monika_hack", "EVE")
    $ mas_lockEVL("monika_justification", "EVE")

    $ mas_lockEVL("monika_submod_remove_hacking_and_murderer", "EVE")

    return