from evennia import Command

class CmdSmell(Command):
    """
    Smell - Return a smell set on a character or object. Adds a bit of flavor.
            Please note that this is not meant to be used for tracking, race
            scent, or other 'hard' RP commands. It just adds another bit of
            detail to a character.

    Usage:
        smell [thing]:
            Returns [thing.db.scent] to caller.
    """

    key = "smell"
    aliases = []
    lock = "cmd:all()"
    help_category = "General"

    def func(self):
        caller = self.caller
        args = str(self.args.strip())
        location = self.caller.location

        # Get keyword smells out of the way first.
        # The two main ones are 'me' and 'here'.

        if args.lower() == "here":
            if location.db.scent:
                caller.msg("You smell: {}".format(location.db.scent))
                return
            else:
                caller.msg("You don't smell anything in particular here.")
                return
        elif args.lower() == "me":
            if caller.db.scent:
                caller.msg("Your own scent: {}".format(caller.db.scent))
                return
            else:
                caller.msg("You don't smell like anything! Try 'editaccount' to change this.")
                return

        # Now we have to figure out what we're looking for.
        target = caller.search(args, location=caller.location)
        if target is None:
            return
        else:
            if target.db.scent and target.db.scent != "None":
                caller.msg("You smell: {}".format(target.db.scent))
                target.msg("{} smelled you!".format(caller.name))
                return
            else:
                caller.msg("{} doesn't smell like anything.".format(target.name))
                target.msg("{} smelled you!".format(caller.name))

        return
