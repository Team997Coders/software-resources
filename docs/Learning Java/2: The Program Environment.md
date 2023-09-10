Throughout this introduction to Java, we'll be providing examples and exercises for the reader. If you have a Java environment already set up, you should follow along in it to build familiarity. Otherwise, an interactive Java environment will be provided for you to work with.

<body>
  <div data-pym-src='https://www.jdoodle.com/plugin' data-language="java"
    data-version-index="4">public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}  </div>
  <script src="https://www.jdoodle.com/assets/jdoodle-pym.min.js" type="text/javascript"></script>
</body>

## Hello World!
Writing "Hello World!" to the output is the traditional first task when learning a new programming language.

### The Entry Point
Most of the above looks like gibberish right now. Public static void? String[] args? You don't need to know what they mean right now, just that this combination of words and symbols tells the compiler that your program should start by running whatever is inside the innermost curly brackets. Java will expect the above code to be in a file called "Main.java" (this doesn't matter for online compiler users).

### System.out.println()
This function is very useful in a testing or teaching environment. It simply prints whatever variable you pass to it, followed by a line break. It is the easiest way to quickly see the output of a program.

### Executing the Code
Online compiler users can just press the execute button, of course.

If you're off in your own Java environment, you need to take a few extra steps. In the terminal, make sure you're in the same working directory as your .java source file. Then run:
```
$ javac <YOUR FILE>.java
$ java <YOUR FILE>
```
There should be no file extension for the second option.

If you run into a problem such as "Command javac not found", Java likely either a) isn't installed, or b) isn't on your PATH. See [Setting Up Your Programming Environment](../Setting Up Your Programming Environment/index.md) for help.