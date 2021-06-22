===
title: TanktopTimes5
tags: Tanktop times5
colorID: 0
position: -622,-2416
---
#Already danced with them and have the boost. Get the Link and sex thing depending on the path (or your partner hooking up with them).
<< if Tanktop Link in memories and flirt >= 10>>
    << run cutie.flirt>>

<< if Tanktop Link in memories and flirt < 10>>
    You've really made a connection with this cutie tonight.
        << if Tanktop Conversation in memories>>
            Your partner's gonna want to talk about this later for sure.
        << if Tanktop Interest in memories>>
            You think they might come home with us tonight
            if you step we our flirt game up.
        << if Tanktop partner in memories>>
            << if Partner hookup not in memories>>
                Your partner gives you this we-gotta-talk look.
            << if Partner hookup in memories>>
                Your partner's even happier about it.
            
<< if Tanktop Link not in memories>>
    << if location == dancefloor>>
        The cutie in the tanktop catches you looking and comes to you.
        They take you to a more quiet spot.
    
    You sweethearts have really made my night.
    << if Tanktop Partner in memories>>
        Especially you, sexy
        they say to your partner with a wink
    It's been very special.
    I hope we can keep hanging out.
    you end up exchanging phone numbers and instagram accounts
    you speak a bit longer and go back to the dance floor.
    << add Tanktop Link to memories>>
    <<time passes>>