init python:

    def Action_approval_checks(Girl, Action_type):
        if Action_type == "kiss":
            love_approval = approval_check(Girl, "love", 20)
            trust_approval = approval_check(Girl, "trust", 40)
        elif Action_type == "blowjob":
            love_approval = approval_check(Girl, "love", 50)
            trust_approval = approval_check(Girl, "trust", 50)
        elif Action_type == "sex":
            love_approval = approval_check(Girl, "love", 60)
            trust_approval = approval_check(Girl, "trust", 70)
        elif Action_type == "anal":
            love_approval = approval_check(Girl, "love", 80)
            trust_approval = approval_check(Girl, "trust", 80)

        if love_approval and trust_approval:
            approval = True
        else:
            approval = False

        return approval
