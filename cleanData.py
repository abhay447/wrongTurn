import pandas as pd
df = pd.read_csv('Data.csv',index_col=False)
df = df[(df['Casualty Class']=='Driver') | (df['Casualty Class']=='Driver/Rider')]

df = df[['Time (24hr)','Road Surface','Age of Casualty',
         'Sex of Casualty', 'Type of Vehicle','Casualty Severity']]

df.rename(columns={'Sex of Casualty': 'Sex', 'Age of Casualty': 'Age',
                  'Casualty Severity':'Severity', 'Time (24hr)':'Time',
                  'Road Surface':'Surface','Type of Vehicle':'Vehicle'}, inplace=True)

#clean Road-Surface,Casuality-Severity Data
surface_dict = {}
for i in list(df['Surface'].unique()):
    surface_dict[i] = list(df['Surface'].unique()).index(i)
severity_dict = {}
for i in list(df['Severity'].unique()):
    severity_dict[i] = list(df['Severity'].unique()).index(i)+1
sex_dict = {}
for i in list(df['Sex'].unique()):
    sex_dict[i] = list(df['Sex'].unique()).index(i)
veh_dict = {}
for i in list(df['Vehicle'].unique()):
    veh_dict[i] = list(df['Vehicle'].unique()).index(i)

print surface_dict
print sex_dict
print veh_dict
print severity_dict
df = df.replace({'Surface':surface_dict,'Severity':severity_dict,
                'Sex':sex_dict,'Vehicle':veh_dict})
df.to_csv('DriverCauses.csv')