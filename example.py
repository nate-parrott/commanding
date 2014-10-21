"""
This is an example of commanding.py's parsing.
It's the set of commands for Astrobot (astro-bot.appspot.com),
a service for browsing the web over SMS.
Run the example and try some natural-language commands in the console.
For example,
"search the web for new york" returns
"[search: ['search the web for', ['~query', 'new york']]]"
"""

from commanding import Phrase, parse_phrase

examples = [
	Phrase("url", [["*url", "google.com"]]),
	Phrase("url", ["load", ["*url", "google.com"]]),
	Phrase("url", ["open", ["*url", "google.com"]]),
	Phrase("url", ["fetch", ["*url", "google.com"]]),
	Phrase("url", ["go to", ["*url", "google.com"]]),
	Phrase("url", ["show", ["*url", "google.com"]]),
	Phrase("search", ["search", ["~query", "hacker school"]]),
	Phrase("search", ["google", ["~query", "weather 11215"]]),
	Phrase("search", ["search the web for", ["~query", "kanye west"]]),
	Phrase("search", ["search for", ["~query", "hello world"]]),
	Phrase("search", ["search", ["search_source/wikipedia", "wikipedia"], "for", ["~query", "praying mantis"]]),
	Phrase("search", [["search_source/wikipedia", "wikipedia"], ["~query", "android"]]),
	Phrase("search", [["search_source/wikipedia", "show me the wikipedia article for"], ["~query", "the grateful dead"]]),
	Phrase("search", ["search", ["search_source/this_site", "this site"], "for", ["~query", "contact us"]]),
	Phrase("search", ["find", ["~query", "support"], "on", ["search_source/this_site", "this site"]]),
	Phrase("search", [["~query", "barack obama"]]),
	Phrase("more_text", ["more"]),
	Phrase("more_text", [["*number", "2"], "more pages"]),
	Phrase("more_text", [["*number", "3"], "more pages"]),
	Phrase("more_text", ["next"]),
	Phrase("more_text", ["next", ["*number", "4"]]),
	Phrase("previous_text", ["previous"]),
	Phrase("previous_text", ["last", ["*number", "3"]]),
	Phrase("previous_text", ["previous", ["*number", "7"], "messages"]),
	Phrase("previous_text", ["last part"]),
	Phrase("back_to_top", ["back to top of page"]),
	Phrase("navigate", ["click", ["*number", "6"]]),
	Phrase("navigate", [["*number", "7"]]),
	Phrase("navigate", [["*number", "7"]]),
	Phrase("navigate", [["*number", "7"]]),
	Phrase("navigate", ["click link", ["target", "hvuiehguo"]]),
	Phrase("navigate", ["click", ["target", "ihenigo"], ["on_last_page", "on last page"]]),
	Phrase("navigate", ["load", ["target", "jegotghr"], ["on_last_page", "from previous page"]]),
	Phrase("show_navigation", ["show navigation"]),
	Phrase("help", ["help me"]),
	Phrase("help", ["what are the options"]),
	Phrase("help", ["what can I say?"]),
	Phrase("summarize", ["summarize this page"]),
	Phrase("summarize", ["summarize", ["*number", "2"]]),
	Phrase("show summary for", ["*number", "3"]),
	Phrase("back", ["back"]),
	Phrase("whereami", ["where am i?"]),
	Phrase("whereami", ["what page am i on?"]),
	Phrase("whereami", ["current site"]),
	Phrase("contents", ["show me the table of contents"]),
	Phrase("contents", ["zoom out"]),
	Phrase("contents", ["list the headings on the page"])
]
regexes = {
"url": r"[a-zA-Z0-9_\-\.]+\.[a-z]+(\/[^ ]*)?",
"number": r"\-?[0-9]+(\.[0-9]+)?"
}

if __name__=='__main__':
	while True:
		print parse_phrase(raw_input("Enter a command > "), examples, regexes)
