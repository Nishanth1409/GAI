from pydantic import BaseModel
import wikipediaapi

# Define the data model using Pydantic
class InstitutionDetails(BaseModel):
	name: str
	founder: str
	founded: str
	branches: int
	employees: int
	summary: str

# Fetch details of an institution (Harvard University as an example)
institution_name = "Harvard University"

# Define a user agent (a string identifying your request, following Wikipedia's policy)
user_agent = "YourAppName/1.0 (your-email@example.com)" # Replace with your app's name and your contact info

# Initialize the Wikipedia API object with the user agent
wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)

# Fetch the page
page = wiki.page(institution_name)

summary = page.summary[:500] # Fetching a summary (you can limit the length)

# Parse the institution details (example data)
details = InstitutionDetails(
	name = institution_name,
	founder = "John Harvard",
	founded = "1636",
	branches = 12,
	employees = 20000,
	summary = summary
)

# Output the details in JSON format using model_dump_json
print(details.model_dump_json())
