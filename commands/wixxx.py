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
from evennia.utils.evtable import EvTable, fill

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
        'ap': 'avian-preferred'
    }

    def func(self):

        # Start the fun..

        caller = self.caller
        args = self.args.strip()
        switch = next(iter(self.switches or []), None)

        # Build the output string header

        output = "{R.-< {CWhat-Is XXX{R >-"
        output = output.ljust(38, '-')
        output += ".{n\r"

        # If the switch is /list we can ignore everything else...

        if switch == "list":
            output += "Flags and Meanings:\n"
            for i in self.wiData:
                output += i + ": " + self.wiData[i] + " "
            output += "\n"
            self.caller.msg(output)

            return

        # If the switch is /clear then we just remove the flag property

        elif switch == "clear":
            output += "Clearing Set Flags...\n"
            caller.db.widat = ""

            self.caller.msg(output)
            return

        # The /custom switch just grabs the first 12 characters of the arg
        # and turns it into a data field.

        elif switch == "custom":
            output += "Setting a custom string...\n"
            string = args[:13]
            output += '\t"' + string + '"\n'
            caller.db.widatcust = string
            self.caller.msg(output)
            return

        # Set a list of keys by appending them to caller.db.widat

        elif switch == "set":
            output += "Adding flags...\n"

            # Quietly sanitize by ignoring anything not a key.

            for i in args.split():
                if i in self.wiData:
                    output += self.wiData[i] + " "
                    caller.db.widat += i + " "

            output += "\nFor a list of: "
            for i in caller.db.widat.split():
                output += self.wiData[i] + " "

            self.caller.msg(output)
            return

        elif not switch:

            # No switch found, this means we want an output.
            # Check if we want a specific output.
            output += " ".join(switch)
            self.caller.msg(output)
            return

        else:
            output += "I didn't understand that switch."
            self.caller.msg(output)
            return















