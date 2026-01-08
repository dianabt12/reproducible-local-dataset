# Command-Line Dataset Exploration Notes

1. Count the number of records in the 2022 dataset:
wc -l data/raw/records_2022.csv
This command counts how many lines (records) are present in the raw 2022 dataset.

2. Preview the structure and column names of the 2023 dataset:
head -n 5 data/raw/records_2023.csv
This command displays the header and first few rows for quick inspection.

3. Search for records containing a specific year in the date field:
grep "2023" data/raw/records_2023.csv
This command filters rows that include the year 2023 in the date field.

4. Extract the category column from the 2022 dataset:
cut -d',' -f3 data/raw/records_2022.csv > category_list.txt
This command extracts the third column (category) and redirects the output to a file.

5. Count the number of unique record identifiers:
cut -d',' -f1 data/raw/records_2022.csv | sort | uniq | wc -l
This pipeline counts the number of unique record IDs in the dataset.

