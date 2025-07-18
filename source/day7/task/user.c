#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ID_LENGTH 50 

char filename[] = "userFile.txt";

//입력버퍼 지우는 함수
void clearReadBuffer(){
	int ch;
	while((ch = getchar()) != '\n' && ch != EOF );
	clearerr(stdin); // ★ 에러 상태 초기화
}



//회원가입 함수  
// register은 예약어다!! 명심할 것 
void register_user()
{
	// 변수 선언
	char id[50]; //아이디 저장
	char pw[50]; //비밀번호 저장
	FILE *fp; //파일 포인터
	char line[200]; //파일에서 한 줄씩 읽어올 버퍼
	char saved_id[50]; // 파일에서 읽은 아이디
	char saved_pw[50]; //파일에서 읽은 패스워드

	// 아이디 입력 받기
	printf("아이디를 입력하세요: \n");
	scanf("%s", id); //문자열은 %s

	// 비밀번호 입력 받기
	printf("비밀번호를 입력하세요: \n");
	scanf("%s", pw);

	//userFile.txt 파일 읽기 모드로 열기
	// 파일을 열어야 fp null인지 아닌지 알 수 있다 -> 아하!
	fp = fopen(filename, "r");

	if(fp == NULL)
	{
		//파일이 없으면 중복검사 안 하고 새로 저장하러 감
		fp = fopen(filename,"a"); // 쓰기모드로 연다
		if(fp == NULL)
		{
			printf("해당 파일 열 수 없습니다");
			return;
		}
		// fprinf 사용방법 -> fprintf(fp, "저장할 형식", 변수1, 변수2);
		fprintf(fp,"%s,%s\n", id, pw);
		fclose(fp); //함수는 무조건 ()
		printf("회원가입완료\n");	
	}
	else 
	{
		//파일 있으면 중복 검사
		while (fgets(line, sizeof(line), fp)) // 한 줄씩 읽으면서 저장된 아이디/비번 꺼낸다
		{
			sscanf(line, "%[^,],%s", saved_id, saved_pw);  // %[^,] : 콤마 전까지 아이디 저장, %s 콤마뒤 비번저장
			
			//입력한 아이디와 비교
			if(strcmp(saved_id, id)== 0)
			{
				// 아이디 같으면 -> 이미존재
				printf("이미 존재하는 아이디입니다\n");
				fclose(fp);
				return;
			}
			
		} //while 끝
		fclose(fp);
	}
	// 아이디 같지 않음 -> 새로 만들기 
	fp = fopen(filename, "a");
	if(fp == NULL)
	{
		printf("파일을 열 수 없습니다\n");
		return;
	}
	
	fprintf(fp, "%s,%s\n", id, pw);
	fclose(fp);
	printf("----회원가입 완료----\n");
}

//로그인 함수
void login_user()
{
	//변수 선언
	char id[50]; 
	char pw[50]; 
	FILE *fp; 
	char line[200]; 
	char saved_id[50]; 
	char saved_pw[50]; 
	int success = 0; //로그인 성공 여부 표시하는 변수

	// 아이디 입력 받기
	printf("로그인할 아이디를 입력해주세요: \n");
	scanf("%s", id);

	// 비밀번호 입력 받기
	printf("로그인할 비밀번호를 입력해주세요: \n");
	scanf("%s", pw);

	//파일 열기
	fp = fopen(filename, "r");

	if(fp == NULL)
	{
		printf("해당 아이디가 존재하지 않습니다\n");
		return;
	}

	// 회원가입으로 이동하시겠습니까? YES -> 회원가입 함수 불러옴 (추가적으로 해볼)
	while (fgets(line, sizeof(line), fp))
	{
		//아이디, 비밀번호 분리
		sscanf(line, "%[^,],%s", saved_id, saved_pw);

		if (strcmp(saved_id, id) == 0 && strcmp(saved_pw, pw) == 0)
		{
			printf("🎉 로그인 성공!\n");
			success = 1;
			return;
		}
	} // while 끝

	fclose(fp);

	if(success == 0) 
	{ 
		printf(" ❌ 로그인 실패\n "); 
	}
	return;
}// 로그인 함수 끝

//메인
int main(void){
	int choice; // 입력을 받을 변수
	int result; // scanf로 받을 숫자가 정수인지 아닌지 확인하기 위한 변수

	while(1){
		printf("메뉴를 선택하세요: \n");
		printf("==== 메뉴 ====\n");
		printf("1. 회원가입\n");
		printf("2. 로그인\n");
		printf("3. 종료\n");
		printf("==============\n");
		//scanf("%d", &choice); //문제발생 ->문자,문자열 입력시 무한루프 빠짐 
		
		//해결방안
		
		//printf("선택한 번호: \n");
		//result = scanf("%d", &choice);
		
		//1.숫자가 아닌값을 입력했을시(숫자입력)
		// if(result != 1){ 
		// 	printf("❌ 숫자를 입력해주세요\n");
		// 	clearReadBuffer();
		// 	continue;
			
		// }
		//2. 숫자 + 문자 섞어 입력했을 때(숫자 실패)
		//clearReadBuffer();
		
		//3. 숫자가 범위를 벗어났을 때(범위 벗어남)
		// if(choice < 1 || choice > 3){
		// 	printf("잘못된 번호입니다. 다시 선택해주세요\n");
		// 	clearReadBuffer();
		// 	continue; //처음으로 돌아가서 메뉴 보여주기
		// }
		
		
		switch (choice)
		{
		case 1:
			printf("회원가입하기\n");
			//회원가입 함수 호출
			register_user();
			break;
		case 2:
			printf("로그인하기\n");
			//로그인 함수 호출
			login_user();
			break;
		case 3:
			printf("프로그램을 종료합니다\n");
			return 0;
		default:
			printf("잘못된 번호입니다. 다시 선택해주세요\n");
		} // switch 끝
	}//while 끝
}

