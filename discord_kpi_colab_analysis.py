import pandas as pd
from google.colab import drive
from IPython.display import display, HTML

# Mount Google Drive
drive.mount('/content/drive')

# Load CSV files
df0 = pd.read_csv('/content/drive/MyDrive/Collab/guild-communicators.csv')
df1 = pd.read_csv('/content/drive/MyDrive/Collab/guild-leavers.csv')
df_7 = pd.read_csv('/content/drive/MyDrive/Collab/guild-retention.csv')
df_8 = pd.read_csv('/content/drive/MyDrive/Collab/guild-total-membership.csv')
df_joins_by_source = pd.read_csv('/content/drive/MyDrive/Collab/guild-joins-by-source.csv')
df_activation = pd.read_csv('/content/drive/MyDrive/Collab/guild-activation.csv')
df_message_activity = pd.read_csv('/content/drive/MyDrive/Collab/guild-message-activity.csv')

# Process DataFrames
df0['active_users'] = df0['visitors'] * df0['pct_communicated'] / 100
df0 = df0.rename(columns={'pct_communicated': 'pct_engagement'})
df_grouped4 = df1.groupby('interval_start_timestamp')['leavers'].sum().reset_index()

# Perform merges
joined_df_D = df_7.merge(df_8, how='outer', on='interval_start_timestamp')
joined_df_B = df_joins_by_source.merge(df_grouped4, how='outer', on='interval_start_timestamp')
joined_df_1_2 = df0.merge(df_activation, how='outer', on='interval_start_timestamp')
joined_df_5_78 = joined_df_D.merge(df_message_activity, how='outer', on='interval_start_timestamp')
joined_df_12_34 = joined_df_B.merge(joined_df_1_2, how='outer', on='interval_start_timestamp')
joined_df_1to8 = joined_df_12_34.merge(joined_df_5_78, how='outer', on='interval_start_timestamp')

# Convert 'interval_start_timestamp' to datetime
joined_df_1to8['interval_start_timestamp'] = pd.to_datetime(joined_df_1to8['interval_start_timestamp'])

# Calculate weekly metrics
weeks = [
    "2024-01-08", "2024-01-15", "2024-01-22", "2024-01-29",
    "2024-02-05", "2024-02-12", "2024-02-19", "2024-02-26",
    "2024-03-04", "2024-03-11"
]

# Initialize DataFrame for metrics
metrics = ['Total Members', 'Total Visitors', 'New Members', 'Members Left',
           'Daily Active Users %', 'Total Messages', 'Engagement %', 'Retention Rate %']
weekly_metrics = pd.DataFrame(index=metrics)

# Populate weekly_metrics with calculated data
for i in range(len(weeks)-1):
    start, end = weeks[i], weeks[i+1]
    mask = (joined_df_1to8['interval_start_timestamp'] >= start) & (joined_df_1to8['interval_start_timestamp'] < end)
    temp_df = joined_df_1to8.loc[mask]
    summary = {
        'Total Members': temp_df['total_membership'].mean(),
        'Total Visitors': temp_df['visitors'].sum(),
        'New Members': temp_df['total_joins'].sum(),
        'Members Left': temp_df['leavers'].sum(),
        'Daily Active Users %': temp_df['active_users'].mean(),
        'Total Messages': temp_df['messages'].sum(),
        'Engagement %': temp_df['pct_engagement'].mean(),
        'Retention Rate %': temp_df['pct_retained'].mean(),
    }
    for metric, value in summary.items():
        weekly_metrics.loc[metric, end] = value

# Round the metrics to 1 decimal point
weekly_metrics = weekly_metrics.round(1)

# Display the final metrics table
display(HTML(weekly_metrics.to_html()))

print("Processing complete!")
