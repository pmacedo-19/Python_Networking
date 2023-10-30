import subprocess
import tkinter as tk

# List of netsh wlan options
netsh_options = [
    "show networks",
    "show profiles",
    "show interfaces",
    # Add more options here
]

def execute_netsh_command():
    selected_option = option_var.get()
    option = netsh_options[selected_option]
    command = f'netsh wlan {option}'
    result = subprocess.check_output(command, shell=True)
    decoded_result = result.decode('utf-8')
    result_text.delete(1.0, tk.END)  # Clear the previous text
    result_text.insert(tk.END, decoded_result)

app = tk.Tk()
app.title("Netsh WLAN Command")

# Create a variable to track the selected option
option_var = tk.IntVar()

# Radiobuttons for netsh options
for i, option in enumerate(netsh_options):
    option_radio = tk.Radiobutton(app, text=option, variable=option_var, value=i)
    option_radio.pack(anchor="w")

# Button to execute the netsh command
execute_button = tk.Button(app, text="Execute", command=execute_netsh_command)
execute_button.pack(anchor="w")

# Text widget to display the command result
result_text = tk.Text(app, wrap=tk.CHAR)  # Use "CHAR" for text wrapping
result_text.pack(fill=tk.BOTH, expand=True)

app.mainloop()
