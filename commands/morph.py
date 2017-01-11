"""
EvMorph, a multidesc+ program designed to store entire sets of data
for a form! Please note that this is designed for social RP and can
break some things if shifting/ forms require some kind of system check.
This won't care! Based off of morph hammer by Triggur. Adapted for
Evennia by Indigo@Startide
"""

from commands.command import MuxCommand
from evennia.utils import evmenu
from evennia.utils import evtable
from assist import header, footer, sysemit

# List of db attributes to capture for each morph.
morph_attrs = ("desc",
               "sex",
               "race",
               "fullname",
               "scent",
               "widat",
               "widatcust")

class CmdMorph(MuxCommand):
    """
    EvMorph is a multidesc style program designed to allow the storage and
    retrieval of multiple character attributes per 'form'. It is capable of
    storing any attribute that it has a key for. You set a form by having
    the attributes where you like them, then 'add' that morph to the list to
    save it.

    Usage:
        morph:            provides a list of morphs that are already saved.

        morph [name]:     change into morph name. This will over write what is
                          on the character with what is stored in the morph.
                          That data WILL be lost.

        morph/add:        grabs current attributes, and prompts for a name to
                          use for the form. If that name is already taken, you
                          will have an option to overwrite that data.

        morph/del [name]: This will delete the named morph from your morph data.
                          Please note that this cannot be reversed!

    Morph data is stored as a dict of dicts.
    """

    key = "morph"
    aliases = ["+morph"]
    lock = "cmd.all()"
    help_category = "General"

    def func(self):
        caller = self.caller
        args = self.args.strip()
        switch = next(iter(self.switches or []), None)

        #Initialize the character's db attribute if it isn't there.
        if not caller.db.morph:
            caller.db.morph = {}

        # Handle switches. These are all passed onto other functions.
        if switch == "add":
            evmenu.get_input(caller, "Enter a one word label for this morph (12 Chars or less).", addMorph)
            return
        elif switch == "del":
            if args in caller.db.morph.keys():
                del caller.db.morph[args]
                sysemit(caller, "Morph {} deleted.".format(args))
                return
            else:
                sysemit(caller, "No morph by the name {} found to delete.".format(args))
                return
        elif switch is not None:
            sysemit(caller, "Switch {} not understood.".format(switch))
            return

        # Now to morph or not to morph?
        if args:
            if args in caller.db.morph.keys():
                # We're morphing. Unpack.
                attr_dict = caller.db.morph[args]
                for attr in attr_dict.keys():
                    setattr(caller.db, attr, attr_dict[attr])
                sysemit(caller, "Morphed to {}.".format(args))
                return
            else:
                # Not a valid morph.
                sysemit(caller, "Morph '{}' not found.".format(args))
                return
        else:
            caller.msg(header("Morph"))
            table = evtable.EvTable("|gKey:|n", "|cDescription:|n", width=74, align="l", valign="t", border="none")
            table.reformat_column(0, width=14)
            for name in caller.db.morph.keys():
                unpack = caller.db.morph[name]
                table.add_row("|G" + name + "|n", "|C" + unpack.get("mdesc", "none") + "|n")
            caller.msg(table)
            caller.msg(footer())
            return


def addMorph(caller, prompt, result):
    args = result.strip()
    args = args[:12]

    # Do we already have this key used?
    if args in caller.db.morph.keys():
        sysemit(caller, "The morph name '{}' already in use!".format(args))
        return
    else:
        caller.ndb.mname = args
        evmenu.get_input(caller, "Enter a short description for this form (32 chars or less):", descMorph)
        return True

def descMorph(caller, prompt, result):
    args = result.strip()
    args = args[:32]
    # Lets start storing!
    attr_list = {}
    for attr in morph_attrs:
        attr_list[attr] = getattr(caller.db, attr)
    attr_list["mdesc"] = args
    caller.db.morph[caller.ndb.mname] = attr_list
    del caller.ndb.mname
    sysemit(caller, "The morph '{}' stored. Use with 'morph {}'.".format(args, args))
    return


