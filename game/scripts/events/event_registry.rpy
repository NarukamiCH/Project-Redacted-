init python:

    def register_Events():
        Events = [
            chapter_one_conversation_A(),
            chapter_one_conversation_B(),
            chapter_one_news_story_A(),
            chapter_one_news_story_B(),
            chapter_one_news_story_C(),
            chapter_one_finale(),

            Rogue_exam(),
            Rogue_study(),
            Rogue_blew_off(),

            Laura_meeting(),
            Laura_workout(),
            
            caught_changing(),
            caught_showering()]

        for Event in Events:
            EventScheduler.add_Event(Event)

        return
