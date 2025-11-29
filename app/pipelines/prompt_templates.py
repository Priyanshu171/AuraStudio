from jinja2 import Template

BLOG_TEMPLATE = Template("""
Write a {{ format }} article titled "{{ title }}" for {{ audience }}.
Tone: {{ tone }}.

Structure:
- Intro (80–120 words)
- 4 sub-headings, each with 2 short paragraphs
- Conclusion with a CTA
- Provide 3 social captions + 3 hashtags
""")

SOCIAL_TEMPLATE = Template("""
Write 6 short social media posts about "{{ title }}".
Tone: {{ tone }}.
2 promotional, 2 educational, 2 quick tips.
Max 280 characters each.
""")
