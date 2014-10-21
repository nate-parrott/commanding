# Commanding.py

A simple module for parsing natural-language commands in Python.

[Astro-bot](http://astro-bot.appspot.com) using `commanding` to parse commands to allow people to browse the web over SMS (or in an online demo). Try it out.

## Usage

In `commanding`, you provide examples of natural-language phrases, annotated with `intent`s and with portions of their text marked with `tags.` Then, let `commanding` parse any string into a structured format, with an `intent` and `tagged` text, just like your examples.

### Providing examples

You give `commanding` a set of *sample phrases.* You give each sample phrase an *intent* and a set of "tags" marking certain parts of the text.

For example, in "send a text to Mary saying hello world", you might mark the intent as "send_text", and tag "hello world" as "~message" and "mary" as "recipient." (tags with names beginning with ~'s are 'free-text' tags — marking them with this convention helps the parser.)

The `Phrase` object is used to define examples (with specified intents and tags). It's also the object you get back when you run the parser on a string.

Here's what some examples look like (from `example.py`):

```
	Phrase("contents", ["show me the table of contents"]), # an intent w/ no tags
	Phrase("search", ["search the web for", ["~query", "kanye west"]]), # ~query is a tag
	Phrase("search", [["search_source/wikipedia", "show me the wikipedia article for"], ["~query", "the grateful dead"]]) # search_source/wikipedia and ~query are tags
```

If you wanted to recognize commands like "search the web for san francisco now!", with an intent `search`, you'd give `phrases` like `Phrase("search", ["search the web for", ["~query", "san francisco"], "now!"])` Ideally, you should give a lot of differently phrased examples.

### Parsing queries

Once you have examples, call 
```phrase = parse_phrase("web search for san francisco", [your list of examples])```
 and you'll get backed a `Phrase` object. The `intent` will be `search`. To extract the `~query,` call phrase.get("~query") (it'll return `None` if no query could be found).

### Free-text tags (~tags)

By default, `commanding` assumes that each tag has a specific set of words that are more likely to appear in it. For tagging things like times or types of candy, this works well, but it doesn't work so well for free-text things like search queries or tweet messages. Tell `commanding` to ignore word-frequency on certain tags by prefixing the tag with ~.

### Regex tags (*tags)

Tags can also be identified using regexes — for example, in the command "print this 5 times," you might tag "5" as a number, in which case you miht want to use a regex to tell `commanding` what a number is. To do this, prefix your tag name with "*", then provide a dictionary that maps regex tag names to regexes, and pass this is in as the third argument to `parse_phrase`

For example: (from example.py)

```
	...
	Phrase("more_text", [["*number", "3"], "more pages"]),
	Phrase("url", ["show", ["*url", "google.com"]])
]
regexes = {
"url": r"[a-zA-Z0-9_\-\.]+\.[a-z]+(\/[^ ]*)?",
"number": r"\-?[0-9]+(\.[0-9]+)?",
}

if __name__=='__main__':
	while True:
		print parse_phrase(raw_input("Enter a command > "), examples, regexes)

```

