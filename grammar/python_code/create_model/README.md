pip list

创建demo.c
    gcc -shared -o demo.so .\demo.c -I "D:/Programfile/anaconda/include" -L "D:\Programfile\anaconda\libs" -lpython37
    即可使用python调用c
    