from Simulator import Simulator


def main():
    simulation = Simulator()
    simulation.run_simulation()
    simulation.print_table()
    simulation.print_statistics()

main()

