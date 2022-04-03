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
        metrics = self.plastron.menu("metrics","Metrics")
        # Create a submenu of metrics
        checks = self.plastron.menu("checks", "Checks")
        metrics.add_item(checks)
        # An item to add disk usage
        disk = self.plastron.item("disk", "Disk check")
        disk.add_procedure(self.disk_free)
        checks.add_item(disk)
        # Create a submenu of metrics
        analysis = self.plastron.menu("analysis", "Analysis")
        metrics.add_item(analysis)
        # An item to add memory analysis
        memory = self.plastron.item("memory", "Memory analysis")
        memory.add_procedure(self.memory_analysis)
        analysis.add_item(memory)
        # An item to check processess using top interactive
        process = self.plastron.item("process", "Processes analysis")
        process.add_procedure(self.check_processes)
        analysis.add_item(process)

        """
        CONFIGURE MENU
        """
        # Create another menu and some sub menus
        configure = self.plastron.menu("configure","Configure")
        # Create a submenu to the configure menu
        manual = self.plastron.menu("manual","Manual")
        configure.add_item(manual)
        # Add an item to manual to adjust zsh
        zsh = self.plastron.item("zsh", "Edit ZSH settings")
        zsh.add_procedure(self.zsh_editor)
        manual.add_item(zsh)
        # Create a submenu to the configure menu
        automatic = self.plastron.menu("automatic", "Automatic")
        configure.add_item(automatic)

        """
        RUN SHELL
        """
        # Launch the plastron shell
        self.plastron.menus['main'].add_item(metrics)
        self.plastron.menus['main'].add_item(configure)
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

    # Edit zsh
    def zsh_editor(self):
        os.system("vim ~/.zshrc")

App()
