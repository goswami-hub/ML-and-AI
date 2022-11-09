
# Bio-Medical Text Clustering
Historical clinical data is of immense importance today. It is important to study and understand the key challanges in historical trial to get an fair understanding about the requirements of the new trials:
- Sub-groups
- Effect size
- Sample size
- Competitor performance (aka competive intelligence)
There are repositories (e.g. [ClinicalTrials.gov](https://clinicaltrials.gov/)) that collects such data in a regular fashion. It is an obligation to submit key information of each and every regulatory trial in such websites. Therefore, these are key resources to collect information. However, the data is stored here as unstructed text. Threfore, extracting the right information from right trial is a key challenge.
## Our Approach
Patient characteristics of a trial is described under Inclusion/ Exclusion domains. Therefore, major sub group criteria can be extracted using these section to filter out right trial as per desired experiments. Step 1, of this project is to use inclusion, exclusion criteri tio find major patient sub-groups of interest.
We start with a particular domain (e.g. Breast cancer). Let us explore a way to find major patient characteristics of importance studied in this domain. In order to address this, we follow these steps below:
1. Extract Inclusion/ Exclusion criteria
2. Use these text to find meaningful clusters 
3. Derive a model to extract trials as per custom requirement
  - Custom requirement : A single sub group or a collection of multiple sub groups
  - Custom requirement : A free text expression

This is an open end project with work in progress. 
