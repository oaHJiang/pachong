# 动态网页爬虫
# 什么是动态网页爬虫和 AJAX 技术：
# 1．动态网页，是网站在不重新加载的情况下，通过ajax技术动态更新网站中的局部数据。比如拉勾网的职位页面，在换页的过程中， url是没有发生改变的，但是职位数据动态的更改了。
# 2.AJAX(Asynchronouse JavaScript And XML ）异步JavaScript和XML 。前端与服务器进行少量数据交换， Ajax可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。传统的网页（不使用Ajax )如果需要更新内容，必须重载整个网贝负面。因为传统的在传输数据格式方面，使用的是XML语法。因此叫做AJAX ，其实现在数据交互基本上都是使用JSON 。使用AJAX加载的数据，即使使用了ajax加载的数据，只能看到使用这个url加载的html代码。
# 动态网页爬虫的解决方案：
# 1．直接分析ajax调用的接口。然后通过代码请求这个接口。
# 2．使用Selenium + chromedriver模拟浏览器行为获取数据。