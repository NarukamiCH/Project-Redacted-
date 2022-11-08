init python:

    def register_Events():
        Events = [
            chapter_one_conversation_A(),
            chapter_one_conversation_B(),
            chapter_one_news_story_A(),
            chapter_one_news_story_B(),
            chapter_one_news_story_C(),
            chapter_one_finale(),
            
            caught_changing(),
            caught_showering()]

        for C in Cast:
            if renpy.has_label(f"all_{C}_Events"):
                Character_Events = renpy.call_in_new_context(f"all_{C}_Events")

                if Character_Events:
                    for Event in Character_Events:
                        Events.append(Event)

        for Event in Events:
            EventScheduler.add_Event(Event)

        return
