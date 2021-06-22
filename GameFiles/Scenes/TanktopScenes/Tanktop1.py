#this node is basically a reaffirmation of the partner choose-your-path node


<< if tanktop Conversation not in memories and tanktop Interest not in memories and tanktop partner not in memories>>
    Maybe you should talk to your partner before you make a move.

<< if tanktop Conversation in memories or tanktop Interest in memories or tanktop partner in memories>>
    You search around the room and make eye contact
    and they do this thing, between a smile and biting their lip
    Yeah...

    You walk up to their group and you smile
    << if Tanktop Conversation in memories>>
        as harmlessly as you can
        the way you'd smile to a family member
            
        You can tell they notice.
    
    << if Tanktop Interest in memories>>
        a devilish smile
        you really put some weight behind it 
        
        it works.
        << tanktop.flirt += 2>> 

    << if Tanktop partner in memories>>
        pretty harmlessly, you lay back
        and your partner takes over 

        you act as support.

    << if location != dance floor>> 
        You talk a bit about how the party's going
        apparently whoever was supposed to get their candy didn't show up
    << if location == dance floor>>
        You half shout half sign language over the music
        looks like whoever was supposed to get their candy didn't show up

    They're all pretty upset about it
    << time passes>>
    << times talked == 2>>
    << >>
