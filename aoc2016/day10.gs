# Note: nextWord and (especially) nextLine are quirky.
# Include at least 2 trailing newlines on the input.
# TODO: Abstract away the redundant code from nextLine/nextWord.

{1/(.{\."\n"=}{;\(@\.@\+}until;\{+}*\}:nextLine;
{1/(.{\.." "=\"\n"= or}{;\(@\.@\+}until;);\{+}*\}:nextWord;
{[{nextWord\.1/)\;"\n"=}do]}:splitWords;

