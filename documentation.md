# The Commerce Platform

The Commerce Platform is a project to centralize all Commerce-related tools, helping the Media teams and their clients discover, plan, activate and measure their Commerce campaigns.

# The apps

## Commerce: Insights

### Overview

The Commerce Insights app is a tool that helps the Media teams and their clients to easily get access to insightful data about the Commerce landscape, whether it is about the market, the competition, the retailers, their brands, the products or audiences.
Each of these sections will have their own tab, themselves regrouping set of data, charts and insights, and the user will be able to navigate through them to get the information they need.
There will be main filters that will apply across all tabs, but also chart-specific filters that will allow the user to refine the data they are looking at. Chart-specific filters will always overwrite the main filters. The values selected in the main filters will also determine what values can be selected in the chart-specific filters: for example, if the user selects a specific retailer in the main filters, they will only be able to select products from this retailer in the chart-specific filters.

The charts will either be sourced from one source, or a combination of sources, and will be displayed in a way that is easy to understand and interpret. The user will be able to download the data behind the charts.
More details about the datasources here.


### The different analysis

#### Scorecards

#### RPM

### Scorecards - Admin panel

The Scordecards - Admin panel, previously known as "Flow" in Fusion, is an interface for Admin users to create, send and score Retailer RFIs.
RFIs are questionnaires sent to retailers to gather information about their Media platform, for a specific market, through about 500 questions.

95% of the time, the same RFI (Retail Media Network Capabilities RFI) is sent to all retailers. 
But it may happen that a specific client wants to add their own questions. In this case, we need to allow the possibility of creating a new RFI.

#### Create a new RFI
Users can create a new RFI, usually by copying an existing one and modifying it. They can add questions, sections, and change the order of the questions.
A question is defined by : Category, Subcategory, Question, Type (Freeform, Single Select, MultiSelect, File Upload), Answer, Weight, and Mandatory.

#### Send an RFI
Once an RFI is created, users can send it to retailers in a few different steps.
- User clicks on "Create Flow"
- User selects the RFI, the Flow's admins, and the dates the answers are due
- User selectes the partner retailer, the market, and the contact person to which that RFI is directed.
- User clicks send, and the questionnaire is sent to the retailer, through a Google Form. The link to the Google Form contains a token, which allows to identify the retailer and the RFI.

#### Score an RFI
Once the answers are received, the user can score the RFI. 
The user has to go through each of the 500 questions one by one, and based on the answers, give a score.
Since the answers are not provided under a "quantitative" form, the user has to interpret the answers and give a score based on their interpretation, which is a really manual process, as well as fairly subjective.




## General considerations

### User authentication

### Saving user preferences