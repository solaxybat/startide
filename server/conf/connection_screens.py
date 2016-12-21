# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets.UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = \
"""{r----------------------------------------------------------------------------{n

Welcome to...

  @@@@@@ @@@@@@@  @@@@@@  @@@@@@@       {b@@@    @@@{n   '{wcon{n <name> <password>'
 !@@     @@@@@@@ @@!  @@@ @@!  @@@      {b@@@    @@@{n      to log in
  !@@!!    @@!   @!@!@!@! @!@!!@!       {b@@!    @@@{n   '{wcon{n guest guest'
     !:!   @@!   !!:  !!! !!: :!!       {b@@!    @@@{n      to log in as guest
 ::.: :    @!!   :   : :  :   : :       {b@!@!@!@!@!{n   '{wcreate{n <name> <pass>'
           @!!   @@@ @@@@@@@  @@@@@@@@  {b@!@!@!@!@!{n      to create a new
           !!:   @@! @@!  @@@ @@!             {b !!!{n      character
           !!:   !!@ @!@  !@! @!!!:!          {b !!!{n
            :    !!: !!:  !!! !!:             {b : :{n   '{wQUIT{n'
            :    :   :: :  :  : :: :::        {b : :{n      logout
                                                     '{wWHO{n'
                                                        find out who is
                                                        online
                                                     '{whelp{n'
                                                        additional info
 
                                                ... a sci-fi roleplaying MUSH

{r-----------------------------------------------------------------------------{n
   Based on "Startide" concept originally created by Corvidae and Drakkon.
   Game {g%s {non Evennia v%s {nas Maintained by Indigo.""" \
 % (settings.SERVERNAME, utils.get_evennia_version())
