from .prompt_templates import BLOG_TEMPLATE, SOCIAL_TEMPLATE

def build_prompt(req):
    if req.format == "blog":
        return BLOG_TEMPLATE.render(
            title=req.title,
            tone=req.tone,
            audience=req.audience,
            format=req.format
        )
    return SOCIAL_TEMPLATE.render(
        title=req.title,
        tone=req.tone
    )
