# ------------------------------

# Project Title: Did_ya_watch_your_videos
# Project Purpose: Pop up program which notify you if you watched your videos or not
# Naming Convention: snake_case
# Worked On By: Abdullah Alzahrani
# Notes:
# Python Version: 3.12.3
# Date: Jan 21

# ------------------------------
"""Pop up program which notify you if you watched your videos or not"""
import tkinter as tk
import webbrowser
import os
from PIL import Image, ImageTk


class Application(tk.Tk):
    """This class is to set up root props"""

    def __init__(self):
        super().__init__()
        self.title("Reminder!")

        ico = Image.open(rf"{os.getcwd()}\images\rmd.ico")
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)
        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)


class InputForm(tk.Frame):
    """This class is to design the frame"""

    def __init__(self, parent):
        super().__init__(parent)

        self.vid1 = tk.Checkbutton(self)
        self.vid1.grid(row=0, column=0)
        self.label1 = tk.Label(self, text="How to Read Better", cursor="hand2")
        self.label1.grid(row=0, column=1)
        self.label1.bind(
            "<Button-1>",
            lambda e: webbrowser.open_new(
                "https://www.youtube.com/watch?v=A5ucvNAENjU"
            ),
        )

        self.vid2 = tk.Checkbutton(self)
        self.vid2.grid(row=1, column=0)
        self.label2 = tk.Label(
            self,
            text="كيف تكون مبدع في الادارة المالية وتوفر فلوسك؟ 💵",
            cursor="hand2",
        )
        self.label2.grid(row=1, column=1)
        self.label2.bind(
            "<Button-1>",
            lambda e: webbrowser.open_new(
                "https://www.youtube.com/watch?v=bFfeCSbLaB8"
            ),
        )

        self.vid3 = tk.Checkbutton(
            self,
        )
        self.vid3.grid(row=2, column=0)
        self.label3 = tk.Label(
            self,
            text="The Daily Routine That Changed My Life (4 Habits Most People Ignore)",
            cursor="hand2",
        )
        self.label3.grid(row=2, column=1)
        self.label3.bind(
            "<Button-1>",
            lambda e: webbrowser.open_new(
                "https://www.youtube.com/watch?v=M6dhlz8hhe0&t=1009s"
            ),
        )

        self.vid4 = tk.Checkbutton(
            self,
        )
        self.vid4.grid(row=3, column=0)
        self.label4 = tk.Label(
            self,
            text="ترند  مقطع متداول البروفيسور عبدالله السبيعي في 7 دقائق يتحدث عن كيف تكون شخصية هيبة بطريقة رائعة جدًا.",
            cursor="hand2",
        )
        self.label4.grid(row=3, column=1)
        self.label4.bind(
            "<Button-1>",
            lambda e: webbrowser.open_new("https://x.com/i/status/1837621892183663098"),
        )

        self.vid5 = tk.Checkbutton(
            self,
        )
        self.vid5.grid(row=4, column=0)
        self.label5 = tk.Label(
            self,
            text="ترند  مقطع متداول  الدكتور خالد الجابر في 6 دقائق يوضح لماذا لا نرتاح في الصلاة ويعطي الحلول بطريقة مشوقة ورائعة جدًا.",
            cursor="hand2",
        )
        self.label5.grid(row=4, column=1)
        self.label5.bind(
            "<Button-1>",
            lambda e: webbrowser.open_new("https://x.com/i/status/1858868098448621892"),
        )

        self.clear = tk.Button(self, text="Clear", command=self.clear_content)
        self.clear.grid(row=5, column=1)

    def clear_content(self):
        """If the videos got watched then close everything"""
        self.quit()


def main():
    """Main prog"""
    # schedule.every().day.at("19:51").until(time(19,53,0)).do(run_prog)
    # while 1:
    #     schedule.run_pending()
    #     tm.sleep(1)
    app = Application()
    app.mainloop()
    



if __name__ == "__main__":
    main()
