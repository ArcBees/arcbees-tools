# Handling JSON and XML with GQuery generators

## Introduction
Although Gquery provides the class `Properties` to handle Json objects, and Gquery is also able to inspect Xml objects using the css selector engine ...

```
    // Using Properties to handle JSON messages
    Properties p = $$("key1: 'value1', key2: [1,2]");
    String v1 = p.getStr("key1");

    // Traversing XML documents with GQuery
    Element e = JsUtils.parseXML("<root><message>hello</message></root>");
    String txt = $("root message", e).text();
```

... additionally Gquery provides generators to deal with Xml and Json as normal 'java' objects:

```
   s.setKey1("key1").setKey2(new long[]{1, 2});
   System.out.println(s.getKey1());
```

So as you can consider gquery as an alternative in client side to gwt autobeans or gwt json and xml parsers.

It support getters, setters, method chaining, attribute renaming via annotations, etc.
The usage of data binders makes the code more readable, type-saving, handing nulls, type castings, etc, without penalizing the performance.

The json implementation supports both server and client sides.

## Data Binding

### JSON
 * Given a JSON message

```
{
 "id": 1234,
 "referer": {"id": 2, "url": "http://google.com"},
 "url": "http://mochikit.com/interpreter/index.html",
 "title": "Interpreter",
 "tags": [
   "mochikit","webdev","tool","tools",
   "javascript","interactive","interpreter","repl"
  ]
}
```

 * Create an interface with setters and getters to handle the attributes.
Note that you can return the interface in setters to chain methods and use it as a classic builder.
You can use 'set' and 'get' prefixes or omit them, and you could change the name of the attribute using the @Name annotation.

```
  interface Site extends JsonBuilder {
    long getId();
    String getUrl();
    String[] getTags();
    // change the name to fix the misspelling
    @Name("referer")
    Site getReferrer();
    String getTitle();

    Site setId(long id);
    Site setUrl(String url);
    Site setTags(String[] tags);
    @Name("referer")
    Site setReferrer(Site site);
    Site setTitle(String title);
  }
```

 * Finally the `GWT.create()` to get an instance of your interface and use fill the object whether chaining setters or parsing a json message.

```
    Site s = GQ.create(Site.class);
    s.parse(xmlString);
    s.setId(123).setUrl("http://www.google.com");
```

 * Here you have a complete example Using Ajax

```
    GQuery.getJSON("test.json", null, new Function() {
      public void f() {
        // Create the Site instance and load the data got from server
        Site s = GQ.create(Site.class).load(arguments(0));
        // Now we can use standard getters and setters,
        // making our code more readable and type-safe
        alert("Response received: " +
            s.getUrl() + " " +
            s.getTags()[0] + " " +
            s.getReferrer().getUrl());
      }
    });
```

* Note that you must use an object as the root element and never an array.

### XML

 * Given a XML message, like this one taken from the gmail feeds service

```
<?xml version='1.0' encoding='UTF-8'?>
<feed version='0.3' xmlns='http://purl.org/atom/ns#'>
 <title>Gmail - Inbox for manolo@gquery.org</title>
 <tagline>New messages in your Gmail Inbox</tagline>
 <fullcount>30</fullcount>
 <link rel='alternate' href='http://mail.google.com/mail' type='text/html' />
 <modified>2012-11-07T10:32:52Z</modified>
 <entry>
  <title>Trending Startups and Updates</title>
  <summary>AngelList Weekly Trending Startups Storenvy Tumblr for stores E-Commerce Platforms · San Francisco</summary>
  <link rel='alternate' href='http://mail.google.com/mail?account_id=manolo@gquery.org&amp;message_id=13ad2e227da1488b&amp;view=conv&amp;extsrc=atom' type='text/html' />
  <modified>2012-11-05T23:22:47Z</modified>
  <issued>2012-11-05T23:22:47Z</issued>
  <id>tag:gmail.google.com,2004:1417840183363061889</id>
  <author>
   <name>AngelList</name>
   <email>noreply@....</email>
  </author>
 </entry>
</feed>
```

 * Create the interfaces which represents all xml elements

```
  interface Feed extends XmlBuilder {

    interface Tag extends XmlBuilder {
    }
    Tag getTitle();
    Tag getTagline();
    Tag getFullcount();
    Tag getModified();

    interface Link extends XmlBuilder {
      String getHref();
      String getType();
    }
    Link getLink();

    interface Entry extends XmlBuilder {
      interface Author extends XmlBuilder {
        Tag getEmail();
        Tag getName();
      }
      Tag getTitle();
      Tag getSummary();
      Link getLink();
      Tag getModified();
      Tag getIssued();
      Tag getId();
      Author getAuthor();
    }
    Entry[] getEntry();
  }
```

* Finally use `GWT.create()` to get an instance of the object and fill it from a xml string.

```
    Feed x = GWT.create(Feed.class);
    x.parse(xml);
    System.out.println(x.getTitle().getText());
    System.out.println(x.getEntry()[0]);
```

* Here you have a full example using xml databinding with gquery ajax:

```
    GQuery.ajax(Ajax.createSettings()
        .setUrl("http://webservice-proxy.mydomain.com")
        .setType("get")
        .setDataType("xml")
        .setTimeout(3000)
        .setSuccess(new Function(){
          public void f() {
            Feed f = GWT.create(Feed.class);
            f.load(getDataObject());
            Window.alert("There are " + f.getFullcount().getText() + " new messages in " + f.getTitle().getText());
          }
        })
        .setError(new Function(){
          public void f() {
            Window.alert("ERROR " + getDataObject());
          }
        })
      );
  }
```
