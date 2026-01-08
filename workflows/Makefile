.PHONY: all clean

all: data/processed/cleaned_records.csv reports/summary.md

data/processed/cleaned_records.csv: data/raw/records_2022.csv data/raw/records_2023.csv src/clean.py
	python src/clean.py

reports/summary.md: data/processed/cleaned_records.csv src/report.py
	python src/report.py

clean:
	rm -f data/processed/*
	rm -f reports/*

