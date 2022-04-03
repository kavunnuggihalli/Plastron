#: Created by Kavun Nuggihalli
#: Email: kavunnuggihalli@gmail.com
#: Website: https://kavunnuggihalli.com
from plastron import Plastron
import os

class App:

    def __init__(self):
        # Setup your plastron application
        self.plastron = Plastron("Kavun Nuggihalli", "Kavun", "A personal shell")

        """
        METRICS MENU
        """
        # Create my first menu object with some items
        metrics = self.plastron.menu("metrics","Metrics")

        """
        METRICS MENU ITEMS
        """
        # An item to add disk usage
        disk = self.plastron.item("disk", "Disk check")
        disk.add_procedure(self.disk_free)
        metrics.add_item(disk)

        # An item to add memory analysis
        memory = self.plastron.item("memory", "Memory analysis")
        memory.add_procedure(self.memory_analysis)
        metrics.add_item(memory)

        # An item to check processess using top interactive
        process = self.plastron.item("process", "Processes analysis")
        process.add_procedure(self.check_processes)
        metrics.add_item(process)

        """
        RUN SHELL
        """
        # Launch the plastron shell
        self.plastron.menus['main'].add_item(metrics)
        self.plastron.shell()

    # A function to check disk usage
    def disk_free(self):
        os.system("df -h")

    # A function to check memory usage
    def memory_analysis(self):
        os.system("top -l 1 -s 0 | grep PhysMem")

    # A function to check memory usage
    def check_processes(self):
        os.system("top")

App()
