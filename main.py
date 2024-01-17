import socket
import psutil
from tkinter import *



DEEP_BLUE = "#004080"
ACCENT_ORANGE = "#ffa500"
STEEL_GREY = "#9a9a9a"
CHARCOAL = "#333333"


def get_hostname ():
    hostname = socket.gethostname()
    return hostname



def get_ethernet_wifi_ips():
    # all nics as a dict
    addrs = psutil.net_if_addrs()

    ethernet_ips = []
    wifi_ips = []


    for nic, addresses in addrs.items():
        if "ethernet" in nic.lower():
            ethernet_ips.extend([addr.address for addr in addresses if addr.family == socket.AF_INET])
        elif "wi-fi" in nic.lower():
            wifi_ips.extend([addr.address for addr in addresses if addr.family == socket.AF_INET])

    return ethernet_ips, wifi_ips


ethernet_ips, wifi_ips = get_ethernet_wifi_ips()

window = Tk()
window.title("IP-Lookup")
window.minsize(width=250, height=250)
window.config(bg=DEEP_BLUE, pady=10)

# Hostname Frame
hostname_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2, highlightbackground=ACCENT_ORANGE)
hostname_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

hostname_label = Label(hostname_frame, text="Computer Name:")
hostname_label.config(bg=DEEP_BLUE, fg="white", font=("Arial", 10))
hostname_label.grid(row=0, column=0, pady=5, padx=10)

hostname_value = Label(hostname_frame, text=get_hostname())
hostname_value.config(bg=DEEP_BLUE, fg="white", font=("Arial", 12, "bold"))
hostname_value.grid(row=0, column=1, pady=5, padx=10)


# Ethernet Frame
ethernet_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2, highlightbackground=ACCENT_ORANGE)
ethernet_section_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

for item in range(len(ethernet_ips)):
    ethernaet_label = Label(ethernet_section_frame, text=f'Ethernet {item}:')
    ethernaet_label.config(bg=DEEP_BLUE, fg="white", font=("Arial", 12, "bold"))
    ethernaet_label.grid(row=item, column=0,padx=10, pady=10)

    ethernaet_value = Label(ethernet_section_frame, text=f'{ethernet_ips[item]}')
    ethernaet_value.config(bg=DEEP_BLUE, fg="white", font=("Arial", 12, "bold"))
    ethernaet_value.grid(row=item, column=1,padx=10, pady=10, sticky="w")

# WiFi Frame
wifi_section_frame = Frame(window, bg=DEEP_BLUE, bd=2, relief=GROOVE, highlightthickness=2, highlightbackground=ACCENT_ORANGE)
wifi_section_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

for item in range(len(wifi_ips)):
    wifi_label = Label(wifi_section_frame, text=f'Wifi {item}:         ')
    wifi_label.config(bg=DEEP_BLUE, fg="white", font=("Arial", 12, "bold"))
    wifi_label.grid(row=item, column=0,padx=10, pady=10)

    wifi_value = Label(wifi_section_frame, text=f'{wifi_ips[item]}')
    wifi_value.config(bg=DEEP_BLUE, fg="white", font=("Arial", 12, "bold"))
    wifi_value.grid(row=item, column=1,padx=10, pady=10, sticky="w")
window.mainloop()

