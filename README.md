# Data Visualization Tool - Histogram Generator

## Overview
This tool allows users to upload any dataset (in CSV format) and quickly generate histograms to visualize the distribution of both categorical and numerical data. The first 15 entries from the dataset are displayed for context, saving time for deeper analysis.

## Features
- Upload any dataset in CSV format.
- View the first 15 rows for a quick glance.
- Visualize categorical data frequency.
- Visualize numerical data distribution through histograms.

## How to Use
1. Upload a CSV file using the drag-and-drop interface or by selecting a file.
2. The first 15 rows of the dataset will be displayed for context.
3. Choose a column from the dropdown to generate the histogram (both categorical and numerical columns are supported).
4. The tool will generate and display a histogram based on the selected column.

## Technologies Used
- **Dash** for the web interface.
- **Pandas** for data handling.
- **Plotly** for data visualization.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Midnight-W4lker/DataViz-Histogram-Tool.git
   cd DataViz-Histogram-Tool
   
2. Install required libraries:
   ```
   pip install -r requirements.txt
   
3. Run the app:
   ```
   python app.py
   
