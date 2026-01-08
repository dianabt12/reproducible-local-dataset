# File Formats and Schema Evolution Notes

The raw datasets are kept unchanged in their original CSV format to preserve the source data exactly as provided by the instructor.  
During processing, the cleaned dataset is also exported to JSON format to improve interoperability and ease of use in downstream applications.  
JSON was chosen because it is widely supported, human-readable, and suitable for structured data exchange.  
The schema of the processed data is standardized during cleaning, including normalized column names, consistent date formats, and cleaned categorical values.  
No raw fields are removed, however, missing values are handled explicitly and invalid records are corrected or flagged during processing.

