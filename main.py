import random
import tkinter as tk

# tkinter penceresi oluştur
window = tk.Tk()
window.title("Sayı Tahmin Oyunu")

# işlevleri tanımla
def start_game():
    global secret_number, remaining_guesses
    # sayı aralığı al
    low = int(low_entry.get())
    high = int(high_entry.get())
    # gizli sayıyı belirle
    secret_number = random.randint(low, high)
    # tahmin hakkını al
    remaining_guesses = int(guesses_entry.get())
    # giriş kutularını devre dışı bırak
    low_entry.config(state="disabled")
    high_entry.config(state="disabled")
    guesses_entry.config(state="disabled")
    # yeni oyun mesajını göster
    message_label.config(text="Yeni oyun başladı. Tahmininizi girin.")
    # tahmin kutusunu etkinleştir
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    guess_entry.focus()

def make_guess():
    global remaining_guesses
    # tahmini al
    guess = int(guess_entry.get())
    # tahmini kontrol et
    if guess == secret_number:
        # kazandı mesajını göster
        message_label.config(text="Tebrikler, doğru tahmin! Kazandınız.")
        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")
    elif guess < secret_number:
        # daha büyük sayı tahmin edilmesi gerektiğini belirt
        remaining_guesses -= 1
        if remaining_guesses == 0:
            # kaybetti mesajını göster
            message_label.config(text=f"Maalesef, kaybettiniz. Gizli sayı {secret_number} idi.")
            guess_entry.config(state="disabled")
            guess_button.config(state="disabled")
        else:
            # tekrar tahmin etmek için mesaj ver
            message_label.config(text=f"Daha büyük bir sayı tahmin edin. {remaining_guesses} tahmin hakkınız kaldı.")
    else:
        # daha küçük sayı tahmin edilmesi gerektiğini belirt
        remaining_guesses -= 1
        if remaining_guesses == 0:
            # kaybetti mesajını göster
            message_label.config(text=f"Maalesef, kaybettiniz. Gizli sayı {secret_number} idi.")
            guess_entry.config(state="disabled")
            guess_button.config(state="disabled")
        else:
            # tekrar tahmin etmek için mesaj ver
            message_label.config(text=f"Daha küçük bir sayı tahmin edin. {remaining_guesses} tahmin hakkınız kaldı.")

# arayüz elemanlarını oluştur
low_label = tk.Label(window, text="Aralık (alt):")
low_entry = tk.Entry(window)
high_label = tk.Label(window, text="Aralık (üst):")
high_entry = tk.Entry(window)
guesses_label = tk.Label(window, text="Tahmin Hakkı:")
guesses_entry = tk.Entry(window)
start_button = tk.Button(window, text="Oyuna Başla", command=start_game)
guess_label = tk.Label(window, text="Tahmin:")
guess_entry = tk.Entry(window, state="disabled")
guess_button = tk.Button(window, text="Tahmin Et", command=make_guess)
message_label = tk.Label(window, text="")

# arayüz elemanlarını konumlandır
low_label.grid(row=0, column=0)
low_entry.grid(row=0, column=1)
high_label.grid(row=1, column=0)
high_entry.grid(row=1, column=1)
guesses_label.grid(row=2, column=0)
guesses_entry.grid(row=2, column=1)
start_button.grid(row=3, column=0, columnspan=2)
guess_label.grid(row=4, column=0)
guess_entry.grid(row=4, column=1)
guess_button.grid(row=5, column=0, columnspan=2)
message_label.grid(row=6, column=0, columnspan=2)

# tkinter penceresini göster
window.mainloop()