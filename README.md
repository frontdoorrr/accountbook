# AccountBook
Simple Account Book using Django

## Description
    수입, 지출 내역을 정리할 수 있는 가계부이다.

## Environment
 mysql

## Prerequisite

```
pip install -r requirements.txt
```

### secrets.json sample
    {
        "SECRET_KEY": "django-insecure-afa4^92hwd0dmgm!h(z@m1cst+h&4s$gro3s4&an6c5@n&t_vr",
        "DATABASE_NAME": "accountbook",
        "DATABASE_USER": "root",
        "DATABASE_PSWD": "abc123!@#",
        "DATABASE_HOST": "localhost",
        "DATABASE_PORT": "3306"
    }




### 로그인, 로그아웃
    - JWT 인증을 통해 구현
    - E-Mail과 비밀번호를 통한 로그인 방식
    - 비밀번호 암호화 저장

### 가계부(AccountBook)
    - 유저 생성 시, 개인별 가계부(AccountBook) 생성
    - 상세 세부 내역(Log)를 통해 내용 입력 / 수정 / 삭제 복사 등 가능
