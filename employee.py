
import chromadb
import uuid


client = chromadb.Client()

collection = client.create_collection(
    name = "employee_collection",
    metadata = {"description" : "A collection for storing employee data"}
)

# Defining a list of employee dictionaries
# Each dictionary represents an individual employee with comprehensive information
employees = [
    {
        "id": "employee_1",
        "name": "John Doe",
        "experience": 5,
        "department": "Engineering",
        "role": "Software Engineer",
        "skills": "Python, JavaScript, React, Node.js, databases",
        "location": "New York",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_2",
        "name": "Jane Smith",
        "experience": 8,
        "department": "Marketing",
        "role": "Marketing Manager",
        "skills": "Digital marketing, SEO, content strategy, analytics, social media",
        "location": "Los Angeles",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_3",
        "name": "Alice Johnson",
        "experience": 3,
        "department": "HR",
        "role": "HR Coordinator",
        "skills": "Recruitment, employee relations, HR policies, training programs",
        "location": "Chicago",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_4",
        "name": "Michael Brown",
        "experience": 12,
        "department": "Engineering",
        "role": "Senior Software Engineer",
        "skills": "Java, Spring Boot, microservices, cloud architecture, DevOps",
        "location": "San Francisco",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_5",
        "name": "Emily Wilson",
        "experience": 2,
        "department": "Marketing",
        "role": "Marketing Assistant",
        "skills": "Content creation, email marketing, market research, social media management",
        "location": "Austin",
        "employment_type": "Part-time"
    },
    {
        "id": "employee_6",
        "name": "David Lee",
        "experience": 15,
        "department": "Engineering",
        "role": "Engineering Manager",
        "skills": "Team leadership, project management, software architecture, mentoring",
        "location": "Seattle",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_7",
        "name": "Sarah Clark",
        "experience": 8,
        "department": "HR",
        "role": "HR Manager",
        "skills": "Performance management, compensation planning, policy development, conflict resolution",
        "location": "Boston",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_8",
        "name": "Chris Evans",
        "experience": 20,
        "department": "Engineering",
        "role": "Senior Architect",
        "skills": "System design, distributed systems, cloud platforms, technical strategy",
        "location": "New York",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_9",
        "name": "Jessica Taylor",
        "experience": 4,
        "department": "Marketing",
        "role": "Marketing Specialist",
        "skills": "Brand management, advertising campaigns, customer analytics, creative strategy",
        "location": "Miami",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_10",
        "name": "Alex Rodriguez",
        "experience": 18,
        "department": "Engineering",
        "role": "Lead Software Engineer",
        "skills": "Full-stack development, React, Python, machine learning, data science",
        "location": "Denver",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_11",
        "name": "Hannah White",
        "experience": 6,
        "department": "HR",
        "role": "HR Business Partner",
        "skills": "Strategic HR, organizational development, change management, employee engagement",
        "location": "Portland",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_12",
        "name": "Kevin Martinez",
        "experience": 10,
        "department": "Engineering",
        "role": "DevOps Engineer",
        "skills": "Docker, Kubernetes, AWS, CI/CD pipelines, infrastructure automation",
        "location": "Phoenix",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_13",
        "name": "Rachel Brown",
        "experience": 7,
        "department": "Marketing",
        "role": "Marketing Director",
        "skills": "Strategic marketing, team leadership, budget management, campaign optimization",
        "location": "Atlanta",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_14",
        "name": "Matthew Garcia",
        "experience": 3,
        "department": "Engineering",
        "role": "Junior Software Engineer",
        "skills": "JavaScript, HTML/CSS, basic backend development, learning frameworks",
        "location": "Dallas",
        "employment_type": "Full-time"
    },
    {
        "id": "employee_15",
        "name": "Olivia Moore",
        "experience": 12,
        "department": "Engineering",
        "role": "Principal Engineer",
        "skills": "Technical leadership, system architecture, performance optimization, mentoring",
        "location": "San Francisco",
        "employment_type": "Full-time"
    },
]

# create a doc for each employee
employee_docs = []

# for semantic search.
for employee in employees:
    document = f"{employee['role']} with {employee['experience']} years of experience in {employee['department']}. "
    document += f"Skills: {employee['skills']}. Located in {employee['location']}. "
    document += f"Employment type: {employee['employment_type']}."
    employee_docs.append(document)


#add docs to collections with metadata
collection.add(
    ids = [employee['id'] for employee in employees],
    documents = employee_docs,
    metadatas = [
        {
            "name": employee['name'],
            "experience": employee['experience'],
            "department": employee['department'],
            "role": employee['role'],
            "skills": employee['skills'],
            "location": employee['location'],
            "employment_type": employee['employment_type']
        }
        for employee in employees
    ]
)

# fetches all data in collection
all_items = collection.get()


def similarity_search_examples():

    # python devs
    result = collection.query(
        query_texts = "Python developer with web dev experience",
        n_results = 3
    )
    print(result['documents'])
    print(f"\n")

    # leadership_roles
    result = collection.query(
        query_texts = "Team leader manager with experience",
        n_results = 3
    )
    print(result['documents'])
    print(f"\n")


def metadata_filter_examples():

    # by experience
    result = collection.get(
        where = {
            "experience" : {"$gte" : 10}
        }
    )
    print(result['documents'])
    print(f"\n")
    # by location
    result = collection.get(
        where = {
            "location" : {"$in" : ["Los Angeles", "San Francisco"] }
        },
    )
    print(result['documents'])
    print(f"\n")
    # by department
    result = collection.get(
        where = {
            "department" : {"$eq" : "HR"}
        }
    )
    print(result['documents'])
    print(f"\n")

def metadata_similarity_examples():

    # Example: Find experienced Python developers in specific locations [seattle, new york, san francisco] with exp >=8
    result = collection.query(
        query_texts = "senior python developer ",
        n_results = 3,

        where = {
            "$and" : [
                {"experience" : {"$gte" : 8}},
                {"location" : {"$in" : ["New York", "San Francisco", "Seattle"]}}
            ]
        }
    )
    print(result['documents'])
    print(f"\n")


def run_examples():

    similarity_search_examples()
    metadata_filter_examples()
    metadata_similarity_examples()


if __name__ == "__main__":
    run_examples()



