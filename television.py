class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def __str__(self) -> str:
        """
        Method to print television status, channel value, and volume value
        :return: television status, channel value, and volume value
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume * (not self.__muted)}"

    def power(self) -> None:
        """
        Method to toggle television status
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to mute and unmute television
        """
        if(self.__status):
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase channel value by 1
        """
        if (self.__status):
            if(self.__channel == Television.MAX_CHANNEL):
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to decrease channel value by 1
        """
        if (self.__status):
            if(self.__channel == Television.MIN_CHANNEL):
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to increase volume value by 1
        """
        if (self.__status):
            if(self.__muted):
                self.mute()
            if (self.__volume == Television.MAX_VOLUME):
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease volume value by 1
        """
        if (self.__status):
            if (self.__muted):
                self.mute()
            if (self.__volume == Television.MIN_VOLUME):
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1