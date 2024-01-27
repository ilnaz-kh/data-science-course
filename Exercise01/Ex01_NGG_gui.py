## GUI-base 'Guess Number' program:
## print commands can be removed
import tkinter as tk
from tkinter.font import Font
import random

## Constansts:
LOWER = 1
UPPER = 100
MAX_GUESSES = 6
## Global Variables:
computer_guess = int(random.randint(LOWER, UPPER+1))
count_guesses = 0

def guess_btn_clicked():
    global count_guesses
    if count_guesses == MAX_GUESSES:
        print(f"You lost! :( Please play again. The computer's number was {computer_guess}")
        lbl_result["text"] = f"شما همه {count_guesses} انتخاب خود را انجام داده اید. لطفا از نو بازی کنید"
        return
    try:
        guessed_num = int(ent_guess.get())
        if guessed_num < LOWER or guessed_num > UPPER:
            ## Set new text for the label
            count_text = "\n" + f"برای شما {MAX_GUESSES-count_guesses} انتخاب از {MAX_GUESSES} انتخاب، باقی مانده است"
            lbl_result["text"] = f"عدد وارد شده بین {LOWER} و {UPPER} نمی باشد. لطفا عدد صحیح وارد کنید" + count_text
            print(f"Your guessed number should be between {LOWER} and {UPPER}.")
            return
        
        ent_guess.delete(0, tk.END)
        count_guesses += 1
        count_text = "\n" + f"برای شما {MAX_GUESSES-count_guesses} انتخاب از {MAX_GUESSES} انتخاب، باقی مانده است"
        if guessed_num == computer_guess:
            lbl_result["text"] = f"شما برنده شدید! عدد مورد نظر {computer_guess} بوده است"
            print(f"Wow, You guessed correctly! The computer's number was {computer_guess}")
            ## disable guess entry and guess button:
            ent_guess.config(state="disabled")
            btn_guess.config(state="disabled")

        elif guessed_num > computer_guess:
            if count_guesses < MAX_GUESSES:
                lbl_result["text"] = "حدس شما بیشتر از عدد مورد نظر می باشد" + count_text
                print(f"Your guess {guessed_num} is greater than the computer's number.")
            else: # count_guesses == MAX_GUESSES
                num_text = "\n" + f"عدد مورد نظر {computer_guess} بوده است"
                lbl_result["text"] = "شما باختید! لطفا از نو بازی کنید" + num_text
                print("You lost! Please play again!" + f" The computer's number was {computer_guess}")

        else: ## the guessed number is less than the computer guess
            if count_guesses < MAX_GUESSES:
                lbl_result["text"] = "حدس شما کمتر از عدد مورد نظر می باشد" + count_text
                print(f"Your guess {guessed_num} is less than the computer's number.")
            else: # count_guesses == MAX_GUESSES
                num_text = "\n" + f"عدد مورد نظر {computer_guess} بوده است"
                lbl_result["text"] = "شما باختید! لطفا از نو بازی کنید" + num_text
                print("You lost! Please play again!" + f" The computer's number was {computer_guess}")

    except:
        count_text = "\n" + f"برای شما {MAX_GUESSES-count_guesses} انتخاب از {MAX_GUESSES} انتخاب، باقی مانده است"
        lbl_result["text"] = "عدد معتبری وارد نکرده اید" + count_text
        print("You should enter an integer number!")

def exit_btn_clicked():
    window.destroy()

def restart_btn_clicked():
    ## Restart the Game:
    global computer_guess
    global count_guesses
    count_guesses = 0
    computer_guess = int(random.randint(LOWER, UPPER+1))
    lbl_result["text"] = f"شما {MAX_GUESSES} انتخاب دارید"
    ent_guess.delete(0, tk.END)
    ent_guess.config(state= "normal")
    btn_guess.config(state= "normal")

################ tkinter's GUI design:
## Creating the main window
window = tk.Tk()
## Setting the geometry i.e Dimensions
window.geometry('430x600')
# window.resizable(0, 0)
window.title('بازی بزرگ حدس اعداد')

 ## Creating Frame widgets
frame1 = tk.Frame(master= window)
frame2 = tk.Frame(master= window)
frame3 = tk.Frame(master= window)
frame4 = tk.Frame(master= window)
frame5 = tk.Frame(master= window)
frame1.pack(fill=tk.BOTH, expand=True)
frame2.pack(fill=tk.BOTH, expand=True)
frame3.pack(fill=tk.BOTH, expand=True)
frame4.pack(fill=tk.BOTH, expand=True)
frame5.pack(fill=tk.BOTH, expand=True)

## Creating a label widget
tk.Label(master=frame1, text= f"یک عدد بین {LOWER} و {UPPER} انتخاب کنید",
         font= Font(size=16),
         ).pack(side=tk.RIGHT, padx= 10)

## Creating an Entry widget
ent_guess = tk.Entry(master= frame2, width=20, font= Font(size=16))
ent_guess.pack(side=tk.RIGHT, padx= 10)

## Creating a Button widget
btn_guess = tk.Button(master= frame3, text = "انتخاب کردم", font= Font(size=14), command= guess_btn_clicked)
btn_guess.pack(side=tk.RIGHT, padx= 10)

## Creating a Label widget for showing results
lbl_result = tk.Label(master= frame4, text= f"شما {MAX_GUESSES} انتخاب دارید", justify="right", font= Font(size=14))
lbl_result.pack(side=tk.RIGHT, padx= 10)

## Creating a Button widget for exiting program
tk.Button(master= frame5, text= "خروج", font= Font(size=14),
          command= exit_btn_clicked).pack(side=tk.RIGHT, padx= 20)
## Creating a Button widget for restering program
tk.Button(master= frame5, text= "از نو", font= Font(size=14),
          command= restart_btn_clicked).pack(side=tk.RIGHT, padx= 5)

window.mainloop()
