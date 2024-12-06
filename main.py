import xml.etree.ElementTree as ET
import pandas as pd

# XML 파일 로드
tree = ET.parse('/content/내보내기.xml')
root = tree.getroot()

# 수면 데이터 중 애플워치로 기록된 항목만 추출
data = []
for record in root.findall(".//Record[@type='HKCategoryTypeIdentifierSleepAnalysis']"):
    source_name = record.get('sourceName')
    device = record.get('device')
    
    # sourceName이나 device에 'Watch'가 포함된 경우 추출
    if source_name and 'Watch' in source_name:
        start_date = record.get('startDate')
        end_date = record.get('endDate')
        value = record.get('value')
        data.append({
            'Start Date': start_date,
            'End Date': end_date,
            'Value': value
        })

# 데이터프레임으로 변환
df = pd.DataFrame(data)

# 시간 형식 변환
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# 9월과 10월 데이터 필터링
df = df[df['Start Date'].dt.month.isin([9, 10])]

# 필터링된 데이터를 CSV로 저장
df.to_csv('watch_sleep_data_filtered.csv', index=False)

print("데이터를 watch_sleep_data_filtered.csv 파일로 저장했습니다.")
