## Fivetwork OPEN API

### 소개

2018년 300인 이상 사업장에, 2020년 50인 이상 사업장에 마지막으로 2021년에 50인 이하 사업장으로 확대될 주 52시간제를 위한 근태관리 오픈소스 프로젝트 `Fivetwork`입니다.

### API Swagger

```
localhost:5000/api/documentation
```


### Usage

#### CLI Setting
```sh
export FLASK_APP=manage
```

#### Migrate DB

```sh
flask db init
```

```sh
flask db migrate --comment "blas"
```

```sh
flask db upgrade
```

#### Testing
```sh
flask test
```

#### Run Flask App
```sh
flask run
```

#### Create Super user
```sh
flask createsuperuser
```
