import json

def convert_to_html(json_content, css):
    html_messages = []
    
    # Adding a CSS link to the HTML header
    html_messages.append(f'<link rel="stylesheet" type="text/css" href="{css}">')
    
    for conversation in json_content:
        title = conversation["title"]
        html_messages.append(f'<h1>{title}</h1>')
        for key, value in conversation["mapping"].items():
            message = value.get("message")
            if message:
                author_role = message["author"]["role"]
                content_parts = message["content"]["parts"]
                for part in content_parts:
                    html_messages.append(f'<div class="{author_role}">{part}</div>')
    
    return "\n".join(html_messages)

if __name__ == "__main__":
    with open("pages/conversations.json", "r") as f:
        json_content = json.load(f)

    css = "style/chatstyle.css"
    html_content = convert_to_html(json_content, css)

    with open("pages/conversation.html", "w") as f:
        f.write(html_content)

    print("HTML conversion completed!")
