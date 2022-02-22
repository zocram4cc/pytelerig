from winreg import HKEY_PERFORMANCE_DATA
import irc.bot
import irc.strings
from threading import Thread, Lock

class RigBot(irc.bot.SingleServerIRCBot):
    stopped = True
    lock = None

    homecommand = 0
    awaycommand = 0

    def __init__(self, channel, nickname, rigger, homenickname, awaynickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.lock = Lock()
        self.channel = channel
        self.rigger = rigger
        self.homepassword = homenickname
        self.awaypassword = awaynickname
    
    def start(self):
        """Start the bot."""
        t = Thread(target=self.run)
        t.start()
        
    def stop(self):
        self.stopped = True

    def run(self):
        self._connect()
        super().start()
        #print("TACCI")


    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        a = e.arguments[0].split(":", 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(
            self.connection.get_nickname()
        ):
            self.do_command(e, a[1].strip())
        return


    def do_command(self, e, cmd):
        #print(self.homepassword, self.awaypassword)
        nick = e.source.nick
        c = self.connection
        splitcmd = cmd.split(" ", 2)
        self.lock.acquire()
        if nick == self.rigger:
            if splitcmd[0] == "home":
                self.updatehomenickname(splitcmd[1])
            elif splitcmd[0] == "away":
                self.updateawaynickname(splitcmd[1])
            elif splitcmd[0] == "current":
                c.notice(nick, "Current managers are: " + self.homepassword + " and " + self.awaypassword)
            elif cmd == "die":
                self.die()
            else:
                c.notice(nick, "Wtf do you mean by " + cmd)
        elif nick == self.homepassword:
            try:
                self.homecommand = int(cmd)
            except ValueError:
                c.notice(nick, "Not a number m8")
        elif nick == self.awaypassword:
            try:
                self.awaycommand = int(cmd)
            except ValueError:
                c.notice(nick, "Not a number m8")
        else:
            c.notice(nick, "You're either not a current manager, or wrote something stupid: " + cmd)
        self.lock.release()


    def retrievehomeinput(self):
        if 0 < self.homecommand < 9:
            returnvalue = self.homecommand
            self.homecommand = 0
            return returnvalue
        else: return 0
    
    def retrieveawayinput(self):
        if 0 < self.awaycommand < 9: 
            returnvalue = self.awaycommand
            self.awaycommand = 0
            return returnvalue
        else: return 0
    
    def retrievehomenickname(self):
        return self.homepassword

    def retrieveawaynickname(self):
        return self.awaypassword

    def updatehomenickname(self, nickname):
        self.homepassword = nickname
    
    def updateawaynickname(self, nickname):
        self.awaypassword = nickname