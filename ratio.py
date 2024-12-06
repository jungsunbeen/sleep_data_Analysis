import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 로드
df = pd.read_csv('watch_sleep_data_all.csv')

# 시간 형식 변환
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# 수면 지속 시간 계산
df['Duration'] = (df['End Date'] - df['Start Date']).dt.total_seconds() / 3600

# 수면 시작 시간대 (잠든 시간의 시각만 추출)
df['Hour'] = df['Start Date'].dt.hour

# 수면 단계 필터링 (REM 수면 데이터만)
df_rem = df[df['Value'].str.contains('AsleepREM')]

# 수면 단계 필터링 (Core 수면 데이터만)
df_core = df[df['Value'].str.contains('AsleepCore')]

# 수면 단계 필터링 (Deep 수면 데이터만)
df_deep = df[df['Value'].str.contains('AsleepDeep')]

# 잠든 시간대별 REM 수면 비율 계산
rem_ratios = df_rem.groupby('Hour')['Duration'].sum() / df.groupby('Hour')['Duration'].sum()

# 시각화
plt.figure(figsize=(10, 6))
rem_ratios.plot(kind='bar', color='skyblue', alpha=0.7)
plt.xlabel('Hour of Sleep Onset')
plt.ylabel('REM Sleep Ratio')
plt.title('REM Sleep Ratio by Hour of Sleep Onset')
plt.tight_layout()
plt.show()
