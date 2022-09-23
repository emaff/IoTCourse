import signal


class GracefulKiller:
    def __init__(self):
        self.__kill_now__ = False
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.__kill_now__ = True
        print("EXITING GRACEFULLY!!!!!!!!!!!!!!!!!!!")

    def is_killed(self):
        return self.__kill_now__