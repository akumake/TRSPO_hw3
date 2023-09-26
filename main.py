import multiprocessing as mp
import time

def colatz_steps(col_num: int):
    steps = 0
    while col_num != 1:
        if col_num % 2 == 0:
            col_num = col_num // 2
        else:
            col_num = 3 * col_num + 1

        steps += 1

    return steps

if __name__ == '__main__':
    N = 1000000
    num_threads = 14
    numbers_list = list(range(1, N+1))

    pool = mp.Pool(num_threads)

    results = pool.map(colatz_steps, numbers_list)

    pool.close()
    pool.join()

    average_steps = sum(results) / len(numbers_list)
    print(f'Середня кількість кроків: {average_steps}')