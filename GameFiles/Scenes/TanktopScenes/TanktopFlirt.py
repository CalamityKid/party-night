def tanktopflirtcontent(player):
    pass


content = """
===
title: TanktopFlirt
tags: Tanktop Flirt
colorID: 0
position: -408,-3536
---
<< if times talked == 0>>
    Maybe test the waters first?
<< if times talked >= 1>>
    << if tanktop Conversation not in memories and tanktop Interest not in memories and tanktop partner not in memories>>
        Maybe you should talk to your partner before you make a move.
    << if Tanktop Conversation or Tanktop partner in memories>>
        You decided you're gonna sit this one out.

    << if Tanktop Interest in memories>> #if youve actually decided youre going after them
        << if Tanktop.timestalked == 1>> 
            Maybe talk a little more first.

        << if Tanktop.timestalked >= 2>> #then you can actually check if yo can flirt, I cap the level each timestalked.
        <<flirtornot = None>> 
          
            << if Tanktop.timestalked == 2>>
                << if Tanktop.flirt >= 4>> #these are the cap texts
                    They seem to be busy talking with their friends about something.
                << elif tanktop.flirt < 4 >>
                    << flirtornot = True>>

            << if Tanktop.timestalked == 3>>
                << if Tanktop.flirt >= 6>>
                    << if pusher Bussiness in memories>>
                        << if flirt < 8>>
                            << flirtornot = True>>
                        <<elif flirt => 8>> #same as timestalked.4
                            Looks like they want to dance.
                    << if pusher Bussiness not in memories and Looking for pusher in memories>> 
                        You don't get through, maybe get a contact first.
                    <<  if pusher Bussiness not in memories and looking for pusher not in memories>>
                        Seems like something's going on with their friends.
                << elif tanktop.flirt < 6>>
                    << flirtornot = True>>

            << if Tanktop.timestalked == 4>>
                << if Tanktop.flirt >= 8>>
                    Looks like they want to dance.
                << elif tanktop.flirt < 8>>
                    << flirtornot = True>>

            << if Tanktop.timestalked == 5>>
                << if Tanktop.flirt >= 10>>

                << if Tanktop Asks not in memories>> 
                    Your partner's all over them. They look so hot together.
                    They lust for you too. They want you all to go home and play.
                    << add Tanktop Asks in Memories>> 
                << if Tanktop Asks in memories>>
                    Do you want to leave the party with the cutie in the tanktop? (y/n)
                    << if yes>>
                        This would end the night, are you sure? (y/n)
                        << if yes>> 
                            << add Tanktop Home to memories >>
                            << RUN ENDGAME()>> 
                        <<if no>>
                            You tell them to wait a little longer.
                            << add Tanktop Asks to memories>>
                    << if no>>
                        << add Tanktop Asks to memories>>
                        You tell them to wait a little longer.


                << elif tanktop.flirt < 10>>
                    << flirtornot = True>>

            << if flirtornot == True>> 
                << result = flirt(Tanktop)>>
                << if result == True>>
                    <<Flirtgoodbark(Tanktop)>>
                    << tanktop.flirt +1>> 
                    [[|FlirtGoodBark(Person)]]
                << if result == False>>
                    <<Flirtbadbark(Tanktop)>>
                    [[|FlirtBadBark(Person) ]]
                    << tanktop.flirt -1>> 
                << time passes>>
 

a point system and the calculation thingy
"""
