# Spartan Robotics Software Resources
Software documentation for Spartan Robotics.

## [View on GitHub Pages!](https://team997coders.github.io/software-resources/)

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

## Contributing
This project uses [MkDocs](https://www.mkdocs.org/) with the [Material](https://squidfunk.github.io/mkdocs-material/) theme. Both sites contain plenty of documentation information.

The docs are written in Markdown, which is very close to plain text and easy to pick up. [This manual](https://www.markdownguide.org/) is an excellent reference source. Be aware that a few extended syntax features may not actually work with MkDocs.

### Working Locally
It's a good idea to check the rendering of your documentation before committing it. A local setup can be done pretty easily, thankfully.

Start by installing the python requirements:
```
pip install -r requirements.txt
```

And then render an automatically-refreshing output to `127.0.0.1.8000`:
```
mkdocs serve
```

It's that easy!

### Adding New Pages
New pages can be added by creating a .md file somewhere in the `docs` directory. Follow the pattern shown at the bottom of `mkdocs.yml` to add them to the navigation sidebar.

### MathJax/LaTeX
Math expressions are supported, using the MathJax Javascript library. LaTeX is a complicated beast, but we only use its math expression syntax. [MathJax's LaTeX documentation](https://docs.mathjax.org/en/latest/input/tex/index.html) is a good place to start.

### Mermaid2
Mermaid is a very slick library for generating charts, using similar syntax to Markdown. Documentation on using Mermaid in MkDocs can be found [here](https://mkdocs-mermaid2.readthedocs.io/en/latest/), and general Mermaid information at [the official site](https://mermaid.js.org/community/n00b-overview.html).

### Macros
Markdown doesn't support a few things that we want to do in our documentation, notably the embedded compiler and spoiler tags for code. Instead, we have to use raw HTML. Macros help with this process-- instead of manually adding all the tags ourselves, we can call a macro which applies the proper tags. The macros are processed before Markdown is turned into HTML and before HTML is rendered, so the generated text is just as real to them as anything else.

Macros are written in Python, and live inside the main.py file. That file should be formatted with [black](https://github.com/psf/black) (`black .`).

Invoking a macro is done with `{{ macroName(arg1, arg2, ...)}}`. Further documentation can be found [here](https://mkdocs-macros-plugin.readthedocs.io/en/latest/pages/).