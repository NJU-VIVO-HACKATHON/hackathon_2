# hackathon_2
利用Flask搭建一个简单的服务器，调用OpenAI API生成文字和图片  

**文字生成**
```POST /aigc/chat```  
请求样例
```
Content-Type: application/json

{
  "prompt": "什么是python"
}
```
响应样例
```
Content-Type: text/html; charset=utf-8

Python是一种高级程序设计语言，具有直观易用、可读性强、简洁明了等特点。它的设计理念是代码简洁、容易理解、易于扩展和优化。Python语言广泛应用于计算机科学、网络编程、数据分析、人工智能等各个领域。Python具有良好的跨平台性，可以在Windows、Mac
OS X、Linux等各种操作系统上运行。Python代码可以被解释和编译两种方式执行，具有良好的灵活性和可维护性。
```

**图片生成**
```POST /aigc/image```
请求样例
```
Content-Type: application/json

{
  "prompt": "什么是python"
}
```
响应样例
```
Content-Type: text/html; charset=utf-8

https://oaidalleapiprodscus.blob.core.windows.net/private/org-nQ2su19ado3KvvI9HE5vAZHO/user-JlsAnxnI90hX4zqaVZVn5YSu/img-CDtufIwtuOhfliJ8EXoizMWp.png?st=2023-05-21T23%3A39%3A44Z&se=2023-05-22T01%3A39%3A44Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-05-21T16%3A21%3A21Z&ske=2023-05-22T16%3A21%3A21Z&sks=b&skv=2021-08-06&sig=cBV5HyjotkrQ7LJU7DhK%2B8kPyp0/NVx7P2KUpis1lW0%3D
```

