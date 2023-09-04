import markdown2

def markdownToHTML(markdown_text):
    extras={
        'code-friendly': None,
        'fenced-code-blocks': None,

    }
    return markdown2.markdown(markdown_text, extras=extras)
