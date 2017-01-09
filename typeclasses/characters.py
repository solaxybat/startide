"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
import time
from evennia import DefaultCharacter
from commands.assist import header, footer, csex

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(player) -  when Player disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Player has disconnected" 
                    to the room.
    at_pre_puppet - Just before Player re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "PlayerName has entered the game" to the room.

    """
    def at_object_creation(self):
        super(Character, self).at_object_creation()

        self.db.xp = 0
        self.db.time_played = 0.0
        self.db.lastConnect = time.time()
        self.db.lastDisconnect = time.time()
        self.db.lastIP = ""


    def return_appearance(self, looker):
        """
        This formats a description. It is the hook a 'look' command
        should call.

        Args:
            looker (Object): Object doing the looking.
        """
        if not looker:
            return
        # Variable set up.
        name = self.get_display_name(looker)
        desc = self.db.desc
        contents = (con for con in self.contents if con != looker and con.access(looker, "view"))

        # Title of screen.
        string = header("Character: {}".format(name))
        # Current pose.
        string += "\n\n{}".format(desc) if desc else "\nA nebulous concept."
        """
        # Can't quite figure out how to parse this (yet).
        if len(contents) > 0:
            string += "\n\nCarrying: "
            for con in contents:
                string += con.get_display_name(looker) + ", "
        """
        string += "\n\n"
        string += footer()

        return string

    def at_post_puppet(self):
        """
        Called just after puppeting has been completed and all
        Player<->Object links have been established.
        Note:
            You can use `self.player` and `self.sessions.get()` to get
            player and sessions at this point; the last entry in the
            list from `self.sessions.get()` is the latest Session
            puppeting this Object.

        Overriding default to allow for tracking connection time.
        """
        self.db.lastConnect = time.time()
        self.msg("\nYou become {c%s{n.\n" % self.name)
        self.msg(self.at_look(self.location))

        def message(obj, from_obj):
            obj.msg("%s has entered the game." % self.get_display_name(obj), from_obj=from_obj)
        self.location.for_contents(message, exclude=[self], from_obj=self)

    def at_post_unpuppet(self, player, session=None):
        """
        We stove away the character when the player goes ooc/logs off,
        otherwise the character object will remain in the room also
        after the player logged off ("headless", so to say).
        Args:
           player (Player): The player object that just disconnected
                            from this object.
           session (Session): Session controlling the connection that
                              just disconnected.

        Overriding default to allow for tracking disconnection time.
        Also changing behavior to -not- store the character object.
        Hiding characters will be done at the room level based on active session.
        """
        # Update Time Played.
        sessions = self.sessions.get()
        session = sessions[0] if sessions else None

        # Update last HOST for tracking purposes.
        self.db.lastIP = session.address
        self.db.lastDisconnect = time.time()
        # Actual time - time connected.
        self.db.time_played += time.time() - session.conn_time

        if not self.sessions.count():
            # only remove this char from grid if no sessions control it anymore.
            if self.location:
                def message(obj, from_obj):
                    obj.msg("%s has left the game." % self.get_display_name(obj), from_obj=from_obj)
                self.location.for_contents(message, exclude=[self], from_obj=self)
                self.db.prelogout_location = self.location
                # Override the 'storage' mechanism.
                # self.location = None

