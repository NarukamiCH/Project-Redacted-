label recent_Action_reactions(Girl, Action_type):
    # call recent_Action_lines(Girl, Action_type)

    return

label daily_Action_reactions(Girl, Action_type):
    # call daily_Action_lines(Girl, Action_type)

    return

label first_time_asking_reactions(Girl, Action_type):
    # call first_time_asking_lines(Girl, Action_type)

    return

label first_approval_reactions(Girl, Action_type):
    # call first_approval_lines(Girl, Action_type)

    return

label Action_accepted(Girl, Action_type):
    # call accepted_without_question_lines(Girl, Action_type)
    call Action_accepted_changes(Girl, Action_type)

    return

label Action_rejected(Girl, Action_type):
    # if Girl.History.check(f"no_{Action_type}", tracker = "daily"):
    #     call Action_already_rejected_lines(Girl, Action_type)
    # elif Girl.History.check(Action_type):
    #     call previous_Action_rejected_lines(Girl, Action_type)
    # else:
    #     call otherwise_not_interested_lines(Girl, Action_type)

    $ Girl.History.update(f"no_{Action_type}")

    return