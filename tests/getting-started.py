#: Created by Kavun Nuggihalli
#: Email: kavunnuggihalli@gmail.com
#: Website: https://kavunnuggihalli.com
# An import we need
import os

# Import plastron module
from plastron import Plastron

# A useful function
def useful_disk_free_check():
    os.system("df -h")

# Inatalize the shell
my_shell = Plastron("Kavun", "PLASTRON", "A personal shell")

# Create a menu for this shell
metrics_menu = my_shell.menu("metrics","Metrics")

# Create an item for this menu to run the function
disk_item = my_shell.item("disk", "Disk check")

# Add the useful function to the item's procedure
disk_item.add_procedure(useful_disk_free_check)

# Add the item to the menu
metrics_menu.add_item(disk_item)

# Add the new menu to the main menu
my_shell.menus['main'].add_item(metrics_menu)

# Launch the shell
my_shell.shell()
