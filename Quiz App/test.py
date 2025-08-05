from tkinter import *
import csv

questions = {
    "8+3": ['2', '11', '5', '9'],
    "5-1": ['2', '4', '5', '2'],
    "18/2": ['3', '8', '9', '7'],
    "6*9": ['45', '23', '54', '99'],
    "Who is the father of nation?": ['Narendra Modi','Saish Chavan','Mahatma Gandhi','Lal Bhadur Shastri'],
    "Name the National Game of India":['Football','Hockey','Basketball','Cricket'],
    "Name the National Bird of India":['Dove','Peacock','Parrot','Peahen'],
    "Is Helium and neon gases":['True','False'] 
}
ans = ['11', '4', '9', '54','Mahatma Gandhi','Hockey','Peacock','True']

current_question = 0
user_name = "glenjr009"

def start_quiz():
    global user_name
    user_name = name_entry.get()
    if user_name:
        name_prompt.pack_forget()
        name_entry.pack_forget()
        start_button.pack_forget()
        next_button.pack()
        next_question()

def next_question():
    global current_question
    if current_question < len(questions):
        check_ans()
        user_ans.set('None')
        c_question = list(questions.keys())[current_question]
        clear_frame()
        Label(f1, text=f"Question: {c_question}", padx=15, font="calibre 28 italic", bg="#E6E6FA").pack(anchor=NW)

        for option in questions[c_question]:
            Radiobutton(f1, text=option, variable=user_ans, value=option, padx=28, font="calibre 16 italic", bg="#E6E6FA", selectcolor="#FFB6C1", indicatoron=0, width=20).pack(anchor=NW, pady=5)
        current_question += 1
    else:
        check_ans()
        next_button.pack_forget()
        show_result()

def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == ans[current_question - 1]:
        user_score.set(user_score.get() + 1)

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

def save_score_to_csv(name, score):
    with open('quiz_scores.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, score])

def show_result():
    clear_frame()
    output = f"Your Score is {user_score.get()} out of {len(questions)}"
    Label(f1, text=output, font="calibre 25 bold italic", bg="#E6E6FA").pack(pady=10)
    Label(f1, text="Congratulations! Above is your final score, Well Played", font="calibre 22 bold italic", bg="#E6E6FA").pack(pady=10)
    
    save_score_to_csv(user_name, user_score.get())
    
    exit_button = Button(f1, text="Exit", command=root.destroy, font="calibre 18 bold italic", bg="#FFB6C1")
    exit_button.pack(pady=20)

def add_credits():
    credits_label = Label(root, text="App designed by Glen and Team", font="calibre 12 italic", bg="#E6E6FA", fg="#4B0082")
    credits_label.pack(side=BOTTOM, pady=10)

if __name__== "__main__":
    root = Tk()
    root.title("GIT QUIZ APP")
    root.geometry("850x520")
    root.minsize(800, 400)
    root.configure(bg="#E6E6FA")  
    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)

    name_prompt = Label(root, text="Enter your name:", font="calibre 25 bold italic", bg="#E6E6FA")
    name_prompt.pack(pady=10)
    name_entry = Entry(root, font="calibre 18 italic", width=30)
    name_entry.pack(pady=10)
    start_button = Button(root, text="Click here to Start the Quiz", command=start_quiz, font="calibre 25 bold italic", bg="#FFB6C1")
    start_button.pack(pady=10)

    f1 = Frame(root, bg="#E6E6FA")
    f1.pack(side=TOP, fill=X)

    next_button = Button(root, text="Next Question", command=next_question, font="calibre 22 bold italic", bg="#FFB6C1")

    add_credits()  

    root.mainloop()
