import tkinter
from tkinter import messagebox

class QuizApp:
    def __init__(self) -> None:
        self.data = [
            {
        "question": "Who is the founder of the C programming language?",
        "options": ["Dennis Ritchie", "Bjarne Stroustrup", "Guido van Rossum", "Linus Torvalds"],
        "correct_ans": 0  
        },
        {
        "question": "Who is the founder of the Python programming language?",
        "options": ["Dennis Ritchie", "Bjarne Stroustrup", "Guido van Rossum", "Linus Torvalds"],
        "correct_ans": 2  
        },
        {
        "question": "Who is the founder of the Java programming language?",
        "options": ["James Gosling", "Ken Thompson", "Larry Page", "Richard Stallman"],
        "correct_ans": 0  
        },
        {
        "question": "Who is the founder of the Perl programming language?",
        "options": ["Larry Wall", "Donald Knuth", "John McCarthy", "Anders Hejlsberg"],
        "correct_ans": 0  
        },
        {
        "question": "Who is the founder of the JavaScript programming language?",
        "options": ["Brendan Eich", "Larry Wall", "Anders Hejlsberg", "Ken Thompson"],
        "correct_ans": 0  
        },
        {
        "question": "Who is the founder of the PHP programming language?",
        "options": ["Rasmus Lerdorf", "Guido van Rossum", "Dennis Ritchie", "James Gosling"],
        "correct_ans": 0  
        },
        {
        "question": "Who is the founder of the C++ programming language?",
        "options": ["Bjarne Stroustrup", "Linus Torvalds", "John McCarthy", "Ken Thompson"],
        "correct_ans": 0  
        },
        {
        "question": "Who is the founder of the R programming language?",
        "options": ["Ross Ihaka", "Rob Pike", "Richard Stallman", "Robin Milner"],
        "correct_ans": 0  
        }
        ]
        self.CurrentQuestion = 0
        self.score = 0
        self.window = tkinter.Tk()
        self.window.geometry("400x400")
        self.window.title("Quiz app")
        self.window.config(bg="light blue")
        self.question_label = tkinter.Label(self.window, text="",bg="light yellow")
        self.question_label.pack()
        self.options_frame = tkinter.Frame(self.window)
        self.options_frame.pack()

        self.options_button = []
        for i in range(4):
            button = tkinter.Button(self.options_frame,text="",width=30,command= lambda ans=i: self.get_answer(ans),bg="lime")
            button.pack(pady=4,padx=4)
            self.options_button.append(button)

        self.next_question = tkinter.Button(self.window,text="Next question",width=30,command = self.next_question,bg="pink")
        self.next_question.pack(pady=10)

    def get_answer(self,opt):
        question_info = self.data[self.CurrentQuestion]
        answer = question_info["correct_ans"]
        if opt == answer:
            self.score = self.score + 1
            messagebox.showinfo("Correct","you selected the correct option")
        else:
            messagebox.showerror("Incorrect","you selected the wrong option")
        
        

    def load_question(self):
        question_info = self.data[self.CurrentQuestion]
        self.question_label.config(text= question_info["question"])
        options = question_info["options"]
        for i in range(4):
            self.options_button[i].config(text = options[i])
    def next_question(self):
        self.CurrentQuestion = self.CurrentQuestion + 1
        if self.CurrentQuestion == len(self.data):
            messagebox.showinfo("Quiz Completed","Your score is"+ str(self.score) +"/8") 
            self.window.quit()
        else:
            self.load_question()

    def start_Quiz(self):
        self.load_question()
        self.window.mainloop()




app = QuizApp()
app.start_Quiz()