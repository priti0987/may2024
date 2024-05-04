package tests;

import static io.restassured.RestAssured.baseURI;
import static io.restassured.RestAssured.given;

import java.util.HashMap;
import java.util.Map;

import org.json.simple.JSONObject;
import org.testng.annotations.Test;

import io.restassured.http.ContentType;

public class PutPatchDeleteExamples {

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
			statusCode(201).
			log().all();
	}
	

}
