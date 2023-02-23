# 크로메이트 도금 제품 양불 판정 서비스

<p align="center"><img src="https://user-images.githubusercontent.com/108312272/220877097-204f45dd-b477-461d-b629-f3d29d1d86a2.png"></p>

## 1. 프로젝트 소개

> 크로메이트 도금 제품의 정확한 양불 판정으로 품질 균일화를 돕기위한 서비스를 개발하는 것을 목표로 하였습니다. <br><br>
> 개발 기간 : 2022.10 ~ 2022.12 (약 3개월간) <br><br>
> 멤버 : 총 4명(백엔드 1, 프론트엔드 1, 모델러 1, 데이터 1)

<br>

## 2. 주요 기능

- tensorflow를 이용하여 생성한 CNN 모델을 서빙하여 업로드 되는 이미지 양불 판정
- 업로드되는 이미지 정보와 회원정보를 MySQL DB에 적재
- OAuth 2.0 프로토콜을 이용한 구글 소셜 로그인
- Airflow를 이용한 로컬파일에 적재되는 이미지를 일단위로 배치 처리하여 HDFS에 적재
- CI/CD툴인 Jenkins를 이용한 통합, 배포를 자동화 / Slack 연동을 통한 알림

<br>

## 3. 아키텍처

<p align="center"><img src="https://user-images.githubusercontent.com/108312272/220878132-6c64f230-4fae-418b-b8fb-b42dbdf3b05e.png">

## 4. API 명세서
<br>

| 메소드 |           URI            |         설명         |
| :----: | :----------------------: | :------------------: |
|  POST  |         /signup          |       회원가입       |
|  POST  |          /login          |        로그인        |
|  POST  |         /logout          |       로그아웃       |
|  POST  |       /oauth/login       |  구글 로그인 페이지  |
|  GET   |     /oauth/callback      |     권한부여승인     |
|  POST  |      /oauth/logout       |    구글 로그아웃     |
|  GET   |          /main           |   판정 결과 리스트   |
|  POST  |       /main/submit       |     이미지 판정      |
|  GET   | /detail/<<int:imginfo_id>> | 판정 이미지 세부내용 |

<br>

## 5. CNN 튜닝 과정 및 최종 모델 결과
### CNN 튜닝 과정
<p align=""><img src="https://user-images.githubusercontent.com/108312272/220878633-042c8d2c-ef83-4acf-90ef-71e2b6755801.png" width="500"></p>

### 최종 모델 결과
<p align=""><img src="https://user-images.githubusercontent.com/108312272/220878704-0597782f-428e-4254-8d92-61c9f24ed22d.png" width="500"></p>
<br>

## 6. Jenkins 자동 배포 시연 영상
<a href="https://www.youtube.com/watch?v=d_TsNDF6xps&ab_channel=eoruadl">영상 URL</a>
<br>
