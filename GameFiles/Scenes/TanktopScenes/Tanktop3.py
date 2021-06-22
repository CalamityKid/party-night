===
title: TanktopTimes3
tags: tanktop times3
colorID: 0
position: -632,-2866
---
#Youre either looking for the pusher and stuck here or already introduced and have to wait for an hour to get to 4

You walk up to the cutie in the tanktop.
<< if looking for pusher in memories and pusher bussiness not in memories>>

    <<  if pusher not in total people>>
        Their whole group is pretty low morale.
        
        << if Tanktop Conversation in memories>>
            Maybe try to get a contact for them.
        << if Tanktop Interest in memories>>
            You try to lift the mood up a bit 
            but conversation ends up being about 
            what a great time they'd be having if their friend showed up.
        << if Tanktop partner in memories>> 
            Your partner tries to lift up the mood a bit
            but it seems like the conversation always goes back to 
            what a great time they'd be having if their friend showed up.
    << if pusher in total people>>
        
        Do you wanna introduce them to your new pusher friend?
        It might take some time (y/n).
            << if yes>>
                You look around for your pusher friend.
                << if party is packed. time passes>>
                << change player, partner and cutie in tanktop location to the pushers location>>
                You end up finding them in {player.location} and you introduce them.
                You can tell everybody's pretty happy.
                << player.cool +=30 >> 
                << Pusher bussiness to memories>> 
                << remove looking for pusher from memories>> 
                << record time in variable tanktop.capeo>> 
                << time passes>> 

<< if pusher business in memories>> 
    The saviors of the night!
    the whole group's really happy with you two
     
    << if Tanktop Conversation in memories>>
        Your partner gives you this we're missing out look.
        You're in for a talk after this for sure.

    << if Tanktop Interest in memories>>
        The cutie in the tanktop is in way better spirits
        flirting game's back on point too
        
    << if Tanktop partner in memories>>
        Everybody's in better spirits
        Your partner flirting is hitting home too
    
    << if tanktop.capeo is less than an hour>>
        They're excited for the candy to kick in.
    << if tanktop.capeo is more than an hour>>
        They're looking pretty lively. Looks like the candy kicked in.
        << make times talked4>> 

        << make times talked 4>>