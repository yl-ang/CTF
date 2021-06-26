/*

We inspect element the site and found some code in the .js script:

var pass = unescape("unescape%28%22String.fromCharCode%252867%252C68%252C68%252C67%252C50%252C49%252C123%252C95%252C32%252C68%252C101%252C48%252C98%252C102%252C117%252C36%252C99%252C97%252C116%252C101%252C100%252C45%252C70%252C33%252C97%252C71%252C95%252C125%2529%22%29");

which is URl encoded, we decoded it to:

(67,68,68,67,50,49,123,95,32,68,101,48,98,102,117,36,99,97,116,101,100,45,70,33,97,71,95,125)

Then we convert it from decimal to Ascii and got the flag:
CDDC21{_ De0bfu$cated-F!aG_}
*/