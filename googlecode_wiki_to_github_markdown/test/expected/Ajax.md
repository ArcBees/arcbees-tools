# Ajax in GQuery

## Introduction

Gwt includes its own facilities for performing communications with the server:
 * RPC, Request Factory
 * Request Builder

But GQuery complements it adding:
 * jQuery syntax.
 * Builders to handle JSON and XML.

**NOTE**: Latest code in gquery-1.4.0-SNAPSHOT includes `Deferred` and `Promises` jQuery API.

## Available Methods
### ajax()
It is the most generic method to get data from servers in gquery, and it is fully configurable through the `Ajax.Settings` object.

It is used internally by the rest of gquery ajax methods : `load()`, `get()`, `post()`, `json()` and `jsonp()`.

```
    Ajax.ajax(Ajax.createSettings()
       .setUrl("miservice.php")
       .setDataType("xml") // txt, json, jsonp, xml
       .setType("get")     // post, get
       .setData(GQuery.$$("param1: 1, param2: 2")) // parameters for the query-string
       .setTimeout(3000)
       .setSuccess(new Function(){ // callback to be run if the request success
         public void f() {
           // The response when dataType=xml, is a dom tree which we can traverse using gquery
           Window.alert($(getDataObject()).find("a_tag").attr("an_attr"));
         }
       })
       .setError(new Function(){ // callback to be run if the request fails
         public void f() {
           Window.alert("There was an error" + getDataObject());
         }
       })
     );
```

### load()
Load a remote html fragment and append it to the element whose `id=c`.

```
    $("#c").load("file.html");
```

Load a remote html and append the fragment with `id=mid` from the returned document to the element with `id=c` in the current one

```
    $("#c").load("file.html #mid");
```

### get()
Request the server using GET protocol, the second parameter is the set of key-values pairs to compose the query string appended to the url. Leave this parameter as null if you do not want to pass any parameter.

In the callback `Function`, the method `getData()` returns an array where the first element is the data from the server, the second is the status (error, success), the third  is the `Request` object and the fourth one the `Response`.

If you want to pass an error callback function or a timeout, you have to use the [ajax()](Ajax.md#ajax) method with the `dataType` set to `get`

```
    GQuery.get("file.html", $$("name:'John',time:'2pm'"), new Function(){
      public void f() {
        alert("success " + getDataObject());
      }
    });
```

### post()
Request the server using POST protocol, the second parameter is the set of parameters to send to the server.

The first parameter is the target url. The second parameter is the set of key-values pairs to send in the post request. The third parameter is the function to be executed if the request succeeds.

In the callback `Function`, the method `getData()` returns an array where the first element is the data from the server, the second is the status (error, success), the third  is the `Request` object and the fourth one the `Response`.

If you want to pass an error callback function or a timeout, you have to use the [ajax()](Ajax.md#ajax) method with the `dataType` set to `post`

```
    GQuery.post("file.html",$$("name:'John',time:'2pm'"),
     new Function(){ public void f() {
        alert("success " + getDataObject());
    }});
```

### getJSON()
Request the server using POST protocol, and parse the response generating a Properties object.

The first parameter is the target url. The second parameter is the set of key-values pairs to send in the post request. The third parameter is the function to be executed if the request succeeds.

In the callback `Function`, the method `getDataProperties()` returns a properties which is a Overlay class wrapping the content of the `json` response.

If you want to pass an error callback function or a timeout, you have to use the [ajax()](Ajax.md#ajax) method with the `dataType` set to `json`

```
    GQuery.getJSON("file.html",$$("name:'John',time:'2pm'"),
      new Function(){ public void f() {
        alert("success " + getDataProperties().toJsonString());
    }});
```

### getJSONP()
Request the server using script tags so as the request is not subject to the same origin policy restrictions.
Note that the server must return a valid json object wrapped by a function call. You can redefine the parameter used by the server side to know the callback-name (if omitted gquery adds 'callback'), the question-mark will be replaced by the temporary callback exposed by gquery in the window object.

The first parameter is the target url. The second parameter is the set of key-values pairs to compose the query string appended to the url, leave this parameter as null if you do not want to pass any parameter or you already appended a query-string to the url. The third parameter is the function to be executed when the requested script loads, note that it will never be called if the service does not support jsonp requests.

In the callback `Function`, the method `getDataProperties()` returns a properties which is a Overlay class wrapping the content of the `json` response.

```
    GQuery.getJSONP("http://externalserver.com/service.php",
        GQuery.$$("callbackParameter: ?, otherParameter: 'abate ver'"),
        new Function(){ public void f() {
          Window.alert("success " + getDataProperties().toJsonString());
        }});

```

The only way to get an error in case the service is not a valid jsonp one, is setting a timeout for the call, to do that you have to use the [ajax()](Ajax.md#ajax) method with the dataType set to 'jsonp'

```
   GQuery.ajax(Ajax.createSettings()
       .setUrl("http://externalserver.com/service.php")
       .setData(GQuery.$$("param1: 1, param2: 2"))
       .setDataType("jsonp")
       .setTimeout(3000)
       .setSuccess(new Function(){
         public void f() {
           Window.alert("Server response: " + getDataProperties());
         }
       })
       .setError(new Function(){
         public void f() {
           Window.alert("There was a timeout, is this a valid jsonp service.");
         }
       })
     );
```

## CORS (Cross Origin Resource Sharing)

In order to make ajax calls to domains different to the one your script is deployed on, you need to use the getJSONP method or either a Cross-origin resource sharing (CORS) filter in the server side.

All modern browsers have support for CORS. The way to enable CORS in your server is adding a filter which takes care of certain headers.

This is an example of how to implement it in a servlet container, and it is compatible with any gwt ajax request type (gquery.ajax, request-builder, rpc, rf, etc):

```
 <filter>
   <filter-name>CORSFilter</filter-name>
   <filter-class>my.namespace.CORSFilter</filter-class>
 </filter>
 <filter-mapping>
   <filter-name>CORSFilter</filter-name>
   <url-pattern>/*</url-pattern>
 </filter-mapping>
```

```
public class CORSFilter implements Filter {
  // For security reasons set this regex to an appropriate value
  // example: ".*example\\.com"
  private static final String ALLOWED_DOMAINS_REGEXP = ".*";

  public void doFilter(ServletRequest servletRequest,
      ServletResponse servletResponse, FilterChain filterChain)
      throws IOException, ServletException {

    HttpServletRequest req = (HttpServletRequest) servletRequest;
    HttpServletResponse resp = (HttpServletResponse) servletResponse;

    String origin = req.getHeader("Origin");
    if (origin != null && origin.matches(ALLOWED_DOMAINS_REGEXP)) {
      resp.addHeader("Access-Control-Allow-Origin", origin);
      if ("options".equalsIgnoreCase(req.getMethod())) {
        resp.setHeader("Allow", "GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS");
        if (origin != null) {
          String headers = req.getHeader("Access-Control-Request-Headers");
          String method = req.getHeader("Access-Control-Request-Method");
          resp.addHeader("Access-Control-Allow-Methods", method);
          resp.addHeader("Access-Control-Allow-Headers", headers);
          // optional, only needed if you want to allow cookies.
          resp.addHeader("Access-Control-Allow-Credentials", "true");
          resp.setContentType("text/plain");
        }
        resp.getWriter().flush();
        return;
      }
    }

    // Fix ios6 caching post requests
    if ("post".equalsIgnoreCase(req.getMethod())) {
      resp.addHeader("Cache-Control", "no-cache");
    }

    if (filterChain != null) {
      filterChain.doFilter(req, resp);
    }
  }

  @Override public void destroy() {}
  @Override public void init(FilterConfig arg0) throws ServletException {}
}
```
