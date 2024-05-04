package tPostExamplesests;

import org.json.simple.JSONObject;
import org.testng.annotations.Test;

import io.restassured.http.ContentType;

import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

import java.util.HashMap;
import java.util.Map;



public class GetAndPostExamples {
	
	@Test
	public void testGet() {
		baseURI = "https://reqres.in/api";
		given().
			get("/users?page=2").
		then().statusCode(200).body("data[4].first_name",equalTo("George")).
			body("data.first_name",hasItems("George","Rachel"));
		
	}
	
	
	@Test
	public void testPut()
	{
		Map<String, Object> map = new HashMap<String,Object>();
		map.put("name","priti");
		map.put("job","teacher");
	
		JSONObject request = new JSONObject(map);
		System.out.println(map);
		System.out.println(request.toJSONString());
		baseURI = "https://reqres.in/api";
		
		given().
			header("Content-Type","application/json").
			contentType(ContentType.JSON).
			accept(ContentType.JSON).
			body(request.toJSONString()).
		when().
			put("/users/2").
		then().
			statusCode(200).
			log().all();
	}
	@Test
	public void testPatch()
	{
		Map<String, Object> map = new HashMap<String,Object>();
		map.put("name","priti");
		map.put("job","teacher");
	
		JSONObject request = new JSONObject(map);
		System.out.println(map);
		System.out.println(request.toJSONString());
		baseURI = "https://reqres.in/api";
		
		given().
			header("Content-Type","application/json").
			contentType(ContentType.JSON).
			accept(ContentType.JSON).
			body(request.toJSONString()).
		when().
			patch("/users/2").
		then().
			statusCode(200).
			log().all();
	}
	
	@Test
	public void testDelete()
	{
		baseURI = "https://reqres.in/api";
		
		when().
			delete("/users/2").
		then().
			statusCode(204).
			log().all();
	}

}
