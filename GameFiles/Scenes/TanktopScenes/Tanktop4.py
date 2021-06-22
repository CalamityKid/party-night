===
title: TanktopTimes4
tags: tantop times4
colorID: 0
position: -626,-2647
---
#Candy's kicked in now, you have to dance with them to jump to 5, if not on dance floor you can get a cigarette, maybe flirt and they go to the dance floor again

<< if location == dancefloor>>
    You approach the cutie in the tanktop's group of friends
    and they're all really getting down to the music.
    You can't really talk, they're all movement.

<< If location != Dance floor >> 
    You approach the cutie in the tanktop's group of friends.
    The cutie's smoking a cigarette, most of them are.
    They offer you one.
    Do you want a cigarette? (y/n)
    << space>> 
    << if yes>>
        << add cigarette to inventory>>
        You take a cigarette from them.
    <<if no>>
        You kindly refuse.
    
        << if Tanktop Conversation in memories>>
            You can feel your partner holding back.

        << if Tanktop Interest in memories>>
            You talk about random stuff.
            Things seem more interesting when a cutie's talking.
            You get some compliments in.
            << random 3>>
            << if 1>>
                You focus on the way they play with their cigarette.
            << if 2>>
                You focus on that beautiful smile. 
            << if 3>> 
                You love how your partner is really going for it.
            << cutie.flirt +2>>

        << if Tanktop partner in memories>>
                Your partner gets some sexy energy into the conversation.
                There's chemistry for sure.
    
    When everybody's done with their cigarette they go back to the dance floor.
    << time passes>>
    << change tanktop locaton to dance floor>>
