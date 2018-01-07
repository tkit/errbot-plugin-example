from errbot import BotPlugin, botcmd, re_botcmd
import re

class Example(BotPlugin):
    """Example plugin for Errbot"""

    # basic command
    @botcmd
    def hello(self, msg, args):
        """Say hello to the world"""
        return "Hello, world!"

    # like robot.respond
    def callback_mention(self, message, mentioned_people):
        for identifier in mentioned_people:
            self.send(message.frm, 'User %s has been mentioned' % identifier)

        if self.bot_identifier in mentioned_people:
            self.send(message.frm, 'Errbot has been mentioned !')

    # like hubot.respond
    @re_botcmd(pattern=r"^(([Cc]an|[Mm]ay) I have a )?cookie please\?$")
    def hand_out_cookies(self, msg, match):
        yield "Here's a cookie for you, {}".format(msg.frm)
        yield "/me hands out a cookie."

    # like robot.hear
    @re_botcmd( pattern=r"(^| )cookies?( |$)", prefixed=False, flags=re.IGNORECASE)
    def listen_for_talk_of_cookies(self, msg, match):
        """Talk of cookies gives Errbot a craving..."""
        return "Somebody mentioned cookies? Om nom nom!"

    # like hubot.hear
    def callback_message(self, message):
        if message.body.find('cookie') != -1:
            self.send(
                message.frm,
                "What what somebody said cookie!?",
            )

    # like robot.brain
    @botcmd
    def remember(self, msg, args):
        self['TODO'] = args

    @botcmd
    def recall(self, msg, args):
        return self['TODO']
