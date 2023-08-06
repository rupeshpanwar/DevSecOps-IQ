import os

# Open and read the text file
with open("raw/K8s-InterviewQs.txt", 'r') as f:
    lines = f.readlines()

# Prepare the HTML file content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Kubernetes Interview Questions</title>
    <link rel="stylesheet" href="../style/styles.css">
</head>
<body>
    <div class="sidebar">
        <a href="../index.html"><button>Main Page</button></a>
        <a href="argocd.html"><button>Argo CD</button></a>
        <a href="kubernetes.html"><button>Kubernetes</button></a>
        <a href="conversation.html"><button>InterviewQuestions</button></a>
    </div>
    <div class="main-content">
        <h1>Kubernetes Interview Questions</h1>
"""

# Add the Q&A sections to the HTML content
for line in lines:
    if line.startswith("Q:"):
        html_content += f'<div class="qa-section"><div class="question"><h3>{line[3:].strip()}</h3></div>'
    elif line.startswith("A:"):
        html_content += f'<div class="answer"><p>{line[3:].strip()}</p></div></div>'

# Close the HTML tags
html_content += """
    </div>
</body>
</html>
"""

# Write the HTML content to a new HTML file
with open("pages/K8s-InterviewQs.html", 'w') as f:
    f.write(html_content)
