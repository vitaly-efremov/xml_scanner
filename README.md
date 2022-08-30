# XML Scanner 

The task
------------  
1. Создает 50 zip-архивов, в каждом 100 xml файлов со случайными данными следующей структуры:
```
<root>
	<var name=’id’ value=’<случайное уникальное строковое значение>’/>
	<var name=’level’ value=’<случайное число от 1 до 100>’/>
	<objects>
		<object name=’<случайное строковое значение>’/>
		<object name=’<случайное строковое значение>’/>…
	</objects>
</root>
```
В тэге objects случайное число (от 1 до 10) вложенных тэгов object.

2. Обрабатывает директорию с полученными zip архивами, разбирает вложенные xml файлы и формирует 2 csv файла:
	- Первый: id, level - по одной строке на каждый xml файл
	- Второй: id, object_name - по отдельной строке для каждого тэга object (получится от 1 до 10 строк на каждый xml файл)

Очень желательно сделать так, чтобы задание 2 эффективно использовало ресурсы многоядерного процессора.

How to install?
------------  
```
  poetry install
```

How to run?
------------  
```
  poetry run python main.py
```
Generated results are in `/report` directory

Benchmark results
------------  
For all methods report generation repeated 100x (MacOs 16 core)
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
