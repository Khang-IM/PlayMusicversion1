import tkinter as tk
from tkinter import messagebox
import track_library as lib
class UpdateTrackWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Update Track")
        self.root.geometry("611x68")

        # Track Number Label and Entry
        self.label_track_number = tk.Label(root, text="Track Number")
        self.label_track_number.place(x=20, y=20)
        self.txt_track_number = tk.Entry(root, width=8)
        self.txt_track_number.place(x=130, y=20)

        # New Rating Label and Entry
        self.label_new_rating = tk.Label(root, text="New Rating")
        self.label_new_rating.place(x=280, y=20)
        self.txt_new_rating = tk.Entry(root, width=5)
        self.txt_new_rating.place(x=400, y=20)

        # Add a button to submit the update (optional)
        self.update_button = tk.Button(root, text="Update", command=self.update_rating)
        self.update_button.place(x=500, y=15)

    def update_rating(self):
        track_number = self.txt_track_number.get().strip()
        new_rating = self.txt_new_rating.get().strip()

        if not track_number or not new_rating:
            messagebox.showerror("Error", "Please fill in both fields.")
            return

        try:
            new_rating = int(new_rating)
            if new_rating < 1 or new_rating > 5:
                messagebox.showerror("Error", "Rating should be between 1 and 5.")
                return
        except ValueError:
            messagebox.showerror("Error", "Rating should be an integer.")
            return
        if track_number not in lib.library:
            messagebox.showerror("Error", f"Track {track_number} not found.")
            return

        play_count = lib.get_play_count(track_number)

        lib.set_rating(track_number, new_rating)

        track_name = lib.get_name(track_number)
        artist = lib.get_artist(track_number)
        track_details = f"Track Name: {track_name}\nArtist: {artist}\nNew Rating: {new_rating}\nPlay Count: {play_count}"
        messagebox.showinfo("Track Updated", track_details)

if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateTrackWindow(root)
    root.mainloop()