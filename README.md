# File Printer
A script written in python for printing a file from a local file or remote URL.

### Usage Example:

#### Print From file
```shell
python3 main.py /home/usr/Desktop/summary.pdf
```

#### Print From URL
```shell
python3 main.py http://www.example.com/documents/report_1.pdf
```

#### Test Printer
By default this will print a PDF document from the web, if possible. Otherwise it will print a text file.
```shell
python3 main.py test
```


### Configurations:
Default formats:
```python
formats = ['pdf',
           'txt',
           'csv']
```

Default Test Document:
```python
print_sample_url = 'http://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf'

print_sample_text = 'The quick brown fox jumps over the lazy dog.'
```