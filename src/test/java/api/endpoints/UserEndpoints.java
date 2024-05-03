package api.endpoints;

import static io.restassured.RestAssured.given;
import io.restassured.http.ContentType;
import io.restassured.response.Response;

import api.payload.User;
/*
 * Created for perform Create , Read , Update, Delete requests the user API.
 */
public class UserEndpoints {
	
	public static Response createUser(User payload){

		Response response = given()
			.contentType(ContentType.JSON)
			.accept(ContentType.JSON)
			.body(payload)
		.when()
			.post(Routes.post_url);
		return response;
	}

	public static Response readUser(String userName){

		Response response = given()
							.pathParam("username", userName)
				
				.when()
					.post(Routes.post_url);
		return response;
	}

	public static Response updateUser(String userName,User payload){

		Response response = given()
			.contentType(ContentType.JSON)
			.accept(ContentType.JSON)
			.pathParam("username", payload)
			.body(payload)
		.when()
			.post(Routes.update_url);
		return response;
	}

	public static Response deleteUser(String userName){

		Response response = given()
				.pathParam("username", userName)
				.when()
			.post(Routes.delete_url);
		return response;
	}

}
