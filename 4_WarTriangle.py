import tkinter as tk
from tkinter import messagebox
import pygame
import emoji
emoji = "\U0001F93A"
import tkinter.font as tkFont

class InvalidInputException(Exception):
    pass

class MainWindow:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("War Triangle")
        self.main_window.attributes('-fullscreen', True)
        
        # Set background image
        self.set_background_image(self.main_window,"F:\\WISE_218\\WarTri.png")
        
        #Adding text
        text = tk.Label(self.main_window, text="WAR TRIANGLE", font=("Times", 50),bg="white")
        text.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Create the start button
        self.start_button = tk.Button(self.main_window, text="Start",font=("Times", 25), bg="#38719f", fg="#cce1e4", bd=0, command=self.open_input_window)
        self.start_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        
        self.main_window.mainloop()
    
    def set_background_image(self, window, image_path):
        image = tk.PhotoImage(file=image_path)
        background_label = tk.Label(window, image=image)
        background_label.image = image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def open_input_window(self):
        self.input_window = tk.Toplevel(self.main_window)
        self.input_window.title("Enter Number of Rows")
        self.input_window.attributes('-fullscreen', True)

        # Set background image
        self.set_background_image(self.input_window,"F:\\WISE_218\\wartriangle.png")
        
        self.rows_label = tk.Label(self.input_window, text="Enter Number of Rows",font=("Times", 40),bg="#a4745e",bd=0)
        self.rows_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        
        self.rows_entry = tk.Entry(self.input_window,bg='black',fg='white', bd=5)
        self.rows_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        submit_button = tk.Button(self.input_window, text="Generate War Triangle",font=("Times",15),bg="#d4bfb2",bd=0,command=self.generate_triangle)
        submit_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    
    def generate_triangle(self):
        try:
            num_rows = int(self.rows_entry.get())
            if not (0 < num_rows < 10):
                raise InvalidInputException("!! Number of rows should be between 1 and 9 !!")
            triangle = self.generate_triangle_pattern(num_rows)
            self.display_triangle(triangle)
        except ValueError:
            messagebox.showerror("Error", "!! Invalid input. Please enter a number !!")
        except InvalidInputException as e:
            messagebox.showerror("Error", str(e))
    
    def generate_triangle_pattern(self, num_rows):
        triangle = []
        i = 1
        while i <= num_rows:
            triangle.append(emoji * i)
            i += 1
        i = num_rows - 1
        while i > 0:
            triangle.append(emoji * i)
            i -= 1
        return triangle

    
    def display_triangle(self, triangle):
        self.output_window = tk.Toplevel(self.main_window)
        self.output_window.title("War Triangle Output")
        self.output_window.attributes('-fullscreen', True)
        # Set background image
        self.set_background_image(self.output_window, "F:\\WISE_218\\war tri (1).png")
        self.display_next_row(triangle, 0)


    def display_next_row(self, triangle, i):
        if i >= len(triangle):
            return
        font = tkFont.Font(size=30)  # Adjust the size as needed
        row_label = tk.Label(self.output_window, font=font,text=" ".join(triangle[i]))
        row_label.pack(anchor="w",padx=10,expand=True)
        # Wait 500 milliseconds before displaying the next row
        self.output_window.after(500, self.display_next_row, triangle, i + 1)
        right_label = tk.Label(self.output_window, text="The Required Pattern to form War Triangle",font=("Times", 25))
        right_label.place(relx=0.5, rely=0.7, anchor="se")


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("The Avengers Theme Song.mp3")
pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # Play the music in an infinite loop (-1)

if __name__ == "__main__":
    main_window = MainWindow()
    pygame.mixer.music.stop()