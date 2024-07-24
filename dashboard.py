import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime, timedelta
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide")

# Load custom CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
    }

 

    main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Generate sample data

# Real-Time Monitoring
def generate_real_time_data():
    time_index = pd.date_range(start=datetime.now() - timedelta(days=7), periods=60, freq="T")
    fuel_levels = np.random.uniform(30, 100, len(time_index))
    dispensing_data = np.random.uniform(100, 500, len(time_index))
    fleet_status = np.random.choice(['Idle', 'In Transit', 'Refueling'], len(time_index))
    locations = np.random.choice(['Terminal A', 'Terminal B', 'Terminal C'], len(time_index))
    temperature = np.random.uniform(15, 35, len(time_index))  # New column for temperature
    pressure = np.random.uniform(1, 5, len(time_index))  # New column for pressure
    humidity = np.random.uniform(30, 70, len(time_index))  # New column for humidity
    tank_capacity = np.random.uniform(500, 1000, len(time_index))  # New column for tank capacity

    df = pd.DataFrame({
        'DateTime': time_index,
        'Location': locations,
        'Fuel Levels (%)': fuel_levels,
        'Dispensing Data (kg)': dispensing_data,
        'Fleet Status': fleet_status,
        'Temperature (°C)': temperature,
        'Pressure (bar)': pressure,
        'Humidity (%)': humidity,
        'Tank Capacity (L)': tank_capacity
    })
    return df

# Operational Efficiency
def generate_operational_efficiency_data():
    time_index = pd.date_range(start="2024-07-01 00:00:00", periods=60, freq="T")
    equipment_status = np.random.choice(['Operational', 'Maintenance Needed', 'Fault'], len(time_index))
    maintenance_alerts = np.random.choice(['No Alert', 'Scheduled Maintenance', 'Malfunction Detected'], len(time_index))
    alert_descriptions = ['All systems normal', 'Scheduled maintenance required', 'Equipment malfunction detected']
    response_times = np.random.uniform(1, 10, len(time_index))  # New column for response time
    downtime = np.random.uniform(0, 2, len(time_index))  # New column for downtime
    maintenance_cost = np.random.uniform(100, 1000, len(time_index))  # New column for maintenance cost
    descriptions = [alert_descriptions[np.random.randint(0, 3)] for _ in range(len(time_index))]

    df = pd.DataFrame({
        'DateTime': time_index,
        'Equipment Status': equipment_status,
        'Maintenance Alerts': maintenance_alerts,
        'Alert Description': descriptions,
        'Response Time (hours)': response_times,
        'Downtime (hours)': downtime,
        'Maintenance Cost ($)': maintenance_cost
    })
    return df

# Environmental Impact
def generate_environmental_impact_data():
    time_index = pd.date_range(start="2024-07-01", periods=60, freq="D")
    emissions_reduction = np.random.uniform(0.1, 2.0, len(time_index))
    carbon_footprint = np.random.uniform(50, 300, len(time_index))

    df = pd.DataFrame({
        'Date': time_index,
        'Emissions Reduction (tonnes)': emissions_reduction,
        'Carbon Footprint (tonnes)': carbon_footprint
    })
    return df

# Financial Performance
def generate_financial_performance_data():
    time_index = pd.date_range(start="2024-07-01", periods=60, freq="D")
    cost_savings = np.random.uniform(5000, 20000, len(time_index))
    revenue = np.random.uniform(10000, 50000, len(time_index))

    df = pd.DataFrame({
        'Date': time_index,
        'Cost Savings ($)': cost_savings,
        'Revenue ($)': revenue
    })
    return df

# Supply Chain
def generate_supply_chain_data():
    time_index = pd.date_range(start="2024-07-01", periods=60, freq="D")
    supply_chain_status = np.random.choice(['On Schedule', 'Delayed', 'Completed'], len(time_index))
    inventory_levels = np.random.uniform(1000, 5000, len(time_index))

    df = pd.DataFrame({
        'Date': time_index,
        'Supply Chain Status': supply_chain_status,
        'Inventory Levels (kg)': inventory_levels
    })
    return df

# Custom color formatting function for Fleet Status
def color_fleet_status(val):
    color = {
        'Idle': 'darkgreen',
        'In Transit': 'darkblue',
        'Refueling': 'orange'
    }.get(val, '')
    return f'background-color: {color}'

# Custom color formatting function for Maintenance Alerts
def color_maintenance_alerts(val):
    color = {
        'No Alert': 'darkgreen',
        'Scheduled Maintenance': 'gold',
        'Malfunction Detected': 'red'
    }.get(val, '')
    return f'background-color: {color}'

# Generate data
real_time_data = generate_real_time_data()
operational_efficiency_data = generate_operational_efficiency_data()
environmental_impact_data = generate_environmental_impact_data()
financial_performance_data = generate_financial_performance_data()
supply_chain_data = generate_supply_chain_data()

# AI-powered insights generation function
def generate_ai_insights(data):
    if data.empty:
        return {
            'Average Fuel Level': 'No data',
            'Max Dispensed Data': 'No data',
            'Most Common Fleet Status': 'No data',
            'Average Temperature': 'No data',
            'Trend in Fuel Levels': 'No data',
            'Peak Fuel Consumption Time': 'No data'
        }, ["No data available for recommendations."]

    avg_fuel_level = data['Fuel Levels (%)'].mean()
    max_dispensed = data['Dispensing Data (kg)'].max()
    most_common_status = data['Fleet Status'].mode()[0] if not data['Fleet Status'].mode().empty else 'No data'
    avg_temp = data['Temperature (°C)'].mean()
    trend_fuel_levels = 'increasing' if data['Fuel Levels (%)'].iloc[-1] > data['Fuel Levels (%)'].iloc[0] else 'decreasing'
    peak_consumption_time = data.groupby(data['DateTime'].dt.hour)['Dispensing Data (kg)'].sum().idxmax()

    insights = {
        'Average Fuel Level': f'{avg_fuel_level:.2f}%',
        'Max Dispensed Data': f'{max_dispensed:.2f} kg',
        'Most Common Fleet Status': most_common_status,
        'Average Temperature': f'{avg_temp:.2f}°C',
        'Trend in Fuel Levels': f'Fuel levels are {trend_fuel_levels} over the week.',
        'Peak Fuel Consumption Time': f'Peak fuel consumption occurs at {peak_consumption_time}:00 hours.'
    }

    # Generate detailed recommendations
    recommendations = [
        "Consider scheduling refueling during off-peak hours to reduce wait times.",
        "Monitor temperature variations closely as they may affect fuel efficiency. A higher average temperature can lead to increased fuel consumption.",
        f"With fuel levels {trend_fuel_levels}, ensure to adjust the storage accordingly to avoid shortages or excess.",
        "Increase the frequency of maintenance checks for fleets frequently in transit to ensure optimal performance.",
        f"Peak fuel consumption occurs at {peak_consumption_time}:00 hours. Schedule maintenance and refueling tasks around this time to avoid operational delays.",
        "Optimize fuel storage locations based on dispensing data trends to improve efficiency and reduce transportation costs."
    ]
    
    return insights, recommendations

# Streamlit app

# Sidebar for navigation
st.sidebar.title("Select Dashboard")
option = st.sidebar.selectbox("Select Dashboard", 
                              ["Real-Time Monitoring", "Operational Efficiency", "Environmental Impact", "Financial Performance", "Supply Chain"])

# Display data based on selection
if option == "Real-Time Monitoring":
    st.header("Real-Time Monitoring Dashboard")
    st.write("Fuel Levels, Dispensing Data, Fleet Tracking")
    
    # Color code the Fleet Status
    styled_data = real_time_data.style.applymap(color_fleet_status, subset=['Fleet Status'])
    st.dataframe(styled_data)
    
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.line(real_time_data, x='DateTime', y='Fuel Levels (%)', title='Fuel Levels Over Time')
        fig1.update_xaxes(title_text='Time')
        fig1.update_yaxes(title_text='Fuel Levels (%)')
        st.plotly_chart(fig1)
        
    with col2:
        fig2 = px.line(real_time_data, x='DateTime', y='Dispensing Data (kg)', title='Dispensing Data Over Time')
        fig2.update_xaxes(title_text='Time')
        fig2.update_yaxes(title_text='Dispensing Data (kg)')
        st.plotly_chart(fig2)
    
    # AI-powered insights
    st.header("AI-Powered Insights")
    weekly_data = real_time_data[real_time_data['DateTime'] >= (datetime.now() - timedelta(days=7))]
    insights, recommendations = generate_ai_insights(weekly_data)
    
    with st.container():
        st.markdown('<div class="highlight-container">', unsafe_allow_html=True)
        st.subheader("Insights")
        for key, value in insights.items():
            st.write(f"**{key}**: {value}")
        st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="highlight-container">', unsafe_allow_html=True)
        st.subheader("Recommendations")
        for recommendation in recommendations:
            st.write(f"- {recommendation}")
        st.markdown('</div>', unsafe_allow_html=True)

elif option == "Operational Efficiency":
    st.header("Operational Efficiency Dashboard")
    st.write("Equipment Status, Maintenance Alerts")
    
    # Color code the Maintenance Alerts
    styled_data = operational_efficiency_data.style.applymap(color_maintenance_alerts, subset=['Maintenance Alerts'])
    st.dataframe(styled_data)
    
    col1, col2 = st.columns(2)
    with col1:
        equipment_status_count = operational_efficiency_data['Equipment Status'].value_counts().reset_index()
        equipment_status_count.columns = ['Equipment Status', 'Count']
        fig1 = px.bar(equipment_status_count, x='Equipment Status', y='Count', title='Equipment Status Count')
        st.plotly_chart(fig1)
        
    with col2:
        maintenance_alerts_count = operational_efficiency_data['Maintenance Alerts'].value_counts().reset_index()
        maintenance_alerts_count.columns = ['Maintenance Alerts', 'Count']
        fig2 = px.bar(maintenance_alerts_count, x='Maintenance Alerts', y='Count', title='Maintenance Alerts Count')
        st.plotly_chart(fig2)

elif option == "Environmental Impact":
    st.header("Environmental Impact Dashboard")
    st.write("Emissions Reduction, Carbon Footprint")
    
    st.dataframe(environmental_impact_data)
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.line(environmental_impact_data, x='Date', y='Emissions Reduction (tonnes)', title='Emissions Reduction Over Time')
        fig1.update_xaxes(title_text='Date')
        fig1.update_yaxes(title_text='Emissions Reduction (tonnes)')
        st.plotly_chart(fig1)
        
    with col2:
        fig2 = px.line(environmental_impact_data, x='Date', y='Carbon Footprint (tonnes)', title='Carbon Footprint Over Time')
        fig2.update_xaxes(title_text='Date')
        fig2.update_yaxes(title_text='Carbon Footprint (tonnes)')
        st.plotly_chart(fig2)

elif option == "Financial Performance":
    st.header("Financial Performance Dashboard")
    st.write("Cost Analysis, Revenue Tracking")
    
    st.dataframe(financial_performance_data)
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.line(financial_performance_data, x='Date', y='Cost Savings ($)', title='Cost Savings Over Time')
        fig1.update_xaxes(title_text='Date')
        fig1.update_yaxes(title_text='Cost Savings ($)')
        st.plotly_chart(fig1)
        
    with col2:
        fig2 = px.line(financial_performance_data, x='Date', y='Revenue ($)', title='Revenue Over Time')
        fig2.update_xaxes(title_text='Date')
        fig2.update_yaxes(title_text='Revenue ($)')
        st.plotly_chart(fig2)

    cost_savings_total = financial_performance_data['Cost Savings ($)'].sum()
    revenue_total = financial_performance_data['Revenue ($)'].sum()
    other_costs = 100000  # Example of other costs

    pie_data = pd.DataFrame({
        'Category': ['Cost Savings', 'Other Costs'],
        'Amount': [cost_savings_total, other_costs]
    })

    pie_chart_costs = px.pie(pie_data, values='Amount', names='Category', title='Cost Analysis')
    st.plotly_chart(pie_chart_costs)

    revenue_data = pd.DataFrame({
        'Category': ['Revenue', 'Other Income'],
        'Amount': [revenue_total, 50000]  # Example of other income
    })

    pie_chart_revenue = px.pie(revenue_data, values='Amount', names='Category', title='Revenue Tracking')
    st.plotly_chart(pie_chart_revenue)

elif option == "Supply Chain":
    st.header("Supply Chain Dashboard")
    st.write("Hydrogen Supply Chain, Inventory Management")
    
    st.dataframe(supply_chain_data)
    col1, col2 = st.columns(2)
    with col1:
        st.write(supply_chain_data['Supply Chain Status'].value_counts())
    with col2:
        fig1 = px.line(supply_chain_data, x='Date', y='Inventory Levels (kg)', title='Inventory Levels Over Time')
        fig1.update_xaxes(title_text='Date')
        fig1.update_yaxes(title_text='Inventory Levels (kg)')
        st.plotly_chart(fig1)
