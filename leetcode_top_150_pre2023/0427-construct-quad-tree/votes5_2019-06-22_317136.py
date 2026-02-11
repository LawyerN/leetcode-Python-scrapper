for i in range(2,8):
    a = make_grid(1<<i)
    %timeit construct(a)