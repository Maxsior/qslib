import tkinter as tk

''' I '''
qs = qslib.System()
qs.closed = True
qs.queue = 5
cs = qslib.ChannelSet(relation='distribute')
cs.createChannels(4, mu=1)
qs.append(cs)
qs.createInput(v=1, lambda_=3)
qs.get_p0()
sample_of_visitors = [1, 2, 2, 3, 1, 2, 3]  # выборка частот прихода клиентов
qs.createInput(sample_of_visitors)
qs.get_n_queue()


''' II '''
qs = qslib.QS(closed=False, queue=1, channels=1, channel_relation="isolate")
qs.get_p0(lambda_=1, mu=2)


''' III '''
qs = qslib.create_closed_with_queue(
    sample_of_visitors,
    channels=3,
    queue=5,
    output=3
)
qs["probabilities"][0]
qs["numbers"]["queue"]


if __name__ == "__main__":
    root = tk.Tk()



import tkinter as tk


class QS(tk.Tk):
    def __init__(self, channels: int, queue: int, closed: bool):
        super().__init__('QSim')
        self.__config_widgets()

        self.channels = channels
        self.queue = queue
        self.closed = closed

    def __config_widgets(self):
        self.title('QSim')
        self.resizable(False, False)
        self._canv = tk.Canvas(self, width=700, height=500, highlightthickness=0)
        self._canv.pack(fill=tk.BOTH)

    def draw_applicant(self):
        pass

    def animate(self):
        l = self._canv.find_withtag('l')
        self._canv.move(l[0], 0, 1)
        self._canv.update()
        self.after(30, self.animate)

    def simulate(self):
        # self._canv.create_line(0, 10, 10, 10, fill="red", tag="l")
        # self.after(0, self.animate)
        self.mainloop()


if __name__ == '__main__':
    qs = QS(1, 0, False)
    qs.simulate()
    ###


