/*Program which calculate factorial of a number*/
import java.io.*;
import java.net.*;
public class udpServerFact
{
public static void main(String args[])
{
try
{
DatagramSocket ds = new DatagramSocket(2000); 
byte b[] = new byte[1024];
DatagramPacket dp = new DatagramPacket(b,b.length); 
ds.receive(dp);
String str = new 
String(dp.getData(),0,dp.getLength()); 
System.out.println(str);
int a= Integer.parseInt(str);
int f = 1, i;
String s= new String();
for(i=1;i<=a;i++)
{
f=f*i;
}
s=Integer.toString(f);
String str1 = "The Factorial of " + str + " is : " + 
f; byte b1[] = new byte[1024]; b1 = 
str1.getBytes();
DatagramPacket dp1 = new
DatagramPacket(b1,b1.length,InetAddress.getLocalHost(),1000);
ds.send(dp1);
}
catch(Exception e)
{
e.printStackTrace();
}
}
}
