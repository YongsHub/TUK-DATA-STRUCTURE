/*
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
	push X: 정수 X를 스택에 넣는 연산이다.
	pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	size: 스택에 들어있는 정수의 개수를 출력한다.
	empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
	top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE 100

typedef int element;
typedef struct {
	int stack[MAX_SIZE];
	int N;
	int topIndex;
} StackType;

void init_stack(StackType* s) {
	s->topIndex = -1;
}

void push(StackType *s, element item) {
	s->stack[++s->topIndex] = item;
}

void pop(StackType *s) {
	if (s->topIndex != -1) {						// 스택이 비어있지 않으면 값 출력
		printf("%d\n", s->stack[s->topIndex--]);
	}
	else if (s->topIndex == -1) printf("-1\n");	// 스택이 비어있으면 -1 출력
}

int size(StackType *s) {
	printf("%d\n", s->topIndex+1);
}

int empty(StackType *s) {
	if (s->topIndex != -1) printf("0\n");			// 스택이 비어있지 않으면 0 출력
	else if (s->topIndex== -1) printf("1\n");		// 스택이 비어있으면 1 출력
}

int top(StackType *s) {
	printf("%d\n", s->stack[s->topIndex]);
}

int main()
{
	StackType s;
	int N;					//총 입력할 줄의 수
	char command[10];		//명령어 저장

	scanf("%d", &N);		//총 줄의 수 입력

	int stack[MAX_SIZE];	//스택 크기
	init_stack(&s);
	for (int i = 0; i < N; i++) {

		scanf("%s", &command);		//명령어 입력

		if (strcmp(command, "push") == 0) {					// push 명령어 입력 (입력받은 문자열이 push인지 비교)
			int num;				//스택에 입력할 정수
			scanf("%d", &num);		//스택에 입력할 정수 입력
			push(&s, num);			//입력 받은 정수 스택에 입력
		}
		else if (strcmp(command, "pop") == 0) pop(&s);		// pop 명령어 입력 (입력받은 문자열이 pop인지비교)
		else if (strcmp(command, "top") == 0) top(&s);		// top 명령어 입력 (입력받은 문자열이 top인지비교)
		else if (strcmp(command, "size") == 0) size(&s);	// size 명령어 입력 (입력받은 문자열이 size인지비교)
		else if (strcmp(command, "empty") == 0) empty(&s);	// empty 명령어 입력 (입력받은 문자열이 empty인지비교)
	}
	return 0;
}