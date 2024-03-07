# Discord Analytics KPI Dashboard

This repository provides a Python script designed to run in Google Colab, offering an easy way to display key performance indicators (KPIs) from Discord's analytics. The script processes CSV files exported from Discord to calculate and display various KPIs, facilitating quick insights into community engagement and growth.

## Features

- Calculation of KPIs such as Total Members, New Members, Engagement Percentage, and more.
- Weekly metrics display, offering insights into community trends over time.
- Easy to use in Google Colab with minimal setup required.

## Prerequisites

- Google Colab account
- CSV files exported from Discord containing analytics data

## How to Use

1. **Prepare Your Data**: Export your Discord analytics data as CSV files.
2. **Set Up Google Colab**: Open a new notebook in Google Colab.
3. **Mount Google Drive**: Use the script to mount your Google Drive where the CSV files are stored.
4. **Run the Script**: Execute the provided Python script in your Colab notebook. Ensure the CSV file paths in the script match those in your Google Drive.
5. **View KPIs**: The script will output a table displaying the calculated KPIs, with metrics as rows and weeks as columns.

## Customization

To customize the KPIs or adjust the time frame, modify the `weeks` list and the `summary` dictionary in the script as needed.
