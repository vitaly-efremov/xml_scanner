# XML Scanner 

How to install?
------------  
```
  poetry install
```

Benchmark results
------------  
For all methods report generation repeated 100x. 
```
  timeit.timeit(lambda: report_generator.generate(path), number=100)
```


| Method          | Time  |
|-----------------|-------|
| Multiprocessing | 26.97 |
| Async           | 34.34 |
| Sync            | 39.73 |
| Multithreading  | 45.90 |

So the fastest way of processing this task is **Multiprocessing** method.
