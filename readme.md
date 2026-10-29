# **两种IP的区别**
## 入口IP，从本地连接到cf worker
    本机 → CF 边缘（入口），优化目标入口延迟低、不绕路，可以用优选域名保底
## proxyip，从worker连接到访问的网址，例如youtube 币安
    出口能连通、地区对、风控好。所谓优选IP，基本指这个，这个最重要
# ProxyIP来源：
## 原生运营商 jp1
    来自日本原生运营商，IP稀少，一个月只有三四个
## CF中转IP发布 jp
    来自CF中转IP发布，这里的IP非常多，而且基本有效，挑选其中延时低的
    https://zip.cm.edu.kg
## ProxyIP.JP.CMLiussss.net
    从各大博主分享的ProxyIP网址解析出来
# 操作流程
 - 1.通过fofa搜索ip,推荐当地本土原生运营商，不要用国际大厂    
 - 2.筛选可用的ip：ProxyIP.JP.CMLiussss.net，https://check.proxyip.cmliussss.net/     
 - 3.导入客户端，挑选低延迟的ip，做为 proxyip 与 优先ip，两个设置成一样的     
 - 4.测试网站连通性与延迟     
https://bestcf.pages.dev/tiancheng/all.txt?port=443    
https://bestcf.pages.dev/wetest/ipv4.txt   
https://bestcf.pages.dev/lzj/all.txt   
https://raw.githubusercontent.com/cc1nt/ip/main/tw1.txt    
https://raw.githubusercontent.com/cc1nt/ip/main/jp2.txt#jp2    
![原生](pic/jp1.png)
![中转](pic/jp2.png)
# 更新
2026年10月29日11:46:25  新增jp0,从池子里筛选风控度低的IP    
## **日本风控偏低**（原生 ISP / 老牌本土运营商）
- 2914|4713|2514|2516|17676|4694|2497|2518|4685|9605|2527|17511|7679|10010|18126|9824|4725|10013|9595|2519|2510     
- country="JP" && server="cloudflare" && port="443" && status_code="403" && (asn="2914"||asn="4713"||asn="2516"||asn="17676"||asn="2497"||asn="2518"||asn="2514"||asn="4685"||asn="9605") && is_honeypot=false
- 可以直接问AI