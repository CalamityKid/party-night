===
title: TanktopTimes2
tags: Tanktop times2
colorID: 0
position: -632,-3096
---
#One of their friends didn't bring candy, introduce them to the pusher if you can
<< if location == dance floor>> 
    They're busy talking to their group about something.
<< if location != dance floor>> 
    You walk up to their group.
    They're talking to each other about how to get candy
    specifically they could use some pills

    << if pusher in total people>>
        
        Do you wanna introduce them to your new pusher friend?
        It might take some time (y/n).
            << if yes>>
                You look around for your pusher friend.
                << if party is packed. time passes>>
                << change player, partner and cutie in tanktop location to the pushers location>>
                You end up finding them in {player.location} and you introduce them.
                You can tell everybody's pretty happy.
                << Pusher bussiness to memories>> 
                << time passes>> 
                << record the time this happens in a variable>> 
                << make times talked 3>> 

    << if pusher not in total people>>
        You tell them you don't know of anybody in here.
        But you'll let them know if you hear something.
        << add Looking for pusher in memories>> 
        << make times talked 3>> 

        you act as support.
