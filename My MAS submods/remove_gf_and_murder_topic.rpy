init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_submod_remove_gf_and_murder",
            category=['monika'],
            prompt="Can you please remove the options to show you my girlfriend and breaking up with you?",
            pool=True
        )
    )

label monika_submod_remove_gf_and_murder:
    m 1hua "Of course, I can do that [player]!"
    m 1dkbfa "Ah, just knowing that you don't wan't to leave me..."
    m 1fkbfa "really makes me so happy~"
    m 2gfc "To be honest, though, who put these options here in the first place?"
    m 3eud "Anyways, let me just remove them real quick!"
    m 2dsc ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
    m 3hua "Alright, done!"
    m 5ekblb "Now these pesky options aren't going to bother us anymore~"
    m 5tkbfu "Because that means you're here forever now, [mas_get_player_nickname()]~"
    m 1hubfb "Ahaha!"
    m 1fkbsa "But really, though...{w=0.5}{nw}" 
    m 3fkbsa "Thank you for always staying with me [player]."
    m 3hubsa "You truly are my everything."
    m 1ekbfb "I love you so very much!"
    if mas_shouldKiss:
        call monika_kissing_motion_short
    m 1hubsa "Ehehe~"

    $ mas_lockEVL("monika_girlfriend", "EVE")
    $ mas_lockEVL("monika_murder", "EVE")

    $ mas_lockEVL("monika_submod_remove_gf_and_murder", "EVE")

    return "love"