from s3v2 import * # from wafflehouse import * means the function can be used as globals (all globals in that file/lib become globals for me too) I can use wafflehouse's pancake() function just by calling pancake(x) ... if I used import wafflehouse I have access to the file/lib's functions, but not as globals, so I need to associate them with wafflehouse, so to call the pancake() function I would need to use: wafflehouse.pancake(x). General rule of thumb: use import instead of from X import * because import alone keeps my globals less cluttered and makes my code more clearly readable (as I know where the functions and variables came from that I'm referencing). More here: http://stackoverflow.com/questions/5124232/what-is-the-difference-between-import-modx-and-from-modx-import


gucci_ties = filter_col_by_string(data_from_csv, 'brandName', 'Gucci')
jcrew_ties = filter_col_by_string(data_from_csv, 'brandName', 'J.Crew') # this wasn't working because the brand name for J. Crew is "J.Crew" not "J. Crew". It seems like these sorts of errors are common when you're working with a new data_set. Isn't munging about removing formatting and otherwise making these sorts of errors less likely?

max_gucci = find_max(gucci_ties[1:], 2)
max_jcrew = find_max_min(jcrew_ties[1:], 2)

message = "Maximum {} tie price is ${:03.2f}"
print(message.format("Gucci", max_gucci))


# print(gucci_ties[:2]) # this how you slice into a list to return only some of the results. In this case the first two rows. I used this originally to take a look at the jcrew_ties list. I found that we only had a header row, which meant that the list wasn't populated with data. So I looked directaly at the csv file and noticed the brand name didn't have a space between J. and Crew (i.e. "J.Crew" NOT "J. Crew")