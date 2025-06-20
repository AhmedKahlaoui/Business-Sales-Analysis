# ☕ Coffee Bean Sales Analysis Dashboard

## 📊 Project Overview

This Business Intelligence (BI) project focuses on building an end-to-end sales analysis solution for a coffee bean business. It includes data cleaning, integration, warehousing, and visualization to uncover key insights regarding sales performance, customer demographics, and product trends.

The project culminates in an interactive **Power BI dashboard** to assist decision-makers in understanding and optimizing business operations.

## 🎯 Objectives

- Analyze customer buying behavior
- Identify top-performing products and regions
- Evaluate seasonal trends in sales
- Provide actionable business insights through KPIs

## 🔧 Tools & Technologies

- **Python (Pandas)**: Data extraction and transformation
- **PostgreSQL**: Data storage and querying
- **Power BI**: Visualization and dashboarding
- **Excel/CSV**: Intermediate data storage and sharing

## 🔁 ETL Process

**Extract**:
- Data collected from multiple CSV sources

**Transform**:
- Cleaning: handled missing values, fixed data types, removed duplicates
- Standardization: formatted columns, unified date formats
- Integration: merged datasets into a consolidated table

**Load**:
- Stored into CSV, Excel, and PostgreSQL for flexibility and robust querying

## 🏗️ Data Modeling

- **Star Schema** design
- **Fact Table**: `Orders` (OrderID, ProductID, CustomerID, Quantity, Date, etc.)
- **Dimension Tables**:
  - `Products` (Product info, coffee type)
  - `Customers` (Demographics, country)
  - `Time` (Day, Month, Year)

✅ **ROLAP (Relational OLAP)** architecture used for performance and scalability

## 📈 Dashboard Features (Power BI)

- **KPI Cards**: Profit, quantity ordered
- **Bar Charts**: Sales by region and coffee type
- **Line Charts**: Monthly/yearly sales trends
- **Maps**: Geographic distribution of customers
- **Filters**: Time, product type, region, customer demographics

## 💡 Key Insights

- **ARA coffee type** generates the most profit
- **Winter season** sees peak demand; **summer** needs targeted campaigns
- **US region** shows highest sales — marketing should focus here
- **Fidelity card** shows no significant sales lift — reallocate CRM efforts

## 🚧 Challenges & Lessons Learned

- Data consistency issues across sources resolved through rigorous cleaning
- Initial unfamiliarity with visualization tools overcome through practice
- Learned effective BI design principles (layout, interactivity, drill-downs)


