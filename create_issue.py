import sys
from jira import JIRA

def build_custom_issue(summary,assignee_name,description_path, 
    proj_key=\"JAB\",
                issue_type=\"Bug\",
                reporter_name=\"a.ovchinnikova\",
                priority=\"Medium\",
                labels=[]
                ):
    issue_fields = {
        \"project\"     : {\"key\": proj_key},
        \"issuetype\"   : {\"name\": issue_type},   # Bug Task Story Epic
        \"summary\"     : \"[REGRESS][{}] Тесты падают на регрессе\".format(summary),
        \"reporter\"    : {\"name\":reporter_name},
        \"description\" : open(description_path, \"r\").read(),
        \"priority\"    : {\"name\": priority}, # Highest High Medium Low Lowest Blocker
        \"labels\"      : labels,
        \"assignee\"    : {\"name\": assignee_name}
    }
    return issue_fields

def get_jira():
    jira_options = {\'server\': \'https://j-ymp.yadro.com\'}
    jira = JIRA(options=jira_options, basic_auth=(\"CI\", \"CI4YMP\"))
    return jira
    
def create_jira_issue(issue_fields):
    jira = get_jira()
    issue_result = jira.create_issue(issue_fields)
    return issue_result
    
input_values = sys.argv[1:]
create_jira_issue(build_custom_issue(input_values[0],input_values[1],input_values[2]))
