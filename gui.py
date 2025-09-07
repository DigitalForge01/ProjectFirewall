import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
from firewall_core import start_firewall, stop_firewall
from rules_manager import load_rules, add_rule, remove_rule
import os

LOG_FILE = 'firewall.log'

class FirewallGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Firewall")

        # Status label
        self.status_label = tk.Label(root, text="Firewall Status: OFF", fg="red")
        self.status_label.pack()

        # Start/Stop buttons
        self.start_btn = tk.Button(root, text="Start Firewall", command=self.start)
        self.start_btn.pack()

        self.stop_btn = tk.Button(root, text="Stop Firewall", command=self.stop)
        self.stop_btn.pack()

        # Log view
        self.log_box = tk.Text(root, height=20, width=80)
        self.log_box.pack()

        # Refresh log button
        self.refresh_btn = tk.Button(root, text="Refresh Log", command=self.show_log)
        self.refresh_btn.pack()

        # Rule management buttons
        self.rule_btn = tk.Button(root, text="Add Rule", command=self.add_rule_popup)
        self.rule_btn.pack()

    def start(self):
        self.status_label.config(text="Firewall Status: ON", fg="green")
        threading.Thread(target=start_firewall, daemon=True).start()

    def stop(self):
        stop_firewall()
        self.status_label.config(text="Firewall Status: OFF", fg="red")

    def show_log(self):
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                self.log_box.delete('1.0', tk.END)
                self.log_box.insert(tk.END, f.read())

    def add_rule_popup(self):
        rule_type = simpledialog.askstring("Rule Type", "Enter rule type (block_ips / allow_ports / block_protocols):")
        value = simpledialog.askstring("Rule Value", "Enter value:")
        if rule_type and value:
            try:
                # Convert to int if it's a port
                if rule_type == 'allow_ports':
                    value = int(value)
                add_rule(rule_type, value)
                messagebox.showinfo("Rule Added", f"Added {value} to {rule_type}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

