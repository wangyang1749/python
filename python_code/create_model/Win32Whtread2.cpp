#include <stdio.h>
#include <Windows.h>
#include <process.h>
 
void __cdecl ThreadProc(void *para)
{
    printf("sub thread started\n");
	// TODO: Add your thread code here.
	printf("sub thread finished\n");
	_endthread();	// 可以省略，隐含会调用。
}
 
int main(int argc, char* argv[])
{
	HANDLE hThread = (HANDLE)_beginthread(ThreadProc, 0, NULL);
 
	WaitForSingleObject(hThread,INFINITE);
	CloseHandle(hThread);
}
