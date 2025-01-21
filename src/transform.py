import os
import json

def clean_and_transform(input_dir, output_dir):
    """
    Reads extracted text files, cleans and transforms JSON data, and saves as JSON files.
    """
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        with open(os.path.join(input_dir, file), 'r') as f:
            raw_data = f.read()
            job_data = json.loads(raw_data)
        
        # Perform schema transformation
        transformed_data = {
            "job": {
                "title": job_data.get("job_title"),
                "industry": job_data.get("job_industry"),
                "description": job_data.get("job_description"),
                "employment_type": job_data.get("job_employment_type"),
                "date_posted": job_data.get("job_date_posted"),
            },
            "company": {
                "name": job_data.get("company_name"),
                "link": job_data.get("company_linkedin_link"),
            },
            "education": {
                "required_credential": job_data.get("job_required_credential"),
            },
            "experience": {
                "months_of_experience": job_data.get("job_months_of_experience"),
                "seniority_level": job_data.get("seniority_level"),
            },
            "salary": {
                "currency": job_data.get("salary_currency"),
                "min_value": job_data.get("salary_min_value"),
                "max_value": job_data.get("salary_max_value"),
                "unit": job_data.get("salary_unit"),
            },
            "location": {
                "country": job_data.get("country"),
                "locality": job_data.get("locality"),
                "region": job_data.get("region"),
                "postal_code": job_data.get("postal_code"),
                "street_address": job_data.get("street_address"),
                "latitude": job_data.get("latitude"),
                "longitude": job_data.get("longitude"),
            },
        }

        # Save transformed data
        with open(os.path.join(output_dir, file.replace(".txt", ".json")), 'w') as f:
            json.dump(transformed_data, f, indent=4)
