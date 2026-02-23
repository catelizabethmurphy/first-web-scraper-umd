# physicians news app ideas — cat murphy, feb. 23

data cleaning tasks we would need to do: 
- collapse rows by provider
- lol, it would also be great to get the 2020 data
- scrape the pdfs of the disciplinary records from before 2017
- scrape the pdfs of the individual disciplinary records themselves
- clean the date column to compare the beginning of 2026 to the beginning of previous years
- create a categorized type column (fine, suspension, etc.)

so, the first thing here is that each row isn't necessarily an individual reprimand — it's a single action within the reprimand process for a given provider. but because the reprimand process can involve several steps, this means a single provider often appears in our dataset more than once. so, while there are over 1,800 rows in our dataset, there aren't actually that many providers.

and in the context of a news app, we would probably want to collapse the actions for an individual physician into a single row instead of having each action listed or displayed separately. that way we could create a "timeline" of sorts to show the progression and, when available, the outcome of a given reprimand. this would also allow us to show how long the reprimand process can take, and potentially what happens to a provider's ability to treat patients in the interim (i actually don't know what exactly this would show, but i think it could be interesting if there were patterns related to the type of offense, type of discipline, etc.). 

the other thing is that our dataset is missing a lot of information and/or it's inaccessible in the dataset's current form. the information about the offense itself, for instance, is locked away in the pdfs. for a news app, we would ideally want to scrape these files so that we could actually display what exactly these providers were disciplined for. this would also allow us to categorize offenses — something that could be helpful if we wanted users to be able to filter the reprimands by offense to display breakdowns by provider type, discipline type, severity, permanence, length, etc. this could also maybe show us if their punishment changed over the course of the process.

this news app could also display discipline over time. by faceting by name *and* year to get the number of unique cases each year, i can see that the number of disciplinary cases skyrocketed in 2024 but then dropped to its lowest level in 2025. but i would also want to know things about trends in the discipline — like we know cases are dropping, but is the percentage of suspensions going up? are fines increasing? are probation sentences longer? right now, it's kind of impossible to tell because the only meaningful field — type — isn't particularly facetable, per se. so we would want to clean the dataset in a way that would break up our current "type" column into fields that we could actually analyze and turn into a news app.

other things i would potentially want to see would be location, specialty, and how many of the cases involve out-of-state doctors surrendering their licenses because the state of maryland found out they received disciplinary action in another state (something i found a few instances of while looking through some of the records).