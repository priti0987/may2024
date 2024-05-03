package collections;

import java.util.HashMap;

public class hashmap {

	public static void main(String[] args)
	{
		HashMap m = new HashMap();
		//HashMap<Integer, String > m = new HashMap<Integer, String>();	
	
		m.put(1, "priti");
		m.put(2, "priya");
		m.put(3, "bhavika");
		m.put(4, "pratap");
		m.put(5, "neel");
		m.put(6, "shriya");
		m.put(6, "anvit");
		m.put(7, "shriya");
		m.put(8, "shriya");

		
		System.out.println(m); //{1=priti, 2=priya, 3=bhavika, 4=pratap, 5=neel, 6=anvit, 7=shriya, 8=shriya}


		//get
		System.out.println(m.get(1));//priti
		m.remove(6);
		System.out.println(m);
		
	}
}
