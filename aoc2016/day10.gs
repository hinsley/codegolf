# Note: nextWord and (especially) nextLine are quirky.
# Include at least 2 trailing newlines on the input.
# TODO: Abstract away the redundant code from nextLine/nextWord.

{{(1/([\]);\+}%}:acronymifyPairs;
{1/(.{\."\n"=}{;\(@\.@\+}until;\{+}*\}:nextLine;
{1/(.{\.." "=\"\n"= or}{;\(@\.@\+}until;);\{+}*\}:nextWord;
{["and" "gives" "goes" "high" "low" "to"]-}:simplifyCommand;
{[{."\n"=}{nextLine\}until;]}:splitLines;
{[{nextWord\.1/)\;"\n"=}do]}:splitWords;

splitLines
{splitWords simplifyCommand 2/ acronymifyPairs}%

