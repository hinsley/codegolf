{{(1/([\]);\+}%}:acronymifyPairs;
{["and" "gives" "goes" "high" "low" "to"]-}:simplifyCommand;
{"\n"/}:splitLines;
{" "/}:splitWords;

splitLines
{splitWords simplifyCommand 2/ acronymifyPairs}%

