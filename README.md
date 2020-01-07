# A Exchange rate prediction

Forecasting Exchange Rates Using Time Series Data

### Time Series Analysis란?
>시계열은 일정 시간 간격으로 배치된 데이터들의 수열을 말한다. 시계열 해석(time series analysis)라고 하는 것은 이런 시계열을 해석하고 이해하는 데 쓰이는 여러 가지 방법을 연구하는 분야이다. 예컨대, 이런 시계열이 어떤 법칙에서 생성되어서 나오느냐는 기본적인 질문을 이해하는 것이 궁극적인 목표라고 할 수 있다. 시계열 예측(time series prediction)이라고 하는 것은 주어진 시계열을 보고 수학적인 모델을 만들어서 미래에 일어날 것들을 예측하는 것을 뜻하는 말이다.
[WIKIPEDIA](https://ko.wikipedia.org/wiki/%EC%8B%9C%EA%B3%84%EC%97%B4)

## 설치 방법
- 실행 환경 (테스트 환경)
  - Windows 10 or Ubuntu Linux
  - Python3.x
  
## 예시

- Load the data (약 3000개 2019.12.13 ~ 2019.12.23)

	[Rate of Exchange Crawling](https://github.com/Xenia101/Rate-of-Exchange-Crawling)으로 크롤링 후 output으로 나온 sample.json

```python
with open('./json/sample.json') as json_file:
	json_data = json.load(json_file)
	df = pd.DataFrame(list(json_data.items()),columns = ['ds','y']) 
	df['ds'] = pd.to_datetime(df['ds'])
```

```json
{
	"2007.12.13": 925.0,
	"2007.12.12": 926.5,
	"2007.12.11": 924.0,
	"2019.12.26": 1162.0,
	"2019.12.24": 1164.0,
	"2019.12.23": 1164.0,
}
```

- Prediction

```python
model = Prophet()
model.fit(data)

future = model.make_future_dataframe(periods=365) # 365 days
forecast = model.predict(future)
forecast.tail()
```

- Graph

<p align=center float="left">
	<img width="45%" src="https://github.com/Xenia101/A-Exchange-rate-prediction/blob/master/img/Figure_1.png?raw=true">
	<img width="45%" src="https://github.com/Xenia101/A-Exchange-rate-prediction/blob/master/img/Figure_3.png?raw=true">
</p>

<p align=center>
	<img width="100%" src="https://github.com/Xenia101/A-Exchange-rate-prediction/blob/master/img/Figure_2.png?raw=true">
</p>
