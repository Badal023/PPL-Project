import tkinter as tk
from tkinter import messagebox

# Sample product data
products = {
    "Apple": 50.0,
    "Banana": 30.0,
    "Carrot": 40.0,
    "Tomato": 20.0
}

# List to store the cart items
cart = []

# Function to add product to the cart
def add_to_cart():
    selected_product_index = listbox_products.curselection()
    if selected_product_index:
        selected_product = listbox_products.get(selected_product_index[0]).split(" - ")[0]
        cart.append(selected_product)
        update_cart_list()
    else:
        messagebox.showerror("Error", "Please select a product to add to the cart.")

# Function to update the cart list
def update_cart_list():
    listbox_cart.delete(0, tk.END)
    total_amount = 0
    for item in cart:
        listbox_cart.insert(tk.END, f"{item} - ₹{products[item]}")
        total_amount += products[item]
    label_total.config(text=f"Total: ₹{total_amount:.2f}")

# Function to checkout and generate the bill
def checkout():
    if cart:
        bill = "\n".join([f"{item} - ₹{products[item]}" for item in cart])
        total_amount = sum([products[item] for item in cart])
        bill += f"\n\nTotal: ₹{total_amount:.2f}"
        messagebox.showinfo("Bill", bill)
        cart.clear()
        update_cart_list()
    else:
        messagebox.showerror("Error", "Your cart is empty.")

# Function to clear the cart
def clear_cart():
    cart.clear()
    update_cart_list()

# Create the main window
root = tk.Tk()
root.title("Basic Checkout System")
root.geometry("600x500")

# Product List Display
frame_products_list = tk.Frame(root)
frame_products_list.pack(pady=10)

label_products = tk.Label(frame_products_list, text="Available Products:")
label_products.pack()

listbox_products = tk.Listbox(frame_products_list, width=50, height=10)
for product, price in products.items():
    listbox_products.insert(tk.END, f"{product} - ₹{price}")
listbox_products.pack()

# Cart Area
frame_cart = tk.Frame(root)
frame_cart.pack(pady=10)

label_cart = tk.Label(frame_cart, text="Items in Cart:")
label_cart.pack()

listbox_cart = tk.Listbox(frame_cart, width=50, height=10)
listbox_cart.pack()

label_total = tk.Label(frame_cart, text="Total: ₹0.00")
label_total.pack()

# Checkout and Cart Actions
frame_actions = tk.Frame(root)
frame_actions.pack(pady=10)

button_add_to_cart = tk.Button(frame_actions, text="Add to Cart", command=add_to_cart)
button_add_to_cart.grid(row=0, column=0)

button_checkout = tk.Button(frame_actions, text="Checkout", command=checkout)
button_checkout.grid(row=0, column=1)

button_clear_cart = tk.Button(frame_actions, text="Clear Cart", command=clear_cart)
button_clear_cart.grid(row=1, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
