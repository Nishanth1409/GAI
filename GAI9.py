from pydantic import BaseModel
import wikipediaapi
class InstitutionDetails(BaseModel):
	name: str
	founder: str
	founded: str
	branches: int
	employees: int
	summary: str
institution_name = "PESITM"
user_agent = "YourAppName/1.0 (your-email@example.com)"
wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
page = wiki.page(institution_name)
summary = page.summary[:500] 
details = InstitutionDetails(
	name = institution_name,
	founder = "John Harvard",
	founded = "1636",
	branches = 12,
	employees = 20000,
	summary = summary	
)
print(details.model_dump_json())  