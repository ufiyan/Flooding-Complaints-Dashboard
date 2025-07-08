# Assignment 4: Interactive Visualization of Flooding Complaints in Chicago (2018–2025)
![website](images/website.gif) 


![interface](images/interface1.png) 
## Live Dashboard
[Click here to view the interactive visualization](https://mayesh3.github.io/visualMinds-deployment-repo/)


## Dataset Description
Each year 311 receives thousands of complaints about flooding. This dataset includes over **85,000 flooding complaints** reported to Chicago’s 311 system between **2018 and 2025**. These complaints came from phone calls, online reports, and service requests.

Each record includes information like:

- **Type of flooding** (e.g., water in basement or on street)
- **Date** the complaint was made 
- **Location**, including **ZIP code**, **street name**, and **GPS coordinates**
- **Police district** and **city department** assigned to the case
- **Submission method** (phone, internet, mobile app)
- **Status** of the request


This data helps city officials identify flood-prone areas, improve infrastructure, and plan emergency responses. It also gives communities the tools to push for better flood prevention efforts.

## Chart Descriptions
---

![Linked stack](images/linkedStackBar.gif)   
*This interactive view links a stacked area chart (top) with a stacked bar chart (bottom). Users can brush over a time range to filter monthly flood complaint data by ZIP code, making it easy to explore local spikes during selected months.*

### Attributes Being Visualized
- YearMonth: The month and year of each flooding complaint.  
- ZIP_CODE: The location of the complaint.  
- count: The number of flooding complaints filed in each ZIP code per month.

### Motivation and Rationale
The goal of this visualization is to provide a more detailed view of complaint patterns across neighborhoods in a specific time range. While the stacked area chart shows temporal trends overall, this chart allows users to investigate which ZIP codes are driving spikes or drops in complaint volume during specific months.  
By breaking the bars down by ZIP codes, we show a more detailed understanding of which neighborhoods are most affected in a given time window.

### Interaction Mechanisms and Methods
This visualization is linked to the stacked area chart above using an interval selection in which users can:  
- Click and drag on the area chart to select a time range.  
- The bar chart below then filters to only include data from the selected months.  
- The bars are stacked by ZIP code which provides visual clarity into regional distributions over time.

This technique uses:  
- brush selection type (interval) on the x-axis  
- filter transform in the bar chart based on that brush selection  
- groupby aggregation by both ParsedDate and ZIP_CODE

### Design Decisions
- Stacked Bars: Chosen to visualize both total volume and more specific breakdowns simultaneously.  
- X-axis formatted mm/yyyy: YearMonth was parsed into ParsedDate.  
- Color Encoding: ZIP codes are assigned distinct colors and they match their appearance in the stacked area chart.

### Insights Gained
Using brushing from the area chart made it possible to explore localized spikes. For example, if a user selects July - August 2023, they can immediately see which ZIPs had the most flooding and the total flooding during that time.  
A stacked bar chart is more compact and interpretable than a grouped bar chart when analyzing 10 ZIPs across multiple months.  
The link between the overview chart and this detail chart provides a strong foundation for data interpretation.

---

![Choropleth](images/chloropleth.png)

*This choropleth map visualizes total flooding complaints across Chicago ZIP codes. Darker shades represent areas with higher complaint counts, helping identify the most flood-prone neighborhoods at a glance.*

### Attributes Being Visualized
- **ZIP_CODE**: Shows general location using ZIP boundaries (choropleth)  
- **Latitude and Longitude**: Specific location of each flooding complaint (scatter plot)  
- **Complaint Count**: Total number of complaints per ZIP (color scale)

### Motivation and Rationale  
The goal of this visualization was to explore **where in Chicago flooding complaints are coming from**, and how **complaint density varies across the city**. By using both a **choropleth map** and a **dot density scatter plot**, we get both a zoomed-out and zoomed-in view of the issue. The choropleth highlights which ZIP codes have the most complaints, while the scatter plot shows exact complaint locations at the street/block level.

### Interaction Mechanisms and Methods  
This visualization is **static**, but allows for **visual comparison** by offering two complementary views:  
- The **choropleth** gives a clear overview of high-complaint ZIP codes.  
- The **scatter plot** reveals precise clustering and hot spots at a finer scale.

We experimented with both encodings to find which view was clearer and more useful for spotting trends.

### Technique Summary  
- **Choropleth**:  
  - ZIP boundaries from a GeoJSON file  
  - Aggregated complaint counts grouped by ZIP  
  - Color intensity based on total complaints

- **Scatter Plot**:  
  - Individual complaint points plotted by latitude and longitude  
  - Random sample of ~12,000 points for performance  
  - Semi-transparent red dots to avoid overplotting

### Design Decisions  
- **Color Encoding**: Linear blue gradient in the choropleth (darker = more complaints)  
- **Geographic Projection**: Mercator projection used for consistent map layout  
- **Stroke & Borders**: ZIP outlines in black for visibility  
- **Dot Styling**: Scatter plot dots are small, red, and semi-transparent for density clarity  
- **Performance**: Dot map uses sampling to maintain speed while keeping visual accuracy  
- **Layout**: Maps set to 600×500 for balance and legibility

### Insights Gained  
- The **choropleth** made it clear which ZIP codes had the highest flooding complaint totals. ZIPs like **60644 and 60651** stood out immediately.  
- The **scatter plot** helped identify areas of high-density flooding at a more detailed, block-level scale.  
- While the dot plot offers pinpoint accuracy, the choropleth was **easier to interpret and less cluttered** for large-scale trends.  
- Combining both views gave a fuller picture of **where the city’s flooding issues are concentrated**, helping guide potential flood mitigation planning.
  
---

![Barchart](images/barchart.gif)  
*This interactive bar chart shows monthly flooding complaint totals for a selected year. Users can use the dropdown to view seasonal trends year by year, making it easier to spot patterns like spikes in late spring and summer months.*

### Attributes Being Visualized
- **Month**: Categorical (January through December)  
- **count**: Number of flooding complaints in each month  
- **YEAR**: Selected year from dropdown  

### Motivation and Rationale  
The goal of this chart is to explore **how flooding complaints vary across different months of the year**, and to compare those patterns across multiple years. It helps identify which months tend to experience more flooding problems, and whether that trend is consistent from year to year. This view is especially helpful for spotting seasonal spikes and unusual years.

### Interaction Mechanisms and Methods  
- Users can **select a year** from the dropdown menu.  
- The **bar chart updates** to show monthly complaint totals for the chosen year.  
- Hovering over each bar displays the exact number of complaints.

This technique uses:  
- **Selection binding** to `YEAR` through a dropdown  
- A **filter transform** to show only data from the selected year  
- **Month-level aggregation** to summarize the count values

### Design Decisions  
- **Bar Chart**: Chosen for clear comparison of complaint volume by month  
- **Consistent blue color**: Matches other charts in the dashboard  
- **X-axis labels**: Clearly labeled months for easy reading  
- **Dropdown control**: Simple and intuitive way to explore different years

### Insights Gained  
Most years show higher flooding complaints in **late spring and summer**, especially between **May and August**. The year **2023** had a noticeable spike during that time, which may be related to environmental changes or extreme weather. This chart makes it easy to spot yearly patterns and outliers at a glance.


---
![pareto](images/linkedPareto.gif)
*These two linked charts reveal which ZIP codes report the most flooding complaints. The Pareto chart highlights how a few ZIPs dominate the complaint totals, while the lollipop chart clearly shows complaint counts per group for direct comparison.*


### Attributes Being Visualized  
- **ZIP_CODE**: Where each complaint occurred  
- **count**: Total number of complaints per ZIP or group  
- **Cumulative % of complaints**: Shown as a line in the Pareto chart  
- **Group Selection**: Dropdown lets users switch between groupings (e.g., ZIP, SR Type)

### Motivation and Rationale  
The goal of these charts is to highlight **which areas are contributing the most to flooding complaints**. The **Pareto chart** shows how just a few ZIP codes make up the majority of issues, following the 80/20 rule. The **lollipop chart** provides a cleaner and more readable breakdown of complaint volume across all groups.

### Interaction Mechanisms and Methods  
- A **dropdown selector** lets users choose how to group the data (by ZIP, SR Type, etc.)  
- Both the **Pareto chart** and **lollipop chart** update based on the selected grouping  
- Hovering over chart elements shows details like complaint counts and percentages

This technique uses:  
- **Selection binding** to group type  
- **GroupBy aggregation** based on user selection  
- A **Pareto line** showing cumulative totals, paired with a bar chart  
- A **lollipop chart** for a simplified horizontal comparison

### Design Decisions  
- **Pareto Chart**: Combines bars and a line to show volume and build-up  
- **Lollipop Chart**: Used instead of full bars for better readability in dense categories  
- **Color Encoding**: Gradient or consistent tone used to highlight high-volume areas  
- **Dual View**: Shows both summary (Pareto) and full distribution (lollipop)

### Insights Gained  
- A few ZIP codes like **60644** and **60651** account for a large portion of flooding complaints  
- This confirms the around **20% of ZIPs contribute 45% of complaints**  
- 2023 saw significantly more flooding complaints than other years possibly due to heavy rainfall 

---
## Additional Insights and findings
- Peak complaint months May and surrounding months  
- Most years tend to have similar complaints  
- Clustering of complaints seems to be in poorer areas 

- According to [ZIP Atlas](https://zipatlas.com/us/il/chicago/zip-code-comparison/highest-poverty.htm), **only 3 of the top 10 ZIPs** are *not* in the top 15 poorest in Chicago (56 total)  
- All top 15 ZIPs fall below the **60th income percentile**  
- The **trend of repeated flooding complaints** in these areas suggests **little improvement in infrastructure** over time  



