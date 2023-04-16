import java.rmi.*;
import java.rmi.server.*;
import java.util.*;
public class ServerDate extends UnicastRemoteObject implements 
InterDate {
public ServerDate() throws Exception
{
}
public String display() throws Exception
{
String str = "";
Date d = new Date();
str = d.toString();
return str;
}
public static void main(String args[]) throws 
Exception {
ServerDate s1 = new ServerDate();
Naming.bind("DS",s1);
System.out.println("Object registered.....");
}
}