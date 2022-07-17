#the default is 3 uses, in the character setup. If you get the comission from the pusher you get 2 more.

def partnertimes1content(player):


    player.modify_stat("lit", 10, True)

you ask your partner for some k 


if k in active items:
    You just did some, babe
    I'll give you some more later if you want
and that's that for now.
    return False

elif k not in active items:
    if partner.kusesleft == 0:

        I ran out, babe
        I'm sorry
    and it's genuine sadness
    you almost feel bad for asking
    return False

    elif partner.kusesleft > 1:

    << if location = bathroom>> 
        
        << if party is crowded>>
            << if player.stalltimewarning is not True>>
                We're gonna need to go into a stall
                and there's a lot of people waiting.
                It takes a while when the party's this crowded.
                You want to wait? I don't mind...
                << player.stalltimewarning set to True>> 

            It's pretty crowded now, you okay with waiting? (y/n)
                << if yes>>
                    Alright babe, we wait.
                    And you wait like 10 minutes
                    until a stall frees up.
                    You both get in.
                    << use k>>
                    << time passes>> 
                    partner.kusesleft =-1
                    return True

                << if no>> 
                    Okay love. 
                    You tell me if you wanna try later. 
                
        << if party is not crowded>> 
                Great, let's go!
            you go into the stall

            if kusesleft = 1:
                your partner tells you they just gave some to your russian friend
                but you can kill the bag now
                << use k>>
                << time passes>> 
                partner.kuses =-1
                return True
    
    << elif location is not bathroom>>
            Yeah, I could use some freshening up!
        your partner says half smiling
        
        << if player.movementtimewarning is not True>>
            We have to go to the bathroom then. 
            It's a pain. Especially when it's crowded.
            But you gotta do what you gotta do.
            << set player.movementtimewarning to True>>
        
        You really wanna go all the way to the bathroom for this? (y/n)
            << if yes>> 
                << player location changes to bathroom, partner location changes to bathroom>>
                
                << if party is crowded>>
                    Your partner and you slowly make your way to the bathroom.
                    << time passes>> 
            
                << if party is NOT crowded>> 
                    You both find yourselves in the bathroom in no time. 

                return PartnerBorrowK scene (this same scene)

            << if no>> 
                Okay babe, let me know if you change your mind.
                << stop>>