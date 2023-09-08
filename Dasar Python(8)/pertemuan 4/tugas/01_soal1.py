import tkinter as tk

def hitung_total():
    harga = float(entry_harga.get())
    kuantitas = int(entry_kuantitas.get())
    total = harga * kuantitas
    label_hasil.config(text="Total harga adalah: {:.2f}".format(total))

window = tk.Tk()
window.title("Kalkulator Harga")

label_harga = tk.Label(window, text="Harga barang:")
label_harga.pack()
entry_harga = tk.Entry(window)
entry_harga.pack()

label_kuantitas = tk.Label(window, text="kuantitas:")
label_kuantitas.pack()
entry_kuantitas = tk.Entry(window)
entry_kuantitas.pack()

button_hitung = tk.Button(window, text="Hitung total", command=hitung_total)
button_hitung.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()

window.mainloop()