def define_env(env):
    @env.macro
    def compilerEmbed(code: str) -> str:
        return (
            "<body><div data-pym-src='https://www.jdoodle.com/plugin' data-language='java' data-version-index='4'>"
            + code
            + "</div></body>"
        )
    
    @env.macro
    def compilerEmbedEOF() -> str:
        return "<script src='https://www.jdoodle.com/assets/jdoodle-pym.min.js' type='text/javascript'></script>"

    @env.macro
    def entryPoint(code: str) -> str:
        indented: str = "\t\t".join(code.splitlines(True))
        return (
            "public class Main {\n\tpublic static void main(String[] args) {\n"
            + indented
            + "\n\t}\n}"
        )

    @env.macro
    def spoiler(hint: str, content: str) -> str:
        return (
            "<details><summary>"
            + hint
            + "</summary>"
            + content
            + "</details>"
        )