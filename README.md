# Lambda Function Template
This is the base set of code for building Tableau REST API functions that can be deployed with AWS Lambda.

To make this work, clone this repo, create a branch and write your Python script. If you want it to work independently, you are done once your code functions. If you want it to interact with the event or context that triggered it (like an S3 object being created), here's your [next set of reading](http://docs.aws.amazon.com/lambda/latest/dg/python-programming-model.html). When you are all done, push your new branch and submit a pull request.

Select everything in the folder, create a ZIP and upload it to Lambda.

The most important part is getting your function handler right. Lambda needs to know what function to invoke when it gets triggered.

### Here's the formula

```
[filename].function_handler
```

With the included sample, this would be 

```
sample.function_handler
```

That's it!

If you want to learn more, keep reading, otherwise --> Happy Coding!

---

### What is Lambda

AWS Lambda is a way to run code without the need for servers. It accepts these common languages

+ Python 2.7 
+ Java 8
+ NodeJS
+ Node.js 4.3

The core idea is to write code that responds to an event

+ Timer
+ S3 events (objects being created, deleted)
+ API Gateway requests
+ Kinesis stream events
+ Notifications via SNS
+ Amazon Echo (Alexa - do something)

The full documentation around Lambda events can be found [here](http://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html)

This makes Lambda an excellent home for automation tasks. 

---

### Tableau Rest API

Many (but not all) of the initial automation tasks can be accomplished with Tableau's REST API. Python and Node can interact with API requests quite easily (Postman can generate the code you need - and then you parse it). 

Python goes a step further. Bryant Howell (author of [Tableau and Behold](https://tableauandbehold.com)) created a very nice library for interacting with the REST API. It's called [tableau_tools](https://github.com/bryantbhowell/tableau_tools). It uses a simple syntax for querying, adding and deleting. 

#### Sign in and find all your site URLs

```
t = TableauRestApiConnection(u"http://127.0.0.1", u"admin", u"adminsp@ssw0rd", site_content_url=u"site1")
t.signin()
sites = t.query_all_site_content_urls()
print sites
```

There are many more options you can choose from, but it's easy to read and understand, and he even does the job of creating the XML objects for you to interact with, no more loading XML in and out. Just find the parts of the document you want. 

#### Find all users with site role of Unlicensed

```
Sign in
users = t.query_users()
for user in users: 
  if user.attrib['siteRole']=='Unlicensed':
    print user
```

---

## Creating Lambda functions

Out of the gate, AWS supplies the basic Python libraries (similar to what you would find on a vanilla Linux machine). They also include all the AWS command line options ([boto](https://aws.amazon.com/sdk-for-python/)) so you can interact with all their capabilities.

However, because tableau_tools is an external library, you need to package it with your function, otherwise it won't work. The template contains all those dependencies, so you don't have to worry about them, including tableau_tools.

If you can't download the repo yourself (for whatever reason), here's how  you can build your own template.

On Linux (this will not work on windows), run the following script on an AWS Linux AMI
```
Launch an ec2 machine with Amazon Linux ami
Run the following script to accumulate dependencies:
set -e -o pipefail
sudo yum -y upgrade
sudo yum -y install gcc python-devel libxml2-devel libxslt-devel

virtualenv ~/env && cd ~/env && source bin/activate
pip install lxml
for dir in lib64/python2.7/site-packages \
    lib/python2.7/site-packages
do
    if [ -d $dir ] ; then
        pushd $dir; zip -r ~/deps.zip .; popd
    fi
done 
```

then run ```pip install tableau_tools -t \\path\to\folder\```

That will accumulate everything you need in one place!
