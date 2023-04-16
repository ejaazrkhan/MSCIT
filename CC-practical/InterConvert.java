import java.rmi.*;
public interface InterConvert extends Remote
{
public String convertDigit(String no) throws Exception;
}