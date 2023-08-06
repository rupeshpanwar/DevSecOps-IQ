# Open and read the text file
with open("raw/k8s-qs.txt", 'r') as f:
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
for i in range(0, len(lines), 2):
    question = lines[i].strip()
    # Check if there is an answer line before trying to access it
    if i + 1 < len(lines):
        answer = lines[i+1].strip()
        html_content += f'<div class="qa-section"><div class="question"><h3>{question}</h3></div>'
        html_content += f'<div class="answer"><p>{answer}</p></div></div>'
    else:
        # If there is no answer, you can leave it blank or add a placeholder
        html_content += f'<div class="qa-section"><div class="question"><h3>{question}</h3></div>'
        html_content += f'<div class="answer"><p>No answer provided.</p></div></div>'

# Close the HTML tags
html_content += """
    </div>
</body>
</html>
"""

# Write the HTML content to a new HTML file
with open("pages/K8s-Qs.html", 'w') as f:
    f.write(html_content)
