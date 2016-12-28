"""
What-Is XXX is a MUCK-based command allowing specific characters to set a list of 'interests'
    or likes that allow others to find them. As noted by the XXX, this particular version is
    designed primarily for adult interests. As What-Is is a fairly self contained and modular
    bit of code, it is being used as practice in coding.

Usage:
    +wi (or +wixxx):     display an output of all nearby (in the room) players with What-Is
                         information.

    +wi [name]:          display information of character object [name], works at range.

    +wi/set [string]:    Append a list of dictionary keys from [string] to the character's
                         what-is data.

    +wi/clear:           Remove current list of keys.

    +wi/custom [string]: Allows up to 12 characters for a custom field, at the end of the
                         final listing.

    +wi/list:            Display a full list of currently registered keys.
"""

from evennia import CmdSet
from commands.command import MuxCommand
from evennia.utils import evtable

class CmdWixxx(MuxCommand):

    key = "+wi"
    aliases = ["+wixxx", "wi", "wixxx"]
    lock = "cmd:all()"
    help_category = "General"

    # Dictionary List for different flags. Edit this to create/ remove flags.

    wiData = {
        '!': 'no',
        'a': 'available',
        'ag': 'anything-goes',
        'age': 'ageplay',
        'an': 'anal',
        'ap': 'avian-preferred',
        'aq': 'aquatic',
        'bi': 'bisexual',
        'bit': 'biting',
        'blo': 'blood',
        'bod': 'body-modification',
        'cmc': 'cum-covered',
        'cml': 'cum-loving',
        'cok': 'cock-worpshipping',
        'con': 'consensual-only',
        'crx': 'crossdresser',
        'cws': 'cunt-worshipping',
        'd': 'dominant',
        'dia': 'diapers',
        'dir': 'dirty-talk',
        'dis': 'disobediant',
        'dsc': 'discipline',
        'dye': 'dyes',
        'edi': 'edible',
        'el': 'electrical',
        'ema': 'emasculation',
        'en': 'enema',
        'ex': 'exhibitionist',
        'exp': 'experienced',
        'fe': 'female-biased',
        'fea': 'fear',
        'ff': 'foot-fetish',
        'fmz': 'feminization',
        'fp': 'fur-preferred',
        'fsh': 'forcedshifting',
        'fst': 'fisting'
    }

    def func(self):

        # Start the fun..

        caller = self.caller
        args = self.args.strip()
        switch = next(iter(self.switches or []), None)

        # Build the output string header

        output = "{R.-< {CWhat-Is XXX{R >-"
        output = output.ljust(76, '-')
        output += ".{n\r"

        # If the switch is /list we can ignore everything else...

        if switch == "list":
            result = "Flags and Meanings:\n"
            for i in self.wiData:
                result += i + ":" + self.wiData[i] + ", "
            result += "\n"

            self.caller.msg(output)
            self.caller.msg(result)

            return

        # If the switch is /clear then we just remove the flag property

        elif switch == "clear":
            result = "Clearing Set Flags...\n"
            caller.db.widat = ""
            self.caller.msg(output)
            self.caller.msg(result)
            return

        # The /custom switch just grabs the first 12 characters of the arg
        # and turns it into a data field.

        elif switch == "custom":
            result = "Setting a custom string...\n"
            string = args[:13]
            result += '\t"' + string + '"\n'
            caller.db.widatcust = string
            self.caller.msg(output)
            self.caller.msg(result)
            return

        # Set a list of keys by appending them to caller.db.widat

        elif switch == "set":
            result = "Adding flags...\n"

            # Quietly sanitize by ignoring anything not a key.

            for i in args.split():
                if i in self.wiData:
                    result += self.wiData[i] + " "
                    caller.db.widat += i + " "

            result += "\nFor a list of: "
            for i in caller.db.widat.split():
                result += self.wiData[i] + " "

            self.caller.msg(output)
            self.caller.msg(result)
            return

        elif not switch:

            # No switch found, this means we want an output.
            # Check if we want a specific output.
            if args:
                # Alright, time to set up a table...
                result = evtable.EvTable("Name","Result", width=74, align="l", border="none")
                for i in args.split():
                    target = caller.search(i, global_search=True)
                    if target:
                        # Expand the list of the target.
                        wi_result = ""
                        basics = ""
                        if target.db.widat:
                            for k in target.db.widat.split():
                                wi_result += self.wiData[k] + " "
                        if target.db.widatcust:
                            wi_result += caller.db.widatcust
                        if not target.db.widat and not target.db.widatcust:
                            wi_result = "No WI info set. "
                        if target.db.sex:
                            wi_result += " " + target.db.sex
                        if target.db.race:
                            wi_result += " " + target.db.race
                        else:
                            wi_result += " Unknown"
                        result.add_row(target.name,wi_result)
                    else:
                        result.add_row(i, "Character not found.")

                self.caller.msg(output)
                self.caller.msg(result)
                return

            else:
                # No args. Just give the room.
                result = evtable.EvTable(table=["Name","result",""], border="none")
                for i in caller.location.contents():
                    wi_result = ""
                    basics = ""

                    if i.db.widat:
                        for k in i.db.widat.split():
                            wi_result += self.wiData[k] + " "
                    else:
                        wi_result = "No WI info set. "
                    if i.db.sex:
                        basics += i.db.sex + " "
                    if i.db.race:
                        basics += i.db.race
                    else:
                        basics += "Unknown"
                    result.add_row([i.name.capitilize(),wi_result,basics])
                self.caller.msg(result)
                return

            self.caller.msg(output)
            return

        else:
            output += "I didn't understand that switch."
            self.caller.msg(output)
            return















