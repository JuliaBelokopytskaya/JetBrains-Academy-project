Description:
1. Accept a command-line argument which is a directory for saved tabs. For example, if the argument is dir, then you need to create a folder with the name dir and save all the web pages that the user downloads in this folder. Note that if the folder already exists, FileExistsError will be raised. Hence, before creating the directory, you should check whether it's been already created, for example, via the os.access() function. If the folder exists, you don't need to do anything at this step.
Check if the user has entered a valid URL. It must contain at least one dot, for example, bloomberg.com. If the URL is incorrect, the browser should output an error message (it should contain the word error) and wait for another URL. If the URL is valid, print the content of the web page and save it to a file in the aforementioned directory. 
Read the next input. If this input is the string exit, the program should stop running. If not, check if the string corresponds to the name of any file with a web page you saved before. If it does, print the content of this file. If it doesn't, check if the string is a new valid URL.
2. The program should show the previous web page saved to a file if the user types back. Note that the last page you saved to a file is actually the current page; when the user types back, you should output the page that was before the current one. You can implement a stack to do this, but note that the current page should not be in that stack. For example, if the user inputs bloomberg.com, then nytimes.com, and then back, the user should see the content of bloomberg.com.
3. Your program should read the URL from the input, output the content of a real web page. Output the page with all the tags and text inside them. We'll get rid of tags in the next stage. Since the user can input the URL without https:// in the beginning, your browser should append this string if it is not there.
4. No more <div>, <script>, <p> and so on, just a clear readable text! Your browser should display only the content of a limited list of tags (<p>, headers, <a> and <ul>, <ol>, <li>) without showing the tags themselves.
Use the library beautifulsoup4 to make these changes. This library is already installed in your project.
5. Each link should start with a new line and be highlighted with blue color.