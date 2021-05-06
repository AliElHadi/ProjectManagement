About:
‘Project Management’ is a tool for managers to assign employees to projects without conflict, 
with the option to check lists and reports on the latter.

More details about the functionalities:

A. Employee related:
	Add Employee: add employee with his/her ID and needed information.
	Delete Employee: delete employee using employee ID.
	Get List of employees: 
		First list shows all employees.
		Second list shows all unassigned employees.

B. Project related:
	Add Project: add project with its ID and needed information.
	Delete Project: delete project using project ID.
	Get list of projects:
		First list shows assigned projects.
		Second list shows unassigned projects.
		Third list shows finished (completed) projects.
	Change status of project to finished: this would add it to finished projects list, 
	would make its corresponding employees unassigned, 
	and would increment the number of finished projects for each employee by 1.


C. Matching related:
	Match unassigned projects to unassigned employees.


D. Reports related:
	Show report for a specific employee.
	Show report for a specific project.


E. Other:
	Sign in.
	Sign up.


Installation and other requirements:
	Need to install Python and Django.
	Need to include desired employees and projects’ images in ‘static’ folder.
