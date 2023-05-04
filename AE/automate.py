from automan.api import Problem, Automator
from matplotlib import pyplot as plt
import numpy as np

class solve(Problem):
    def get_name(self):
        return 'solve'

    def get_commands(self):
        inp1 = 'python generate_sudoku.py -n 2 -o $output_dir'
        inp2 = 'python generate_sudoku.py -n 3 -o $output_dir'
        inp3 = 'python generate_sudoku.py -n 4 -o $output_dir'
        return [
            ('sudoku2', inp1, None),
            ('sudoku3', inp2, None),
            ('sudoku4', inp3, None)
        ]

    def run(self):
        self.make_output_dir()



class method(Problem):
    def get_name(self):
        return 'method'

    def get_commands(self):
        inp1 = 'python solve_numba.py -n 2 -o $output_dir'
        inp2 = 'python solve_backtracking.py -n 2 -o $output_dir'
        inp3 = 'python solve_no_recursion.py -n 2 -o $output_dir'
        inp4 = 'python solve_numba.py -n 3 -o $output_dir'
        inp5 = 'python solve_backtracking.py -n 3 -o $output_dir'
        inp6 = 'python solve_no_recursion.py -n 3 -o $output_dir'
        inp7 = 'python solve_numba.py -n 4 -o $output_dir'
        inp8 = 'python solve_backtracking.py -n 4 -o $output_dir'
        inp9 = 'python solve_no_recursion.py -n 4 -o $output_dir'
        return [
            ('numba2', inp1, None),
            ('backtracking2', inp2, None),
            ('no_recursion2', inp3, None),
            ('numba3', inp4, None),
            ('backtracking3', inp5, None),
            ('no_recursion3', inp6, None),
            ('numba4', inp7, None),
            ('backtracking4', inp8, None),
            ('no_recursion4', inp9, None),
               ]

    def run(self):
        self.make_output_dir()
        data1 = []
        data2 = []
        data3 = []
        for i in ('numba2', 'numba3', 'numba4'):
            stdout = self.input_path(i, 'stdout.txt')
            with open(stdout) as f:
                values = [float(x) for x in f.read().split()]
                data1.append(values)

        for i in ('backtracking2', 'backtracking3', 'backtracking4'):
            stdout = self.input_path(i, 'stdout.txt')
            with open(stdout) as f:
                values = [float(x) for x in f.read().split()]
                data2.append(values)

        for i in ('no_recursion2', 'no_recursion3', 'no_recursion4'):
            stdout = self.input_path(i, 'stdout.txt')
            with open(stdout) as f:
                values = [float(x) for x in f.read().split()]
                data3.append(values)
        data1 = np.asarray(data1)
        data2 = np.asarray(data2)
        data3 = np.asarray(data3)
        n = [2, 3, 4]
        plt.plot(n, data1, label='numba')
        plt.plot(n, data2, label='backtracking')
        plt.plot(n, data3, label='no_recursion')
        plt.xlabel('n')
        plt.ylabel('time_taken')
        plt.title('Different approach to solve sudoku')
        plt.legend()
        plt.savefig(self.output_path('perf.png'))
        plt.close()


if __name__ == '__main__':
    automator = Automator(
        simulation_dir='outputs',
        output_dir='manuscript/figures',
        all_problems=[solve, method]
                         )
    automator.run()
