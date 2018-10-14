练习tkinter和SMTP发送邮件时写的练习代码，主要实现了通过界面来进行邮件发送。
python版本：3.7

说下其中的坑：
1.tkinter的Text组件中，看官方API，获取输入内容，也是使用get()方法，但没有找到太多内容，结果就是导致调用get时，报 ‘tkinter.get() missing 1 required  positional  arguments index1’
这个错误，其实就是参数错误。Entry组件是支持直接调用get()这个方法的。实际上Text的get需要传入参数，get('1.0',END)，类似如此参数
