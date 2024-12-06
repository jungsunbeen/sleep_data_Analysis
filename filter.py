import pandas as pd
import matplotlib.pyplot as plt

# 필터링된 CSV 파일 로드 (9월과 10월 데이터)
df_sept_oct = pd.read_csv('watch_sleep_data_filtered.csv')

# 시간 형식 변환
df_sept_oct['Start Date'] = pd.to_datetime(df_sept_oct['Start Date'])
df_sept_oct['End Date'] = pd.to_datetime(df_sept_oct['End Date'])

# 수면 지속 시간 계산
df_sept_oct['Duration'] = (df_sept_oct['End Date'] - df_sept_oct['Start Date']).dt.total_seconds() / 3600

# 수면 시간이 있는 날짜들만 필터링 (Duration이 0이 아닌 경우)
df_sept_oct = df_sept_oct[df_sept_oct['Duration'] > 0]

# 수면 시간 시각화 (데이터가 있는 날짜만)
plt.figure(figsize=(10, 6))
plt.plot(df_sept_oct['Start Date'], df_sept_oct['Duration'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Sleep Duration (hours)')
plt.title('Sleep Duration Trend (September & October)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
